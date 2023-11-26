from Composite.Carpeta import Carpeta
from Composite.Documentos import Documentos
from Composite.Links import Links
from Proxy.proxy import *

def launcher():
    #Creamos los documentos 
    doc1 = Documentos("doc1", "pdf", 1.3)
    doc2 = Documentos("doc2", "txt", 0.5)
    doc3 = Documentos("doc3", "csv", 0.8)

    link1 = Links("link1")
    link2 = Links("link2")

    carpeta1 = Carpeta("carpeta1")
    carpeta2 = Carpeta("carpeta2")

    #Añadimos los documentos a las carpetas
    carpeta1.add(doc1)
    carpeta1.add(link1)
    carpeta1.add(link2)

    carpeta2.add(doc2)
    carpeta2.add(doc3)
    



