from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)  # E' UNA TUPLA E RENDE UN DATO VISIBILE IN SOLO LETTURA SENZA POTERLO MODIFICARE
    prepopulated_fields = {"slug": ("title",)} # QUESTO SERVE PER MOSTRARE IN TEMPO REALE COME SARA' LO SLUG. IL PRIMO NEL DIZIONARIO DEVE ESSERE
                                              # UN CAMPO DEL DB E IL SECONDO LO SLUG DEVE ESSERE BASATO SU QUALE CAMPO
    list_filter = ("rating",) # CI PERMETTE DI FILTRARE PER UNO SPECIFICO CAMPO DEL DB
    list_display = ("title", "author") # QUESTO CI PERMETTE DI VISUALIZZARE SUBITO IL TITOLO E L'AUTORE
    
admin.site.register(Book, BookAdmin)