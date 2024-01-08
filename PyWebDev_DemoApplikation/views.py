import logging
import time
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from PyWebDev_DemoApplikation.forms import NoticeForm
from PyWebDev_DemoApplikation.models import Notice
from PyWebDev_DemoApplikation.serializers import NoticeSerializer

"""
Hier sind die View-Funktionen definiert die über die URL's angesprochen werden.
Jeder View-Funktion wir immer mindestens ein request-Objekt übergeben!
"""

"""
Logger in Python erzeugen:
-mit getLogger() initialisieren. Namen angeben um bereits existierende Logger vom Django Framework zu nutzen
-mit setLevel einstellen ab welchem Level geloggt wird. Alles darüber wird geloggt 
-mit addHandler einstellen ob in ein File oder in die Console geloggt wird.
Logger sind als Singleton ausgeführt, daher müssen sie in jeder Funktion neu geholt werden 
"""

"""
Messages sind Django context Objekte die in View-Funktionen beschrieben werden können.
Sie sind in Django bereits als Dictionary angelegt und können in den HTML dateien mit "Messages" ausgewertet werden,
ohne dass man sie manuell als context übergeben muss.
Es sind einmalige Text nachrichten die auf der Seite angezeigt werden. Sie müssen jedes mal neu erzeugt werden.
"""

# Create your views here.
def index_learning1(request):
    """
    Die einfachste Reaktion auf einen request, ist ein HttpResponse.
    Dies ist eine einfache Textantwort, die auf der Seite angezeigt wird

    :return: Es wird eine HTML-Seite generiert die nur den Text als Inhalt hat
    """
    return HttpResponse(f"Hello, world. You're at the Index of Views.")



def index_learning2(request):
    """
    Um eine eigene Seite anzuzeigen, muss eine HTML-Seite gerendert werden.
    Beim Rendern muss der auslösende request sowie der Pfad, der zum HTML Template führt angegeben werden.

    Zudem kann ein context Objekt mit übergeben werden.
    Das context-Objekt ist ein Dictionary, welches dynamisch in der View-Funktion befüllt werden kann.
    Im HTML-Template kann dann über die key's auf die Inhalte des context-Objekts zugegriffen werden

    :return: Es wird eine HTML-Seite mit Inhalten befüllt
    """

    # Aktuelle Zeit mit angabe des Formats
    timestring = time.strftime("%H:%M:%S")

    # context-Objekt befüllen
    context = {'now': timestring,
               'time': time.localtime(),
               'list': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}

    # HTML-Seite generieren, rendern und an den Client zurückliefern
    # return render(request, 'demo/index_ohneBaseVererbung.html', context)
    return render(request, 'demo/index_mitBaseVererbung.html', context)


def index(request):

    # Eine Datenbankreferenz als Objekt erzeugen
    notices = Notice.objects.all()

    # Datenbank filtern
    notices = notices.filter(pub_start__lte=timezone.now())  # wendet den gleichen filter an nur besser
    notices = notices.filter(pub_end__lte=timezone.now() + timezone.timedelta(days=3))
    # Schreibweise der DjangoDb Filter: <attribut>__[lte,gte,lt,gt,startswith,isnull] = <vergleichswert>
    # Jeder Filter fügt eine WEHRE Anweisung an das SELECT Statement, wenn die Datenbank ausgelesen wird.
    # Daher die selbstzuweisung, da jede WEHRE Anweisung an die vorherige angehängt wird

    # Alternative mit standard Python filter Funktion (Dies lädt die ganze Tabelle und filtert danach)
    # notices = filter(lambda notice: notice.pub_start <= time.timezone.now(), notices)

    # Die gefilterte Tabelle als Dictionary übergeben
    context = {'notices': notices}
    return render(request, 'demo/index.html', context)


@login_required  # Decorator von Django umhüllt die Funktion mit einer Anmeldeüberprüfung
def new_notice(request):
    """
    Mit dieser Funktion wird eine Neue Notice angelegt.
    Dazu muss bei einem GET request die Form gerendert werden, sodass der user sie befüllen kann.
    Bei einem POST request wurde die Form bereits befüllt und die Daten müssen in die Datenbank übertragen werden.

    Das request Objekt enthält die Informationen welche Art von request vom Client übergeben wurde.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    logger.info(f"Request in new notice: {request.method=} {request.path=}")

    if request.method == 'POST':
        # Django bietet für Formen einen Konstruktor an dem ein POST request übergeben wird.
        # In diesem request ist die ausgefüllte Form enthalten
        form = NoticeForm(request.POST)

        # Prüfung der Eingaben anhand der Bedingungen die in der Form Klasse definiert sind
        if form.is_valid():
            # Einen neuen Datenbankeintrag anlegen, indem man eine Klassenreferenz auf die Tabelle erzeugt
            notice = Notice()

            # Die Tabellenspalten können hier wie Klassenelemente beschrieben werden.
            # Die Felder aus der Form werden wie aus einem Dictionary ausgelesen,
            # wobei die key's die Attributs namen aus der Form Klasse sind.
            notice.notice_title = form.cleaned_data['notice_title']
            notice.notice_text = form.cleaned_data['notice_text']
            notice.pub_start = form.cleaned_data['pub_start']
            notice.pub_end = form.cleaned_data['pub_end']

            notice.id = request.user.id

            # Erst mit save() wir die Zeile tatsächlich in die Tabelle übertragen
            notice.save()

            # redirect mit dem namens Alias der in der urls.py definiert ist
            return redirect('index')

    # Wenn der request nicht POST ist, wird ein neues Formobjekt an die HTML seite edit.html übergeben
    # und dort gerendert
    context = {'form': NoticeForm()}
    return render(request, 'demo/edit.html', context)


@login_required
def delete_notice(request, delete_id=None):
    # Die URL zu dieser View-Funktion hat den zusätzlichen Parameter "delete_id".
    # Dieser muss hier genau so Bezeichnet werden und muss mit einem Default Wert parametriert werden!

    if delete_id is not None:
        try:
            # Die notice mit der entsprechenden id wird aus der Datenbank geholt
            notice = Notice.objects.get(id=delete_id)

            # Das user Objekt wird von Django geführt und ist in jedem request verfügbar
            if request.user.id == notice.id or request.user.is_staff:
                notice.delete()
                messages.success(request, 'Notice wurde erfolgreich gelöscht')
            else:
                messages.warning(request, 'Keine Berechtigung die Notice zu löschen')
        except Notice.DoesNotExist:
            # Diese Exception kommt von Django und wird von der Datenbank geworfen
            messages.warning(request, f'Die Notice mit der ID {delete_id} wurde nicht gefunden')

    return redirect('index')


@csrf_exempt  # Für REST Schnittstellen muss man diesen Decorator verwenden, da hier kein Token im Message Body enthalten ist
def notice_list(request):
    # Die Liste aller Notices kann über GET und POST request angesprochen werden
    # Bei GET müssen die Daten Serializiert werden, um sie dem Client zu schicken,
    # Bei POST kommen die Serializieren Daten vom Client und müssen deserialisiert werden

    if request.method == 'GET':
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)   # Heir wird jetzt nur die Serializer Classe
        # und die entsprechende Meta Klasse angesprochen
        return JsonResponse(serializer.data, safe=False)    # Hier wird jetzt kein HTML File übertragen sondern nur die Daten

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticeSerializer(data=data) # In der JSON Antwort sind alle Informationen enthalten die
        # der Serializer braucht um die Daten richtig zuzuordnen
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'GET or POST request required'}, status=400)


@csrf_exempt
def notice_detail(request, notice_id):
    # Die Details einer Nachricht können mit GET, PUT oder DELETE verwendet werden

    # Zuerst muss die Nachricht in der Tabelle überhaupt enthalten sein
    try:
        notice = Notice.objects.get(pk= notice_id)
    except Notice.DoesNotExist:
        return JsonResponse({'error': f'Notice {notice_id} not found'}, status=404)

    if request.method == 'GET':
        serializer = NoticeSerializer(notice) # Weil hier many nicht angegebn ist,
        # wird defaultmäßig nur die entsprechende id serialisiert
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoticeSerializer(notice, data=data) # Hier muss jetzt die notice angegeben werden um nur diese id zu updaten
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        notice.delete()
        return JsonResponse({'message': 'Notice was deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'GET or POST request required'}, status=400)
