import cv2 as cv


class Image:
    #init
    def __init__(self, path):
        self.__img = None
        self.__path = path
        self.__width = 0
        self.__height = 0
        if path is not None and path != "":
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
    def createAlpha(self):
        if not self.isDataExist():
            return
        assert self.__img is not None
        # Wert 50 ist Threshold-Wert, kann angepasst werden, 255 ist Maximalwert
        r, newImage = cv.threshold(cv.cvtColor(self.__img, cv.COLOR_BGR2GRAY), 50, 255, cv.THRESH_BINARY)
        path = "import/alpha_img_generated.png"
        cv.imwrite(path, newImage)
        return path

    def compose(self, Key_img, Alpha_img, x, y):
        if not self.isDataExist() or not Key_img.isDataExist():
            return
        assert self.__img is not None
        key = Key_img.getImage()
        alpha = Alpha_img.getImage()
        h, w = alpha.shape[:2]
        if key is None or alpha is None:
            print("FEHLER: Key- oder Alpha-Bild fehlt.")
            return None

        if key.shape[:2] != (h, w):
            print("FEHLER: Key- und Alpha-Bild haben unterschiedliche Größen.")
            return None

        bg_h, bg_w = self.__img.shape[:2]
        if x < 0 or y < 0 or x + w > bg_w or y + h > bg_h:
            print("FEHLER: Key passt nicht vollständig in den Hintergrund an der angegebenen Position.")
            return None

        out = self.__img.copy()
        patch = out[y:y+h, x:x+w]

        #Folgende 5 Zeilen mit Hilfe von ChatGPT erstellt
        mask = (alpha > 0)
        if key.ndim == 3 and mask.ndim == 2:
            mask3 = mask[..., None]
        else:
            mask3 = mask

        patch[mask3] = key[mask3]

        out[y:y+h, x:x+w] = patch
        path = "working/composed_img.png"
        cv.imwrite(path, out)
        return path
    
    #noch überarbeiten
    def save(self, filepath):
        if not self.isDataExist():
            return
        assert self.__img is not None
        cv.imwrite(filepath, self.__img)


    def resize(self, width, height):
        if not self.isDataExist():
            return
        assert self.__img is not None
        try:
            w = int(width)
            h = int(height)
        except Exception:
            print("FEHLER: width/height müssen ganze Zahlen sein.")
            return
        if w <= 0 or h <= 0:
            print("FEHLER: width und height müssen > 0 sein.")
            return
        self.__img = cv.resize(self.__img, (w, h))
        self.__width = w
        self.__height = h

    #fehlt:
    #resize
    #compose

    #setter methoden:
    def setSize(self, width, height):
        #kann das so funktionieren?
        self.__width = width
        self.__height = height  
    

    #getter methoden:
    def getSize(self):
        return self.__height, self.__width
    
    def getPath(self):
        return self.__path
    
    def getImage(self):
        return self.__img
    
    def getAllImgData(self):
        return self.__path, self.__width, self.__height
    
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