import cv2 as cv


class Image:
    def __init__(self, path):
        if path:
            self.load(path)
        else:
            self.__path = path
            self.__width = 0
            self.__height = 0

    def load(self, path):
        self.__img = cv.imread(path)
        if self.__img is None:
            self.__width = 0
            self.__height = 0
        else:
            h, w = self.__img.shape[:2]
            self.__height = h
            self.__width = w

    #fehlt:
    #save
    #create alpha
    #resize
    #display
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
    
    def __str__(self):
        return f"ImageObject(path={self.__path}, width={self.__width}, height={self.__height})"

    #andere methoden:
    def isDataExist(self):
        if self.__img is None:
            print(f"FEHLER: Das Bild '{self.__path}' konnte nicht geladen werden. Bitte überprüfe die Datei.")
            return False
        return True