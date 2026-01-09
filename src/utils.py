import os

def getFilename():
    while True:
        answer = input("Eingabe: ")
        if not answer.lower().endswith(".png"):
            answer += ".png"
        path = os.path.join("import", answer)

        if os.path.isfile(path):
            return answer
        else:
            print(f"ACHTUNG: Datei '{answer}' wurde nicht gefunden!")
            print("Bitte stelle sicher, dass die Datei im Ordner 'import' liegt und überprüfe deine Schreibweise.\n")

def getFilpath(filename, folder):
    return os.path.join(folder, filename)