############## Aufgabe "Match-Case & If-Comprehension" #################
#
# a = 1
# b = 2
# command = "gleich"
# result = ""
#
# # Match-Case
# match command:
#     case "kleiner":
#         # If-Comprehension
#         result = a if a < b else b
#
#     case "grosser":
#         result = a if a > b else b
#
#     case default:
#         # Default wert, falls keiner der Cases ein Match ist
#         result = "Kein Case wurde gematched"
#
# print(result)


############## Aufgabe "Lists & List-Comprehension" #################
#
# # Liste initialisieren und befüllen
# list1 = []
# for i in range(10):
#     # Füllt die Liste von 0 bis 9
#     list1.append(i)
#
# # Listenelemente vorwärts oder rückwärts über Index ausgeben
# print(list1)
# print(f"list1[0]: {list1[0]}")
# print(f"list1[-1]: {list1[-1]}")
#
# # Listenelemente überschreiben
# list1[4] = "NewValue"  # Bestehender Wert wird verändert
# print(list1)
#
# # Listenelemente an Index einfügen
# list1.insert(4, "NewValue")  # Neuer Wert wird eingefügt
# print(list1)
#
# # Listenelemente löschen
# list1.remove("NewValue")  # Nur das erste vorkommen von "NewValue" wird gelöscht
# print(list1)
# list1.remove("NewValue")
#
# # Listen slicing
# print(list1[:])  # Von anfang bis Ende
# print(list1[1:3])  # Von Index 1 bis Index 3 ausgeschlossen
# list2 = list1[1:3]  # Slices zuweisen
# print(list2)
# print(list1)  # Slicing verändert die Liste nicht
#
# # Inbuilt Funktionen von Listen
# list1.reverse()  # permanentes Umkehren der Reihenfolge einer Liste
# print(list1)
# list1.sort()  # permanentes Sortieren der Listenelemente, per Default Aufsteigend
# print(list1)
# list3 = list1.copy()  # Neue Liste mit selbem Inhalt erzeugen (list3 = list1 erzeugt eine Referenz auf dieselbe Liste)
# print(list3)
# # Minimum & Maximum der Listenelemente
# print(min(list1))
# print(max(list1))
# # Kisten aneinanderhängen
# list4 = list2 + list3
# print(list4)
#
# # Über Listenelemente iterieren
# for i in list4:
#     print(i)
#
# # Listen auf Inhalte prüfen
# if "NewValue" in list4:
#     print(f"Index of 'NewValue': {list4.index('NewValue')}")
#
# # List Comprehension
# """
# -Liste erzeugen []
# -Funktion was mit den elementen passieren soll
# -for...Elemente ist ein Liste
# -in...Liste der Elemente (Mit enumerate Index, Value erhalten)
# -Bedingung wann ein Element an die Funktion übergeben wird
# Die Zuweisung der erfolgt an eine neue Liste
# """
# listComp = [(i, x ** 2) for i, x in enumerate(list1) if i % 2 == 0]
# print(f"listComp: {listComp}")

