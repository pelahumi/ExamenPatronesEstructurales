from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):

    def request(self) -> None:
        print("Has pasado el proxy...")

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject, user: str) -> None:
        self.real_subject = real_subject
        self.user = user
        self.usersdb = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
        self.accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
    
    
    def request(self) -> bool:
        if self.check_user():
            self.real_subject.request()
            self.log_user()
            self.log_time()
            return True
        else:
            return False

        
    def check_user(self) -> bool:
        """
        Comprueba si el usuario existe en la base de datos de usuarios autorizados
        """
        try:
            usersdb = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
            cursor = usersdb.cursor()
            cursor.execute("SELECT usuario FROM usuarios_autorizados WHERE usuario = ?", (self.user,))
            if cursor.fetchone():
                return True
            else:
                return False
        finally:
            usersdb.commit()
            usersdb.close()

        
    def log_user(self) -> None:
        """
        Registra el usuario que ha realizado la consulta
        """
        accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
        cursor = accessdb.cursor()
        cursor.execute("INSERT INTO acceso (usuario) VALUES (?)", (self.user,))
        accessdb.commit()
        accessdb.close()

    
    def log_change(self, modificacion: int) -> None:
        """
        Registra si el usuario realiza cambios en los archivos
        """
        accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
        cursor = accessdb.cursor()
        cursor.execute("UPDATE acceso SET modificacion = ?", (modificacion,))
        accessdb.commit()
        accessdb.close()


    def log_time(self) -> None:
        """
        Registra la hora de la consulta
        """
        accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
        cursor = accessdb.cursor()
        now = datetime.now()

        cursor.execute("UPDATE acceso SET hora_modificacion = ?", (now,))
        accessdb.commit()
        accessdb.close()




