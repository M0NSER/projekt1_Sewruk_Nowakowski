from lista_2.fileManager.FileManager import *

newData="jak tic taci to tylko mint"

filemanager=FileManager("F:\RepozytoriumPycharm\projekt1_Sewruk_Nowakowski\lista_2\\testData.txt")
tekst=filemanager.readFile()
print(tekst)
filemanager.updateFile(newData)

tekst=filemanager.readFile()
print(tekst)