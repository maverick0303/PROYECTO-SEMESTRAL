from django.db import models

# Create your models here.
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=30)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=13)
    correo = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    telefono = models.CharField(max_length=13)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE)

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=30)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    f_venta = models.DateField()
    f_despacho = models.DateField()
    f_entrega = models.DateField()
    total = models.IntegerField()
    carrito = models.BooleanField(verbose_name='para saber si el usuario tiene objetos en el carrito')
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

class Producto(models.Model):
    cod_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=60)
    stock = models.IntegerField()  
    foto = models.ImageField(upload_to="tiendita")
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)