import os

def getFilename():
    while True:
        answer = input("Eingabe: ")
        path = os.path.join("import", answer)

        if os.path.isfile(path):
            return answer
        else:
            print(f"ACHTUNG: Datei '{answer}' wurde nicht gefunden!")
            print("Bitte stelle sicher, dass die Datei im Ordner 'import' liegt und überprüfe deine Schreibweise.\n")

def getFilpath(filename, folder):
    return os.path.join(folder, filename)

def whichImage():
    print("Welches Bild möchtest du auswählen?")
    print("1. Hintergrundbild")
    print("2. Keybild")
    print("3. Kombiniertes Bild")
    while True:
        choice = input("Eingabe (1 oder 2 oder 3): ")
        if choice == "1":
            return "Image_background"
        elif choice == "2":
            return "Image_key"
        elif choice == "3":
            return "Image_composed"
        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")

def deleteFile(path):
    if os.path.exists(path):
        try:
            os.remove(path)
        except Exception as e:
            print(f"Fehler beim Löschen der Datei {path}: {e}")
        if not os.path.exists(path):
            return 1
        else:
            print("Die Datei konnte nicht gelöscht werden. Bitte prüfe Berechtigungen oder ob die Datei geöffnet ist.")
            return 0
    else:
        print(f"Datei nicht gefunden: {path}")
        return 0