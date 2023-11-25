from abc import ABC, abstractmethod

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
    
    def request(self) -> None:
        if self.check_access():
            self.real_subject.request()
            self.log_access()
            
    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")

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