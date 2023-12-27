from django import forms
import datetime

"""
In Django werden Formulare genau wie die Datenbanken auch über Klassen beschrieben 
Diese Klassen Erzeugen die Form Ähnlich wie die Klassen in der moddels datei die Tabellen erzeugt
Auserdem wird hier auch die verarbeitung der Formulare beschrieben 
"""


class NoticeForm(forms.Form):
    # Beschreibung des Formulars
    date_formats = ['%d.%m.%Y %H:%M:%S', '%d.%m.%y %H:%M:%S']
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
