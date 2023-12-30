import logging
import time
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from PyWebDev_DemoApplikation.models import Notice
from PyWebDev_DemoApplikation.forms import NoticeForm



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
    # logger = logging.getLogger("django.db.backends")  # Dieser Logger ist von Django und kann hier so geholt und
    # # ausgewertet werden
    # logger.setLevel(logging.DEBUG)  # Die Backend sachen werden im Debugglevel geschrieben
    # logger.addHandler(logging.StreamHandler())

    notices = Notice.objects.all()  # Damit bekommt man eine Referenz auf die Tabelle

    # Man kann die Datenbank mit filtern auslesen
    ###notices = filter(lambda notice: notice.pub_start <= time.timezone.now(), notices)
    # Dies ist jedoch eher schlecht, weil es die ganze Tabelle lädt und dann filtert

    # SQL bietet performantere Filteroptionen an
    notices = notices.filter(pub_start__lte=timezone.now())  # wendet den gleichen filter an nur besser
    notices = notices.filter(pub_end__gte=timezone.now())
    # Schreibweise der DjangoDb Filter: <attribut>__[lte,gte,lt,gt,startswith,isnull] = <vergleichswert>

    # ACHTUNG!!
    # Alle Filter werden hier zu einer WHERE Bedingung zusammengebaut-> daher auch immer die selbstzuweiseung
    # Erst bei nutzung in der VIEW werden die Daten geladen

    context = {'notices': notices}  # Und damit kann ich die Tabelle in der HTML verwenden
    return render(request, 'demo/index.html', context)


@login_required  # Mit deime Decorator von Django wird die Funktion in eine anmeldeüberprüfung gewrapped
def new_notice(request):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    logger.info(f"Request in new notice: {request.method=} {request.path=}")
    if request.method == 'POST':
        form = NoticeForm(request.POST)

        # logger.info(f"Request in new notice: {request.method=} {request.path=} {form.is_valid()=}")

        if form.is_valid():
            notice = Notice()

            notice.notice_title = form.cleaned_data['notice_title']
            notice.notice_text = form.cleaned_data['notice_text']
            notice.pub_start = form.cleaned_data['pub_start']
            notice.pub_end = form.cleaned_data['pub_end']

            notice.id = request.user.id

            notice.save()

            return redirect('index')  # Für das redirecten werden auch die names aliase verwendet
            # die in den urls angegeben sind

    context = {'form': NoticeForm()}
    return render(request, 'demo/edit.html', context)


@login_required
def delete_notice(request, delete_id=None):
    # Hier kommt die id zusammen mit dem request an
    # Die id kommt aus der view weil dort in der href die id der aktuellen notice_id zugewiesen wurde
    # Im Url wurde die id als parameter mit übergeben -> der übergabeparameter muss genauso heisen wie in der URL !!

    if delete_id is not None:
        try:
            # Die notice mit der entsprechenden id wird aus der Datenbank tabelle gelöscht
            notice = Notice.objects.get(id=delete_id)
           # print(f"{request.user.id} {notice.id}")
            if request.user.id == notice.id or request.user.is_staff:   # Das user Object ist auch in den views schon verfügbar
                notice.delete()
                messages.success(request, 'Notice wurde erfolgreich gelöscht')
            else:
                messages.warning(request, 'Keine Berechtigung die Notice zu löschen')
        except Notice.DoesNotExist:
            # Diese Exception kommt von Django und wird geschmissen, wenn die Anfrage auf die Tabelle ins leere geht
            messages.warning(request, f'Die Notice mit der ID {delete_id} wurde nicht gefunden')
            # messages werden in view-funktionen generiert und zum request hinzugefügt
            # dadurch stehen sie in der html datei als message objekt im context zur verfügung
            # ohne, dass man sie extra übergeben muss

    return redirect('index')
