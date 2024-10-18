from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Categoria(models.Model):
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()
    
    def __str__(self):
        return self.descripcion

class Unidad(models.Model):
    ratio = models.CharField(max_length=30)
    formula = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ratio} - {self.formula}'
    
class Unidad2(models.Model):
    ratio = models.CharField(max_length=30)
    formula = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ratio} - {self.formula}'


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    direccion = models.TextField()

    def clean(self):
        super().clean()
        if len(self.documento) != 8 or not self.documento.isdigit():
            raise ValidationError("El documento debe contener exactamente 8 dígitos.")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    class Meta:
        ordering = ['apellidos', 'nombre']
        
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion
        
