from abc import ABC, abstractmethod
import sqlite3
from datetime import datetime

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):

    def __init__(self, real_subject: RealSubject) -> None:
        self.real_subject = real_subject
        self.usersdb = sqlite3.connect("Samur/DataBase/usuarios_autorizados.db")
        self.accessdb = sqlite3.connect("Samur/DataBase/acceso.db")
    
    def request(self) -> None:
        if self.check_access():
            self.real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        pass
        
    def check_user(self, user) -> bool:
        """
        Comprueba si el usuario existe en la base de datos de usuarios autorizados
        """
        cursor = self.usersdb.cursor()
        cursor.execute("SELECT usuario FROM usuarios_autorizados WHERE usuario = ?", (user,))
        if cursor.fetchone():
            return True
        else:
            return False
        
    def log_user(self, user) -> None:
        """
        Registra el usuario que ha realizado la consulta
        """
        cursor = self.accessdb.cursor()
        cursor.execute("INSERT INTO acceso (usuario) VALUES (?)", (user,))
        self.accessdb.commit()
        self.accessdb.close()
    
    def log_change(self) -> None:
        """
        Registra si el usuario realiza cambios en los archivos
        """
        cursor = self.accessdb.cursor()
        cursor.execute("INSERT INTO acceso (cambio) VALUES (?)", (True,))
        self.accessdb.commit()
        self.accessdb.close()


    def log_time(self) -> None:
        """
        Registra la hora de la consulta
        """
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

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)