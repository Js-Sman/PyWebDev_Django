import logging
from unittest import case

############## Aufgabe "Hello World" #################

# var = print("Hello World")
# print(var)

############## Aufgabe "Variablen Scope" #################
#
# def read_variablen():
#     # Innerhalb einer Funktion definierte Variablen
#     # sind auch nur innerhalb der Funktion verfügbar zum lesen und schreiben
#
#     # auf Globale Variablen kann innerhalb von Funktionen immer lesen zugegriffen werden
#
#     lokale_variable = 1
#     print(f'Innerhalb der Funktion "read_variablen": {lokale_variable=}')
#     print(f'Innerhalb der Funktion "read_variablen": {globale_variable=}')
#
#
# def write_variablen():
#     # Um Globale Variablen innerhalb einer Funktion auch zu beschreiben, muss dies explizit angegeben werden
#     global globale_variable
#
#     globale_variable = 3
#     print(f'Innerhalb der Funktion "write_variablen": {globale_variable=}')
#
#
#
# # Alle Variablen die auf der 1. Tab ebene oder nicht innerhalb einer Funktion definiert wurden, sind global
# globale_variable = 2
# read_variablen()
# print(f"Im global Scope: {globale_variable=}")
# write_variablen()
# print(f"Im global Scope: {globale_variable=}")
#
# print(lokale_variable)  # Diese Variable ist nicht innerhalb vom global Scope definiert
# # und somit nicht verfügbar für lese oder schreib operationen

############## Aufgabe "Match-Case & If-Comprehension" #################
#
# a = 1
# b = 2
# command = "gleich"
# result = ""
#
# # Syntax von in Py für Switch -> match <>: \t case <>:
# match command:
#     case "kleiner":
#         # If-Comprehension -> "Dieser Wert" if (Boolsche-OP) else "Dieser Wert"
#         result = a if a < b else b
#     case "grosser":
#         result = a if a > b else b
#
# print(result)

############## Aufgabe "Lists & List-Comprehension" #################
#
# list1 = []  # Init empty list
#
# for i in range(10):
#     list1.append(i)  # Fills list with ints from 0 to 9
#
# print(list1)
# print(f"list1[0]: {list1[0]}")  # Index referencing
# print(f"list1[-1]: {list1[-1]}")  # backwarts index referencing
#
# list1[4] = "NewValue"  # Resigning -> Typ Kontainer ist egal
# print(list1[4])
# print(list1[:])  # List slicing -> von anfang bis ende
#
# list1.remove("NewValue")  # remove operates on the list
# print(list1)
#
# list2 = list1[1:3]  # List splicing -> Inhalte von Index 1 bis 3 ausgeschlossen zuweisen
# print(list2)
# print(list1)  # slicing gibt nur entsprechende werte zurück -> verändert die liste nicht
#
# list1.reverse()  # reverse operates on the list
# print(list1)
#
# list3 = list1.copy()  # Wichtig!!! nur so wird eine neue Liste mit selben inhalt erzeugt -> mit list3 = list1
# # entstehen 2 refs auf dieselbe liste
# list3 = list3[1:3]
# print(list3)
#
# list4 = list2 + list3  # Listen mit + aneinanderhängen
# print(list4)
#
# list4.insert(2, "NewValue")  # NewValue at Index 2
# print(list4)
#
# list4.remove(list4.index("NewValue"))  # Vorsicht!! remove sucht immer den Wert in einer Liste -> Hier wird der Wert
# # 2 gelöscht weil NewValue anm Index 2 steht
# print(list4)
#
# for i in list4:
#     print(i)  # listen iterieren über die inhalte nicht über den index
#
# if "NewValue" in list4:  # mit "in" können inhalten von Listen abgefragt werden
#     print(f"Index of 'NewValue': {list4.index('NewValue')}")
#
# # Built in Functions for lists
# print(min(list1))
# print(max(list1))
#
# ## List Comprehension
#
# listComp = [(i, x ** 2) for i, x in enumerate(list1) if i % 2 == 0]
# print(f"listComp: {listComp}")
#
# listSing = []
# for i, x in enumerate(list1):  # mit enumerate() wird jedes iterable object aufgeteilt in index, value
#     if i % 2 == 0:
#         listSing.append((i, x ** 2))
#
# print(f"listSing: {listSing}")

############## Aufgabe "Dicts" #################

# dict1 = {}
# # Dictionarys konnen nicht "appended" werden
# # Zum befüllen müssen einfach key value paare angegeben werden
# # Keys and Values können beliebige Objekte sein
# dict1["key1"] = "value1"
# dict1["key2"] = 2
# dict1[3] = "value3"
# print(dict1)
#
# print(dict1["key1"]) # wenn man den Key referenziert, bekommt man das Value
#
# print(list(dict1.values()))   # Alle Values
# print(dict1.keys()) # Alle Keys
# print(dict1.items())    # Tupel aller items
#
# for element in dict1:
#     # Das Iteriert über alle elemente -> die elemente sind definiert durch die keys
#     # so werden nur die key ausgegeben
#     print(element)
#     print(dict1[element]) # so könnte man auch hier auf die values kommen
#
# for element in dict1.values():
#     # So referenziert man nur die values
#     print(element)
#
# for element in dict1.items():
#     # So iteriert man über die tupel key value paare
#     print(element)
#     print(element[0])
#     print(element[1])
#
# for key,value in dict1.items():
#     # Und so sind key und value von vornherein aufgetrennt -> best practice
#     print(key,value)

############## Aufgabe "SQLite Kommandozeilenbefehle" #################

# # Tabelle erzeugen
# sqlite> CREATE TABLE Student
#    ...> (name TEXT,matrikel INTREGER, schnitt REAL);
#
# # Werte Einfügen
# sqlite> INSERT INTO Student
#    ...> (name, matrikel, schnitt)
#    ...> VALUES
#    ...> ("Jens", 100, 2,3),
#    ...> ("Grae", 101, 1,0),
#    ...> ("Dude", 101, 1,0);
#
# # Alles ausgeben
# sqlite> SELECT *
#    ...> FROM Student;
#
# # nur name von "bedingung" ausgeben
# sqlite> SELECT name
#    ...> FROM Student
#    ...> WHERE matrikel = 100;
#
# # Durchschnitt alle Studenten schnitte mit nummer über 100
# sqlite> SELECT AVG(schnitt)
#    ...> FROM Student
#    ...> WHERE matrikel > 100;
#
# # Alle Matrikelnummern *10
# sqlite> UPDATE Student
#    ...> SET matrikel = matrikel*10;
#
# # Nur den Schnitt von matrikelnummer 1020 anpassen
# sqlite> UPDATE Student
#    ...> SET schnitt = schnitt -0.1
#    ...> WHERE matrikel = 1020;
#
# # Zeile mit bedingung löschen
# sqlite> DELETE FROM Student
#    ...> WHERE matrikel = 1000;

############## Aufgabe "Klassen -> Vererbung" #################
#
# class A():
#     def name(self):
#         return "A"
#
#     def printInfo(self):
#         print(self.name())
#
#     def __add__(self, other):
#         # Mit den dunder methods kann inbuild verhalten überschrieben werden
#         return self.name() + other.name()
#
# class B(A):
#     def name(self):
#         # Mit dem Schlüsselwort Super werden explizit die Methoden der Elternklasse ausgeführt
#         return super().name() + "B"
#
#
# b = B()
# a = A()
# print(b.name())
# print(b.printInfo())    # Weil B von A erbt kann B auf die in a definierte print info methode aufrufen
# # Achtung die Funktion printet schon und der Rückgabewert der Funktion ist none -> es entstehen 2 ausgaben
# print(b + a)    # Das funktioniert nur weil die add methode in A überschrieben wurde

############## Aufgabe "Mapping, Filtering & Lambda" #################

# # Funktionen können auch übergabeparameter sein
# def say_hello():
#     print("Hello")
#
#
# def do_three_times(func):
#     for i in range(3):
#         func()
#
#
# do_three_times(say_hello)
#
# # Maps
# list1 = ["1","2","3"]   # Liste aus stings
# map_object = map(int, list1)
#
# print(map_object)   # Das MapObject ist ein iterator kein träger der werte
#
# for i in map_object:    # Beim mapping wird die Funktion auf alle teile der Liste angewendet und einmalig im iterator
#     # gespeichert
#     print(i)    # Das sind jetzt Integer werte -> jeder String in list1 wurde auf INT gecastet
#
# print(list1)    # DIe liste bleibt durch das mapping unverändert
# list2 = list(map_object)    #So kann der Iterator in eine Liste umgewandelt werden
# print(list2)    # ACHTUN!! Der Iterrator kann nur einmal gelesen werden-> danach ist er wieder leer
#
# map_object = map(int, list1)
# list3 = list(map_object)
# print(list3)    # Hier kommt jetzt tatsächlich eine Liste auf integern an
#
# # Filter
# # Filter sind ähnlich wie maps nur dass die Funktion selbst beschrieben ist
#
# def filterfunc(item):
#     # Eine Filter funktion muss immer bool zurückliefern
#     # Anhand dessen wird die Liste gefiltert -> Werte die im Filter true ergeben werden übernommen
#     return (item % 2 == 0)
#
# list4 = [1,2,3,4,5,6,7,8,9]
# filtered_list = filter(filterfunc, list4)   # Aufg alle elemente der list4 wird die filterfunc angewendet
# # Wenn true zurück kommt wird der Wert in die filtered liste übernommen
# print(filtered_list)    #ACHTING!! hzier kommt auch erstmal nur ein einmaliger iterator zurück wie bei einer map
#
# list5 = list(filtered_list) # die Iteratoren zu einer Liste machen
# print(list5)
#
# # Lambda
# # Lambda Funktionen sind einfach inline funktionen die nicht auserhalb dieser zeile aufrufbar sind
# # Mit ihnen können Filter realisiert werden weil man dann keine extra deklarierte funktion für den filter braucht
# # Man kann lambdafunktionen allerdings einer variable zuweisen
#
# lambdafunc = lambda item: item % 2 == 0
# filtered_list_lambda = filter(lambdafunc, list4)   # Hier passiert jetzt das gleiche wie oben mit der filterfunc
# print(filtered_list_lambda) #auch hier nur Iterator
# list6 = list(filtered_list_lambda)
# print(list6)
#
# filtered_list_lambda_compact = list(filter(lambda item: item % 3 == 0, list4))  # So kann man jetzt mit inline lambda
# #sehr schnell in einer zeile eine neue liste erzeugen die gefiltert ist
# print(filtered_list_lambda_compact)


############## Aufgabe "Logging" #################
#
# # Ein logger wird niemals mit "new" initialisiert sondern immer mit "getLogger" aus der bib gezogen
# logger = logging.getLogger("TestLogger")
#
# logger.addHandler(logging.StreamHandler()) # So wird der Log in die Console geschrieben
# logger.addHandler(logging.FileHandler("test.log", encoding="UTF-8", mode="w")) # Sor der Log in einem File mitgheschrieben
# # mode: a für Anhängen und w für immer wieder neu
#
# # Die Verschiedenen LEVEL
# logger.debug('Dies ist die erste Debug-Nachricht')
# logger.info('Dies ist die erste  Info-Nachricht')
# logger.warning('Dies ist die erste  Warning-Nachricht')
# logger.error('Dies ist die erste  Error-Nachricht')
# logger.critical('Dies ist die erste  Critical-Nachricht')
# # Default LEVERL ist warning -> dh alles ab waring wird ausgegeben bze im file gespreichert
#
# # um das LEVEl anzupassen
# logger.setLevel(logging.DEBUG)  #Ab jetzt wird alles geloggt
# logger.debug('Dies ist die zweite  Debug-Nachricht')
# logger.info('Dies ist die zweite  ne Info-Nachricht')
# logger.warning('Dies ist die zweite  Warning-Nachricht')
# logger.error('Dies ist die zweite  Error-Nachricht')
# logger.critical('Dies die zweite Critical-Nachricht')
#
# logger.setLevel(logging.CRITICAL)   # ab jetzt werden nurnoch criticals geloggt
# logger.debug('Dies ist die dritte  Debug-Nachricht')
# logger.info('Dies ist die dritte  ne Info-Nachricht')
# logger.warning('Dies ist die dritte  Warning-Nachricht')
# logger.error('Dies ist die dritte  Error-Nachricht')
# logger.critical('Dies die dritte Critical-Nachricht')
#
#
# # Da ein logger immer ein Singelton ist kannn das loglevel zentral im programmeinstieg angepasser werden


############## Aufgabe "Exceptions" #################
#
# # Basic Exception
# loop = True
# while loop:
#     try:
#         # Hier stehen die Sachen bei denen etwas Schiefgehen kann
#         zeahler = int(input("Enter a number: "))
#         nenner = int(input("Enter a number: "))
#         print(zeahler / nenner)
#         loop = False
#
#     except ValueError as ve:
#         print(ve)
#         print("Please enter a number")
#
#     except Exception as e:
#         # So wird einfach jede Ecxeption die auftauchen kann gefangen und im e objekt gespeichert
#         print(e.__class__)
#         print(e)  # das e object printet immer die exception message
#
#     except ZeroDivisionError as zde:
#         print(zde)
#         print("Please")
#
#     # Die Exceptions werden der Reihe nach gefangen -> der ZeroDiv Fehler wird schon vorher
#     # von der basis Exception abgehandelt und kommt hier garnicht erst an
#
#     finally:
#         print("Goodbye") # Alles, was im Finally block steht, wird auf jedenfall
#         # ausgeführt, egal welchen Pfad das programm vorher geht
#
#
# # Custom Exeptions
#
# # Man kann auch eigene Exeptions definieren indem man eine Classe erzeugt die von Exceptions erbt
# class MyException(Exception):
#     def __init__(self):
#         # Um die Exception Message zu definieren muss sie dem super ctor übergeben werden
#         self.message = "Dies ist eine custom Exception"
#         super().__init__(self.message)
#
# loop = True
# while loop:
#     name = input("Enter your Name: ")
#
#     try:
#         if name == "Me":
#             raise MyException()  # Eine custom Exception wird mit raise geworfen
#         # Man kann auch definieren, was genau die custom Exception wirft aber das ist jetzt out of scope
#         else:
#             loop = False
#     except MyException as e:
#         print("My Exception wurde gefangen")
#         print(e)
#
#     finally:
#         # Achtung!!! Das hier passiert immer, auch wenn try erfolgreich ist
#         print(f"Die eingabe lautet: {name}")


############## Aufgabe "Decorators" #################
#
# def sayHello():
#     print("Hello")
#
# def decorator(func):
#     def wrapper():
#         print("+++")
#         func()
#         print("***")
#
#     return wrapper
#
# @decorator
# def sayHello2():
#     print("Hello2")
#
#
#
#
# sayHello()  # Einfache ausführung einer funktion
#
# newHello = decorator(sayHello)  # Funktionen können wie variablen übergeben und zugewiesen werden
#
# newHello()  # die neue funktion ist dekoriert
#
# sayHello2() # Diese Funktion ist mit dem decorator tag versehen -> das wrapped die funktion automatisch
#
# # Mit einem Decorator Tag wird eine Methode in eine andere Methode eingebettet
# # -> diese fügt zusätzliche Funktionalitäten hinzu ohne die Methode zu verändern


############## Aufgabe "JSON" #################
# Das JSON Datenformat is wie ein Dictionary zu verstehen
# Es wird zur standartisierten Serialisierung von Daten Objekten genutzt

import json

# von python zu JSON
data = {} # Dictonary
data['name'] = '<NAME>' # Für JSNO werden die meisten dinge als String dargestellt
data['phone'] = '10123456789'
data['age'] = 42    # Int und Float werden zu einem allgemeinem Numer format
data['hobbies'] = ['<NAME>', '<NAME>', '<NAME>', '<NAME>']  # Listen oder Tupel werden zu arrays
data_as_json = json.dumps(data, indent=3) # Ein Python Dict kann mit jason.dump umgewandelt werden
print(data_as_json)

# JSON dateien sind sehr einfach zu Serialisieren weil sie standartisiert sind und nur auf strings basieren
# Für WebDev ist JSON daher beliebt für die Kommunikation zwischen Server und Client

# Von JSON zu Python
# Um einen Block als JSON zu definieren muss er in """ Anführungszeichen stehen
json_data = json.loads(data_as_json)
print(json_data)
