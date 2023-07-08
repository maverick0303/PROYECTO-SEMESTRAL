class Carrito:
    def __init__(self, request):
        """
        Constructor de la clase Carrito.
        Inicializa el carrito de compras en la sesión del usuario.
        """
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")

        if not carrito:
            # Si no existe un carrito en la sesión, se crea uno vacío.
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            # Si ya existe un carrito en la sesión, se asigna a la variable de instancia.
            self.carrito = carrito

    def add(self, producto):
        """
        Agrega un producto al carrito de compras.
        Si el producto ya está en el carrito, se incrementa la cantidad y el acumulado de precio.
        Si el producto tiene stock disponible, se agrega la cantidad disponible al carrito.
        """
        id = str(producto.cod_producto)
        if id not in self.carrito.keys():
            # Si el producto no está en el carrito, se agrega con cantidad 1 y se actualizan los datos.
            self.carrito[id] = {
                "product_id": producto.cod_producto,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
                "stock": producto.stock
            }
        else:
            stock_disponible = self.carrito[id]["stock"]
            if stock_disponible > 0:
                cantidad_a_agregar = min(stock_disponible, producto.stock)
                # Si el producto está en el carrito y tiene stock disponible, se agrega la cantidad disponible al carrito.
                self.carrito[id]["cantidad"] += cantidad_a_agregar
                self.carrito[id]["acumulado"] += producto.precio * cantidad_a_agregar
                self.carrito[id]["stock"] -= cantidad_a_agregar

        # Actualizar el stock en el objeto producto original
        producto.stock = self.carrito[id]["stock"]
        producto.save()
        self.save()

        # Marcar 0 cuando se compra todo el stock
        if self.carrito[id]["stock"] == 0:
            self.carrito[id]["stock"] = 0

    def subtract(self, producto):
        """
        Resta un producto del carrito de compras.
        Si la cantidad del producto en el carrito es mayor a 1, se disminuye la cantidad y el acumulado de precio.
        Si la cantidad del producto en el carrito es 1, no se elimina el producto del carrito.
        """
        id = str(producto.cod_producto)
        if self.carrito[id]["cantidad"] > 1:
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            self.carrito[id]["stock"] += 1
        else:
            self.carrito[id]["cantidad"] = 1
            self.carrito[id]["acumulado"] = producto.precio
            self.carrito[id]["stock"] += 1

        # Actualizar el stock en el objeto producto original
        producto.stock = self.carrito[id]["stock"]
        producto.save()
        self.save()

    def save(self):
        """
        Guarda los cambios realizados en el carrito en la sesión del usuario.
        """
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def delete(self, producto):
        """
        Elimina un producto del carrito de compras.
        """
        id = str(producto.cod_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.save()

    def clean(self):
        """
        Limpia el carrito de compras, eliminando todos los productos.
        """
        self.session["carrito"] = {}
        self.session.modified = True
