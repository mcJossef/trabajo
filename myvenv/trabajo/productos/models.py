from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    gmail = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} (Email: {self.gmail})"

class Rol(models.Model):
    tipo = models.CharField(max_length=45)
    usuario_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo} (Usuario ID: {self.usuario_usuario.id})"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='productos')

    def __str__(self):
        return self.nombre
    
class Imagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/imagenes/')

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"