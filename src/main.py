from src.Image import Image
import src.utils as utils

def welcome():
    print("Moin! Ich bin Watermarky, dein persönlicher Bildbearbeitungs- und Wassermarkierungs-Ersteller-Assistent! :)")
    print("Bitte lege deine Bilddateien im Ordner 'import' ab.")
    print("Ich werde dich durch den Prozess führen.")
    input("Um weiterzugehen, drücke Enter.")

def getImageFilepaths():
    # Hintergrundbild abfragen
    print("Wie heißt die Bilddatei die du als Hintergrund verwenden möchtest?")
    filename_background = utils.getFilename()
    filepath_background = utils.getFilpath(filename_background, "import")
    #Keybild abfragen
    print("Wie heißt die Bilddatei die du als Keybild verwenden möchtest?") 
    filename_key = utils.getFilename()
    filepath_key = utils.getFilpath(filename_key, "import") 
    return filepath_background, filepath_key

def checkImagesLoaded(image_background, image_key):
    if not image_background.isDataExist():
        print("Das Hintergrundbild konnte nicht geladen werden. Bitte überprüfe die Datei und starte das Programm erneut.")
        exit()
    elif not image_key.isDataExist():
        print("Das Keybild konnte nicht geladen werden. Bitte überprüfe die Datei und starte das Programm erneut.")
        exit()
    else:
        print("Bilder wurden erfolgreich geladen!")

def userInterface():
    print("User-Interface - Home")
    print("Was möchtest du tun? Aktionen:")
    print("1. Bild anzeigen")
    print("2. Bildinformationen anzeigen")
    print("3. Bildgröße ändern")
    print("")
    print("4. Wassermarke hinzufügen")
    print("5. Wassermarke positionieren")
    print("6. Wassermarke skalieren")
    print("7. Wassermarke entfernen")
    print("")
    print("8. Bild exportieren")
    print("9. Programm beenden")
    print("")
    print("Um eine Aktion auszuwählen, gib die entsprechende Zahl ein:")
    action = input("Eingabe: ")
    if action == "1":
        print("Aktion 1 ausgewählt: Bild anzeigen")
        #methode fehlt noch
    elif action == "2":
        print("Aktion 2 ausgewählt: Bildinformationen anzeigen")
        #methode fehlt noch
    elif action == "3":
        print("Aktion 3 ausgewählt: Bildgröße ändern")
        #methode fehlt noch
    elif action == "4":
        print("Aktion 4 ausgewählt: Wassermarke hinzufügen")
        #methode fehlt noch
    elif action == "5":
        print("Aktion 5 ausgewählt: Wassermarke positionieren")
        #methode fehlt noch
    elif action == "6":
        print("Aktion 6 ausgewählt: Wassermarke skalieren")
        #methode fehlt noch
    elif action == "7":
        print("Aktion 7 ausgewählt: Wassermarke entfernen")
        #methode fehlt noch
    elif action == "8":
        print("Aktion 8 ausgewählt: Bild exportieren")
        #methode fehlt noch
    elif action == "9":
        print("Programm wird beendet. Auf Wiedersehen!")
        exit()
    else:
        print("Ungültige Eingabe. Bitte versuche es erneut.")
    #Rückkehr zum User-Interface
    userInterface()


def main():
    # begrüßung
    welcome()
    #Filepaths der Bilder abfragen
    filepath_background, filepath_key = getImageFilepaths()
    # Objekt erstellen
    Image_background = Image(filepath_background)
    Image_key = Image(filepath_key)
    # Überprüfe ob Bilder geladen wurden
    checkImagesLoaded(Image_background, Image_key)
    # User-Interface aufrufen
    userInterface()



    
if __name__ == "__main__":
    main()