from faker import Faker

def generar_usuarios():
    fake = Faker()
    usuario = fake.first_name()
    return usuario

for i in range(10):
    print(generar_usuarios())