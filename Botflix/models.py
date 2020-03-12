from django.db import models

# Create your models here.
class Pregunta(models.Model):
    textoPregunta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoPregunta

class Respuesta(models.Model):
    preg = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textoRespuesta = models.CharField(max_length=200)
    def __str__(self):
        return self.textoRespuesta

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=200)
    descripcion= models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):
        return "Producto: {} precio: $ {}".format(self.nombreProducto, self.precio)

class Miembro(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre       
