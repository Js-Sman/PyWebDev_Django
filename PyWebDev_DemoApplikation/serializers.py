# from rest_framework import serializers
# from .models import Notice
#
# """ In dieser Datei verwenden wir die REST Schnittstelle um die Datenaus unserer Datenbank
# in ein JSON Format zu Serialisieren und zu Deserialisieren"""
#
#
# # Die Serialisierungs klasse muss von ModelSerializer erben
# class NoticeSerializer(serializers.ModelSerializer):
#     # In der inneren Meta Klasse stehen alle Datenbanken mit ihren Feldern die Serialisiert werden sollen
#     class Meta:
#         # Das erste datenfeld der Metaklasse ist immer die Datenbank die Serialisiert werden soll
#         model = Notice
#         # Als zweites Datenfeld müssen die Felder der Datenbank angegeben werden die Serialisiert werden wollen
#         fields = '__all__'
#         # Felder können als String array angegeben werden oder mit der dunder method __all__
#
#         """Anhand dieser Definierten KlassenStruktur, können die Daten in View-Funktionen
#         sehr einfach Serialisiert werden"""
