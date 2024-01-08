from django import forms
import datetime

"""
In Django werden Formulare genau wie die Datenbanken auch über Klassen beschrieben. 
Diese Klassen Erzeugen die Form Ähnlich wie die Klassen in der models datei die Tabellen erzeugen.

Die Attributs namen sind zwar unabhängig von den Attributs namen der Tabelle, jedoch 
sollten sie leserlich zuweisbar sein.

Formen haben Felder mit verschiedenen Eingabemöglichkeiten. 
Diese müssen zwingend mit den Feldtypen der Datenbank übereinstimmen oder konvertierbar sein.
"""


class NoticeForm(forms.Form):
    # Festlegen der zulässigen Formate für ein eingegebenes Datum
    date_formats = ['%d.%m.%Y %H:%M:%S', '%d.%m.%y %H:%M:%S']

    # Beschreibung der Felder des Formulars.
    # Anhand dieser Beschreibung kann Django die Eingaben validieren
    notice_title = forms.CharField(label='Title',
                                   max_length=100,
                                   initial='Notice Title')
    notice_text = forms.CharField(label='Text',
                                  max_length=400,
                                  initial='Notice')
    pub_start = forms.DateTimeField(label='Von',
                                    input_formats=date_formats,
                                    initial=datetime.datetime.now())
    pub_end = forms.DateTimeField(label='Bis',
                                  input_formats=date_formats,
                                  initial=datetime.datetime.now() + datetime.timedelta(days=3))
