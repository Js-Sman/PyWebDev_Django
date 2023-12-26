from django.urls import path
from . import views  # Nötig um von hier aus auf die verschiedenen views zu routen

urlpatterns = [
    path('learning1', views.index_learning1, name='index_learning1'),
    path('learning2', views.index_learning2, name='index_learning2'),
    path('', views.index, name='index'),
    path('new', views.new_notice, name='new'),
]

# der 1. Parameter in path() würde angeben was noch in der url steht → aktuell kommt man hier hin, indem man in die url
# noch einen /demo schreibt.
# wenn man danach nichts weiter angibt, landet man also im view file.
# mit dem views.index wird die Funktion "index" ausgeführt, die in der views datei liegt.


