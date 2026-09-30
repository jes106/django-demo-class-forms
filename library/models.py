from django.utils.timezone import now
from django.db import models

TYPES_OF_BOOKS = [
    ("NOVELA", "Novela"), 
    ("CIENCIA FICCIÓN", "Ciencia Ficción"), 
    ("ENCICLOPEDIA", "Enciclopedia"), 
    ("OTROS", "Otros")
]

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=70)
    category = models.CharField(choices=TYPES_OF_BOOKS, max_length=15)
    price = models.FloatField()
    date_released = models.DateField()
    date_added = models.DateField(auto_now_add=True)