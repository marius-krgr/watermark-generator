import os


def fileImport(filename, folder):
    filepath = os.path.join(folder, filename)

def welcome():
    print("Moin! Ich bin Watermarky, dein persönlicher Bildbearbeitungs- und Wassermarkierungs-Ersteller-Assistent :)")

def queryInput():
    print("Bitte lege deine Bilddateien im Ordner 'Import' ab.")
    input("Um weiterzugehen, drücke Enter.")

    while True:
        answer = input("Wie heißt die Datei, die du verwenden möchtest?\nEingabe: ")
        if not answer.lower().endswith(".png"):
            answer += ".png"
        path = os.path.join("Import", answer)

        if os.path.isfile(path):
            return answer
        else:
            print("ACHTUNG: Datei '{answer}' wurde nicht gefunden!")
            print("Bitte stelle sicher, dass die Datei im Ordner 'Import' liegt und überprüfe deine Schreibweise.\n")

def main():
    # begrüße
    # vorbereitung
    # userinterface
    welcome()
    filename=queryInput()
    fileImport(filename, "/Import")


    print("Hello, World!")
    
if __name__ == "__main__":
    main()