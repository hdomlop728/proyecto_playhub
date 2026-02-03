from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    juego_titulo = models.CharField(max_length=200)
    puntuacion = models.IntegerField()
    comentarios = models.TextField()
    fecha = models.DateField(auto_now_add=True)
