import time

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # Mit einfachen "HttpResponse" kann man z.b Text zurück geben
    # Wenn man jedoch eine Seite in HTML zurück liefer möchte muss diese gerendert werden.

    # Diese Funktion wird ganz normal abgearbeitet, wenn sie Aufgerufen wird
    # dynamische Inhalte können hier demnach ganz einfach erzeugt werden und der HTML seite mit übergeben werden
    timestring = time.strftime("%H:%M:%S") # So würde man ein time format selber definieren
    context = {'now': timestring,
               'time': time.localtime()}   # der kontext wird als dict übergeben
    # um im HTML file die keys zu referenzieren


    return render(request, 'demo/index.html', context)   # Mit dieser Zeile gebe ich an
    # wo die HTML seite beschrieben ist → diese wird als Antwort mit dem context
    # gerendert und zurück an den Server geschickt
