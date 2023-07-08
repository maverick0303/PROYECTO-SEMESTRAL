from .models import Producto
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def add(self, producto):
        id = str(producto.cod_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "product_id": producto.cod_producto,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
                "stock": producto.stock
            }
        else:
            if self.carrito[id]["stock"] <= 0:
                # Si el stock es 0, no se puede agregar más al carrito
                return

            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
            self.carrito[id]["stock"] -= 1

        # Actualizar el stock en el objeto producto original
        producto.stock = self.carrito[id]["stock"]
        producto.save()
        self.save()

    def subtract(self, producto):
        id = str(producto.cod_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            self.carrito[id]["stock"] += 1

            if self.carrito[id]["cantidad"] <= 0:
                self.delete(producto)
            else:
                # Actualizar el stock en el objeto producto original
                producto.stock = self.carrito[id]["stock"]
                producto.save()

            self.save()

    def save(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def delete(self, producto):
        id = str(producto.cod_producto)
        if id in self.carrito:
            del self.carrito[id]

        # Restaurar el stock en el objeto producto original
        producto.stock = producto.stock + self.carrito[id].get("cantidad", 0)
        producto.save()

        self.save()

    def clean(self):
        for id, item in self.carrito.items():
            # Restaurar el stock en los objetos producto originales
            producto = Producto.objects.get(cod_producto=item["product_id"])
            producto.stock = producto.stock + item.get("cantidad", 0)
            producto.save()

        self.session["carrito"] = {}
        self.session.modified = True
