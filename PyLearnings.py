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
