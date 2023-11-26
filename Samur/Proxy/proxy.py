from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):

    def request(self) -> None:
        print("Accediendo a archivos clasificados...")

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject, user: str) -> None:
        self.real_subject = real_subject
        self.user = user
        self.usersdb = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
        self.accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
    
    def request(self) -> None:
        if self.check_user():
            print("Acceso permitido...")
            self.real_subject.request()
            self.log_user()
            self.log_change()
            self.log_time()
        
    def check_user(self) -> bool:
        """
        Comprueba si el usuario existe en la base de datos de usuarios autorizados
        """
        try:
            self.usersdb
            cursor = self.usersdb.cursor()
            cursor.execute("SELECT usuario FROM usuarios_autorizados WHERE usuario = ?", (self.user,))
            if cursor.fetchone():
                return True
            else:
                return False
        finally:
            self.usersdb.commit()
            self.usersdb.close()
        
    def log_user(self) -> None:
        """
        Registra el usuario que ha realizado la consulta
        """
        self.accessdb
        cursor = self.accessdb.cursor()
        cursor.execute("INSERT INTO acceso (usuario) VALUES (?)", (self.user,))
        self.accessdb.commit()
        self.accessdb.close()
    
    def log_change(self) -> None:
        """
        Registra si el usuario realiza cambios en los archivos
        """
        self.accessdb
        cursor = self.accessdb.cursor()
        cursor.execute("INSERT INTO acceso (cambio) VALUES (?)", (0,))
        self.accessdb.commit()
        self.accessdb.close()


    def log_time(self) -> None:
        """
        Registra la hora de la consulta
        """
        self.accessdb
        cursor = self.accessdb.cursor()
        now = datetime.now()

        cursor.execute("INSERT INTO acceso (hora) VALUES (?)", (now,))
        self.accessdb.commit()
        self.accessdb.close()

def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    subject.request()

