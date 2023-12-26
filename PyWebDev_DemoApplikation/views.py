import logging
import time

from django.shortcuts import render, redirect
from django.utils import timezone
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
    # Dies ist jedoch eher schlecht weil es die ganze Tabelle lädt und dann filtert
    # SQL bietet performantere Filteroptionen an
    # notices = notices.filter(pub_start__lte=timezone.now())  # wendet dengleichen filter an nur besser
    # notices = notices.filter(pub_end__gte=timezone.now())
    # Schreibweise der DjangoDb Filter: <attribut>__[lte,gte,lt,gt,startswith,isnull] = <vergleichswert>

    #ACHTUNG!!
    #Alle Filter werden hier zu einer WHERE Bedingung zusammengebaut-> daher auch immer die selbstzuweiseung
    #Erst bei nutzung in der VIEW werden die Daten geladen


    context = {'notices': notices}  # Und damit kann ich die Tabelle in der HTML verwenden
    return render(request, 'demo/index.html', context)


def new_notice(request):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        logger.info(f'POST REQUEST!!!!: {form.is_valid()}')

        if form.is_valid():
            notice = Notice()
            notice.notice_title = form.cleaned_data['notice_title']
            notice.notice_text = form.cleaned_data['notice_text']
            notice.pub_start = form.cleaned_data['pub_start']
            notice.pub_end = form.cleaned_data['pub_end']
            notice.save()
            return redirect('index')

    context = {'form': NoticeForm()}
    return render(request, 'demo/edit.html', context)

