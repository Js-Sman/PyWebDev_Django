from django.urls import path
from . import views  # Nötig um von hier aus auf die verschiedenen views zu routen

"""
Hier ist der Eingang zu dieser Applikation. Die URL's die hier angelegt werden, führen zu den View-Funktionen.
-1. Parameter: erweiterung der URL
-2. Parameter: die Viewfunktion die mit dieser URL aufgerufen wird
-3. Parameter: der Name mit der diese spezielle URL später im Programm dynamisch verwendet werden kann
"""

urlpatterns = [
    path('', views.index, name='index'),
]

