from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Juego(models.Model):
    PLATAFORMAS = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('PlayStation', 'PlayStation'),
        ('Switch', 'Switch'),]


    titulo = models.CharField(max_length=100)
    plataforma =models.CharField(max_length=20, choices=PLATAFORMAS)
    precio = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    fecha_lanzamiento = models.DateField()

    def __str__(self) -> str:
        return self.titulo