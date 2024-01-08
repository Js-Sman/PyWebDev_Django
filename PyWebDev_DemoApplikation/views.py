from django.shortcuts import render
from django.http import HttpResponse

"""
Hier sind die View-Funktionen definiert die über die URL's angesprochen werden.
Jeder View-Funktion wir immer mindestens ein request-Objekt übergeben!
"""


# Create your views here.
def index_learning(request):
    """
    Die einfachste Reaktion auf einen request, ist ein HttpResponse.
    Dies ist eine einfache Textantwort, die auf der Seite angezeigt wird

    :return: Es wird eine HTML-Seite generiert die nur den Text als Inhalt hat
    """
    return HttpResponse(f"Hello, world. You're at the Index of Views.")
