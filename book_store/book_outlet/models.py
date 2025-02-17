from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}, {self.code}"
    
    class Meta:
        verbose_name_plural = "Country"
    
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # OneToOneField RELAZIONE UNO A UNO
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]) #raiting: valutazione
    # ForeignKey RELAZIONE UNO A MOLTI
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False) # editable=Flase, SIGNIFICA CHE IL CAMPO NON PUO' ESSERE MODIFICATO
                                                                                # blank=True, SIGNIFICA CHE IL CAMPO PUO' ESSERE VUOTO
    published_countries = models.ManyToManyField(Country)
    
    def __str__(self):
        return f"{self.title}" # QUESTO SERVE PER RENDERE VISIBILE IL TITOLO SU /ADMIN/
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
