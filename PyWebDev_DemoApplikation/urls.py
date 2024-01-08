from django.urls import path
from . import views  # Nötig um von hier aus auf die verschiedenen views zu routen

"""
Hier ist der Eingang zu dieser Applikation. Die URL's die hier angelegt werden, führen zu den View-Funktionen.
-1. Parameter: erweiterung der URL, wenn leer dann rendert die angegebene View-Funktion die Hauptseite der Applikation
-2. Parameter: die View-Funktion die mit dieser URL aufgerufen wird
-3. Parameter: der Name mit der diese spezielle URL später im Programm dynamisch verwendet werden kann
"""

urlpatterns = [
    path('learning1', views.index_learning1, name='index_learning1'),
    path('learning2', views.index_learning2, name='index_learning2'),

    path('', views.index, name='index'),
    path('new', views.new_notice, name='new'),
    path('delete/<int:delete_id>', views.delete_notice, name='delete'),
    # In eine URL können weitere Parameter in <> eingebettet werden.
    # Die Bezeichnung dieser zusätzlichen Parameter muss jedoch beim Übergeben erhalten bleiben!
    # Wenn diese Parameter mit einem href erzeugt werden, muss der Name ebenfalls identisch sein!

    # Für die REST Schnittstelle braucht es neue View-Funktionen, welche die Daten Serializieren
    path('notice/', views.notice_list, name='notice_list'),
    path('notice/<int:notice_id>', views.notice_detail, name='notice_detail')
]




