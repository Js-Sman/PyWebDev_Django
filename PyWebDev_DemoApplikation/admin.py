from django.contrib import admin
from .models import Notice  # Hier müssen alle Klassen aufgeführt werden die in der Admin Web oberfläche
# als datenbank Sichtbar sein sollen

# Register your models here.
admin.site.register(Notice) # Und so werden die Models Registriert

