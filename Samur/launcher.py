from Composite.Carpeta import Carpeta
from Composite.Documentos import Documentos
from Composite.Links import Links
from Proxy.proxy import *
from auxiliar import generar_usuarios
import time

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

    #Creamos nombres de usuario aleatorios en la base de datos
    generar_usuarios(20)

    #Pedimos el usuario para iniciar sesion
    usuario = input("Introduce tu nombre de usuario: ")
    
    #Creamos el proxy
    real_subject = RealSubject()
    proxy = Proxy(real_subject, usuario)
    if proxy.request() == True:
        time.sleep(0.5)
        print("Accediendo a los archivos...")
        time.sleep(2)

        print("Quieres eliminar algun archivo? (s/n)")
        respuesta = input()
        if respuesta == "s":
            carpeta1.remove(link1)
            print("Archivo eliminado")
            proxy.log_change(1)
        else:
            print("No se ha eliminado ningun archivo")
            proxy.log_change(0)
                
        print(carpeta1.operation())
        print("\n")
        print(carpeta2.operation())
    else:
        print("Acceso denegado...")
        time.sleep(2)
        print("Saliendo del programa...")



    




