from django import forms
import datetime

"""
In Django werden Formulare genau wie die Datenbanken auch über Klassen beschrieben 
Diese Klassen Erzeugen die Form Ähnlich wie die Klassen in der moddels datei die Tabellen erzeugt
Auserdem wird hier auch die verarbeitung der Formulare beschrieben 
"""


class NoticeForm(forms.Form):
    # Beschreibung des Formulars
    # date_formats = ['%d.%m.%Y %hh:%mm:%ss']
    notice_title = forms.CharField(label='Title', max_length=100)
    notice_text = forms.CharField(label='Text', max_length=400)
    pub_start = forms.DateTimeField(label='Von',
                                    initial=datetime.datetime.today())
    pub_end = forms.DateTimeField(label='Bis',
                                  initial=datetime.datetime.today())


