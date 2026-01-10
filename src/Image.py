import cv2 as cv


class Image:
    #init
    def __init__(self, path):
        self.__img = None
        self.__path = path
        self.__width = 0
        self.__height = 0
        if path:
            self.load(path)

    def load(self, path):
        self.__img = cv.imread(path)
        if self.__img is None:
            self.__width = 0
            self.__height = 0
        else:
            h, w = self.__img.shape[:2]
            self.__height = h
            self.__width = w

    def display(self):
        if not self.isDataExist():
            return
        win = f"Bildvorschau: {self.__path or ''}"
        assert self.__img is not None
        cv.imshow(win, self.__img)
        print("Image angezeigt. Zum schließen eines Bildfensters, drücke eine beliebige Taste im Bildfenster.")
        #Bug fix mit Hilfe von ChatGPT (nächste 6 Zeilen)
        while True:
            key = cv.waitKey(10)
            if key != -1:
                break
        cv.destroyWindow(win)
        cv.waitKey(1)

    #bearbeitende Methoden:

    #fehlt:
    #save
    #create alpha
    #resize
    #compose

    #setter methoden:
    def setSize(self, width, height):
        #kann das so funktionieren?
        self.__width = width
        self.__height = height  
    

    #getter methoden:
    def getSize(self):
        return self.__width, self.__height
    
    def getPath(self):
        return self.__path
    
    def getImage(self):
        return self.__img
    
    def getAllImgData(self):
        return f"Image(path={self.__path}, width={self.__width}, height={self.__height})"
    
    def __str__(self):
        return f"Image(path={self.__path}, width={self.__width}, height={self.__height})"

    #andere methoden:
    def isDataExist(self):
        if self.__img is None:
            print(f"FEHLER: Das Bild '{self.__path}' konnte nicht geladen werden. Bitte überprüfe die Datei.")
            return False
        return True
    
    def destroyallwindows(self):
        cv.destroyAllWindows()