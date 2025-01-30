from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]) #raiting: valutazione
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False) # editable=Flase, SIGNIFICA CHE IL CAMPO NON PUO' ESSERE MODIFICATO
                                                                                # blank=True, SIGNIFICA CHE IL CAMPO PUO' ESSERE VUOTO
    
    def __str__(self):
        return f"{self.title}" # QUESTO SERVE PER RENDERE VISIBILE IL TITOLO SU /ADMIN/
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
