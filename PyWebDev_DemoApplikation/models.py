from django.db import models

"""
Für jede Datenbank muss in Django eine Classe angelegt werden.
Die Spalten der Datenbank werden als Klassenattribute beschrieben und von Django in SQL Statements übersetzt.
Name der Classe ist Name der Datenbank.

Mit dem Befehlt "manage.py makemigrations" wird aus jeder Klasse eine Datei generiert die eine SQL Datenbank erzeugt
Diese Datei wird im Ordner "migrations" dokumentiert.
Mit dem Befehl "manage.py migrate" wird die Datenbank tatsächlich angelegt.

Immer dann, wenn sich im Model einer Datenbank etwas ändert, muss zuerst eine Migration durchgeführt werden 
um die Änderungen auf die Tabelle zu übertragen.
"""


# Create your models here.
class Notice(models.Model):

    notice_title = models.CharField(max_length=80)
    notice_text = models.TextField()
    pub_start = models.DateTimeField()
    pub_end = models.DateTimeField()

