#CONSTRUCTOR DE LA CLASE CARRITO:
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")

        if not carrito:
            self.session["carrito"] = {} 
            self.carrito = self.session ["carrito"]
        else:
            self.carrito = carrito

#METODO PARA AÑADIR EL PRODUCTO:
    def add(self, producto):
        id = str(producto.cod_producto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "product_id" : producto.cod_producto,
                "nombre" : producto.nombre,
                "acumulado": producto.precio,
                "cantidad" : 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.save()
    
    # RESTAR PRODUCTO:
    def subtract(self, producto):
        id = str(producto.cod_producto)
        self.carrito[id]["cantidad"] -= 1
        self.carrito[id]["acumulado"] -= producto.precio
        if self.carrito[id]["cantidad"] <= 0: self.delete(producto)
        else:
            self.session["carrito"] = {}
        self.save()

    # METODO PARA GUARDAR: 
    def save(self): 
        self.session["carrito"] = self.carrito
        self.session.modifield = True

    #ELIMINAR:
    def delete(self, producto):
        id = str(producto.cod_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.save() 

    #LIMPIAR:
    def clean(self):
        self.session["carrito"] = {}
        self.session.modifield = True


