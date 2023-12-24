import time

from django.shortcuts import render
from django.http import HttpResponse

from PyWebDev_DemoApplikation.models import Notice


# Create your views here.
def index_learning1(request):
    # Mit einfachen "HttpResponse" kann man z.b Text zurück geben
    # Wenn man jedoch eine Seite in HTML zurück liefer möchte muss diese gerendert werden.

    # Diese Funktion wird ganz normal abgearbeitet, wenn sie Aufgerufen wird
    # dynamische Inhalte können hier demnach ganz einfach erzeugt werden und der HTML seite mit übergeben werden
    timestring = time.strftime("%H:%M:%S")  # So würde man ein time format selber definieren
    context = {'now': timestring,
               'time': time.localtime(),
               'list': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}  # der kontext wird als dict übergeben
    # um im HTML file die keys zu referenzieren

    return render(request, 'demo/index_ohneBaseVererbung.html', context)  # Mit dieser Zeile gebe ich an
    # wo die HTML seite beschrieben ist → diese wird als Antwort mit dem context
    # gerendert und zurück an den Server geschickt


def index_learning2(request):
    timestring = time.strftime("%H:%M:%S")  # So würde man ein time format selber definieren
    context = {'now': timestring,
               'time': time.localtime(),
               'list': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}  # der kontext wird als dict übergeben
    return render(request, 'demo/index_mitBaseVererbung.html', context)

def index(request):

    notices = Notice.objects.all() # Damit bekommt man eine Referenz auf die Tabelle
    context = {'notices':notices}   # Und damit kann ich die Tabelle in der HTML verwenden
    return render(request, 'demo/index.html',context)