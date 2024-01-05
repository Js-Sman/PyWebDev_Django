from django.urls import path
from . import views  # Nötig um von hier aus auf die verschiedenen views zu routen

urlpatterns = [
    path('learning1', views.index_learning1, name='index_learning1'),
    path('learning2', views.index_learning2, name='index_learning2'),

    path('', views.index, name='index'),
    path('new', views.new_notice, name='new'),
    path('delete/<int:delete_id>', views.delete_notice, name='delete'),
    # In die url können in <> alle möglichen parameter mit eingebettet werden
    # Diese können in den views mit den href's beschrieben werden

    # Für die REST Schnittstelle braucht es neue View-Funktionen, welche die Daten Serializieren
    # path('notice/', views.notice_list, name='notice_list'),
    # path('notice/<int:notice_id>', views.notice_detail, name='notice_detail')
]

# der 1. Parameter in path() würde angeben was noch in der url steht → aktuell kommt man hier hin, indem man in die url
# noch einen /demo schreibt.
# wenn man danach nichts weiter angibt, landet man also im view file.
# mit dem views.index wird die Funktion "index" ausgeführt, die in der views datei liegt.


