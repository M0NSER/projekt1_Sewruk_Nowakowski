class FileManager:
    fileName = ""
    data = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def readFile(self):
        uchwyt = open(self.fileName, 'r', encoding='utf-8')
        self.data = uchwyt.read()
        uchwyt.close()
        return self.data

    def updateFile(self, textData):
        uchwyt = open(self.fileName, 'a',encoding='utf-8')
        uchwyt.writelines(textData)
        uchwyt.close()
