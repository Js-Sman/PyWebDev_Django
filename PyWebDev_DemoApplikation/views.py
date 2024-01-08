import time

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_learning(request):
    """
    Um eine eigene Seite anzuzeigen, muss eine HTML-Seite gerendert werden
    Beim rendern muss der auslösende request mit angegeben werden, der Pfad der zum HTML Template führt und es kann
    ein context Objekt mit übergeben werden
    Das context-Objekt ist ein Dictionary, welches dynamisch in der View-Funktion befüllt werden kann.
    Im HTML-Template kann dann über die key's auf die Inhalte des context-Objekts zugegriffen werden

    :return: Es wird eine HTML-Seite mit Inhalten befüllt
    """

    timestring = time.strftime("%H:%M:%S")  # So würde man ein time format selber definieren
    context = {'now': timestring,
               'time': time.localtime(),
               'list': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}

    return render(request, 'demo/index_mitBaseVererbung.html', context)


def index(request):
    timestring = time.strftime("%H:%M:%S")  # So würde man ein time format selber definieren
    context = {'now': timestring,
               'time': time.localtime(),
               'list': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}  # der kontext wird als dict übergeben
    return render(request, 'demo/index.html', context)
