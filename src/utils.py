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
    print("3. komibiniertes Bild")
    while True:
        choice = input("Eingabe (1 oder 2 oder 3): ")
        if choice == "1":
            return "Image_background"
        elif choice == "2":
            return "Image_key"
        elif choice == "3":
            return "Image_composed"
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2 oder 3.")