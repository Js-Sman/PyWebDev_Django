from django.db import models

"""
Für jede Datenbank wird in Django eine Classe angelegt oder Jeder Classe in den Models erzeugt eine Datenbank 
Die SQL Beschreibungen wer Datenbank werden somit von Django übernommen und können Pythontypisch beschrieben werden 
"""


# Create your models here.

class Notice(models.Model):
    # So werden wird die Datenbank angelegt
    # Wenn man jetzt migriert wird eine Tabelle angelegt mit 4 Spalten entsprechend der Python beschreibung
    # Die Tabelle heist so wie die Klasse
    notice_title = models.CharField(max_length=80)
    notice_text = models.TextField()
    pub_start = models.DateTimeField()
    pub_end = models.DateTimeField()

    # Um die Tabelle jetzt wirklich anzulegen muss eine Migration durchgeführt werden
    # Immer dann wenn sich die Python Klasse der Tabelle ändert muss eine neue Migration gemacht werden um die SQL
    # Tabelle entsprechend aktuell zu halten
