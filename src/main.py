import os
from Image import Image
import utils

def welcome():
    print("Moin! Ich bin Watermarky, dein persönlicher Bildbearbeitungs- und Wassermarkierungs-Ersteller-Assistent! :)")
    print("Bitte lege deine Bilddateien im Ordner 'import' ab.")
    print("Ich werde dich durch den Prozess führen.")
    input("Um weiterzugehen, drücke Enter.")

def getImageFilepaths():
    # Hintergrundbild abfragen
    print("Wie heißt die Bilddatei die du als Hintergrund verwenden möchtest? (mit Endung angeben, bitte. Z.B. '.jpg' oder '.png')")
    filename_background = utils.getFilename()
    filepath_background = utils.getFilpath(filename_background, "import")
    #Keybild abfragen
    print("Wie heißt die Bilddatei die du als Keybild verwenden möchtest?") 
    filename_key = utils.getFilename()
    filepath_key = utils.getFilpath(filename_key, "import") 
    #Filepath kombiniertes Bild festlegen
    filepath_composed = "working/composed_img.png"
    return filepath_background, filepath_key, filepath_composed


def checkImagesLoaded(image_background, image_key):
    if not image_background.isDataExist():
        print("Das Hintergrundbild konnte nicht geladen werden. Bitte überprüfe die Datei und starte das Programm erneut.")
        exit()
    elif not image_key.isDataExist():
        print("Das Keybild konnte nicht geladen werden. Bitte überprüfe die Datei und starte das Programm erneut.")
        exit()
    else:
        print("Bilder wurden erfolgreich geladen!")

def userInterface(Image_background, Image_key, Image_alpha, Image_composed, pos_x, pos_y):
    print("User-Interface - Home")
    print("Was möchtest du tun? Aktionen:")
    print("1. Bild anzeigen")
    print("2. Bildinformationen anzeigen")
    print("3. Bildgröße ändern")
    print("")
    print("4. Wassermarke generieren")
    print("5. Wassermarke positionieren")
    print("6. Wassermarke skalieren")
    print("7. Wassermarke entfernen")
    print("")
    print("8. Bild exportieren")
    print("")
    print("10. Programm beenden")
    print("")
    print("Um eine Aktion auszuwählen, gib die entsprechende Zahl ein:")
    while True:
        action = input("Eingabe: ")
        if action == "1":
            print("Aktion 1 ausgewählt: Bild anzeigen")
            image = utils.whichImage()
            if image == "Image_background":
                Image_background.display()
            elif image == "Image_key":
                Image_key.display()
            elif image == "Image_composed":
                if Image_composed.getImage() is None:
                    print("FEHLER: Es ist noch kein kombiniertes Bild vorhanden, du musst zuerst eine Wassermarke generieren")
                    input("Drücke Enter, um fortzufahren...")
                else:
                    Image_composed.display()
            break
        elif action == "2":
            print("Aktion 2 ausgewählt: Bildinformationen anzeigen")
            image = utils.whichImage()
            if image == "Image_background":
                path, width, height = Image_background.getAllImgData()
            elif image == "Image_key":
                path, width, height = Image_key.getAllImgData()
            elif image == "Image_composed":
                    if Image_composed.getImage() is None:
                        print("FEHLER: Es ist noch kein kombiniertes Bild vorhanden, du musst zuerst eine Wassermarke erstellen")
                        input("Drücke Enter, um fortzufahren...")
                        break
                    else:
                        path, width, height = Image_composed.getAllImgData()
                        if width == 0:
                            print("es ist noch kein kombiniertes Bild vorhanden")
                            input("Drücke Enter, um fortzufahren...")
                            break

            print("Pfad:", path)
            print("Breite:", width)
            print("Höhe:", height)
            input("Drücke Enter, um fortzufahren...")
            break
        elif action == "3":
            print("Aktion 3 ausgewählt: Bildgröße ändern")
            image = utils.whichImage()
            if image == "Image_composed":
                if Image_composed.getImage() is None:
                        print("FEHLER: Es ist noch kein kombiniertes Bild vorhanden, du musst zuerst eine Wassermarke erstellen")
                        input("Drücke Enter, um fortzufahren...")
                        break
            w = input("Gib die neue Breite in Pixel ein: ")
            h = input("Gib die neue Höhe in Pixel ein: ")
            if image == "Image_background":
                Image_background.resize(w, h)
            elif image == "Image_key":
                Image_key.resize(w, h)
            elif image == "Image_composed":
                Image_composed.resize(w, h)
            input("Drücke Enter, um fortzufahren...")
            break
        elif action == "4":
            print("Aktion 4 ausgewählt: Wassermarke generieren")
            path = Image_key.createAlpha()
            Image_alpha = Image(path)
            if Image_alpha is None:
                print("Es scheint ein Fehler aufgetreten zu sein. Bitte versuche es erneut.")
                break
            input("Key erfolgreich erstellt. Drücke Enter, um fortzufahren...")
            filepath_composed = Image_background.compose(Image_key, Image_alpha, 0, 0)
            Image_composed = Image(filepath_composed)
            input("Wassermarke erfolgreich gesetzt. Drücke Enter, um das kombinierte Bild anzuzeigen")
            Image_composed.display()
            break
        elif action == "5":
            print("Aktion 5 ausgewählt: Wassermarke positionieren")
            if Image_alpha is None:
                print("FEHLER: Du musst erst eine Wassermarke generieren.")
                break
            print("Hier siehst du die Breite und Höhe deines Hintergrundbildes:")
            print(Image_background.getAllImgData())
            #Fehler abfangen, wenn User keine ganze Zahl eingibt
            pos_x = input("Gib die horizontale Position deines Wasserzeichens in Pixel ein (ganze Zahlen):")
            pos_y = input("Gib die vertikale Position deines Wasserzeichens in Pixel ein (ganze Zahlen):")
            pos_x = int(pos_x)
            pos_y = int(pos_y)
            filepath_composed = Image_background.compose(Image_key, Image_alpha, pos_x, pos_y)
            if filepath_composed is None:
                break
            Image_composed = Image(filepath_composed)
            input("Neue Position festgelegt. Drücke Enter um das Bild anzuzeigen")
            Image_composed.display()
            input("Drücke Enter, um fortzufahren...")
            break
        elif action == "6":
            print("Aktion 6 ausgewählt: Wassermarke skalieren")
            if Image_alpha is None:
                print("FEHLER: Du musst erst eine Wassermarke generieren.")
                break
            factor = input("Mit welchem Faktor möchtest du das Wasserzeichen skalieren: ")
            factor = float(factor)
            key_h, key_w = Image_key.getSize()
            new_w = int(key_w * factor)
            new_h = int(key_h * factor)
            Image_key.resize(new_w, new_h)
            Image_alpha.resize(new_w, new_h)
            if Image_alpha is None:
                break
            filepath_composed = Image_background.compose(Image_key, Image_alpha, pos_x, pos_y)
            print(f"Wasserzeichen skaliert auf {new_w} x {new_h} Pixel.")
            Image_composed = Image(filepath_composed)
            Image_composed.display()
            input("Drücke Enter, um fortzufahren...")
            break
        elif action == "7":
            print("Aktion 7 ausgewählt: Wassermarke entfernen")
            confirm = input("Bist du sicher, dass du die Wassermarke entfernen möchtest? (j/n): ").lower()
            if confirm in ("j", "y"):
                    path = os.path.join("working", "composed_img.png")
                    deleted = utils.deleteFile(path)
                    if deleted: 
                        Image_composed = None
                        print("Wassermarke wurde entfernt.")
                    else :
                        break
            else:
                print("Aktion abgebrochen. Keine Änderungen vorgenommen.")
                break
            input("Drücke Enter, um fortzufahren...")

        elif action == "8":
            print("Aktion 8 ausgewählt: Bild exportieren")
            #Action 8 mithilfe von Chat erstellt
            if Image_composed is None:
                print("FEHLER: Es gibt kein Bild zum Exportieren.")
                break
            filename = input("Wie soll die exportierte Datei heißen? (z.B. mein_bild.png): ")
            export_path = os.path.join("export", filename)
            Image_composed.save(export_path)
            print(f"Bild wurde erfolgreich exportiert nach: {export_path}")
            input("Drücke Enter, um fortzufahren...")
            break
        elif action == "10":
            print("Programm wird beendet. Auf Wiedersehen!")
            path = os.path.join("working", "composed_img.png")
            utils.deleteFile(path)
            exit()
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")
    #Rückkehr zum User-Interface
    userInterface(Image_background, Image_key, Image_alpha, Image_composed, pos_x, pos_y)


def main():
    # begrüßung
    welcome()
    #Filepaths der Bilder abfragen
    filepath_background, filepath_key, filepath_composed = getImageFilepaths()
    # Objekt erstellen
    Image_background = Image(filepath_background)
    Image_key = Image(filepath_key)
    Image_alpha = None
    Image_composed = Image(filepath_composed)
    #Positionsvariablen erstellen
    pos_x = 0
    pos_y = 0
    # Überprüfe ob Bilder geladen wurden
    checkImagesLoaded(Image_background, Image_key)
    # User-Interface aufrufen
    userInterface(Image_background, Image_key, Image_alpha, Image_composed, pos_x, pos_y)
    
if __name__ == "__main__":
    main()