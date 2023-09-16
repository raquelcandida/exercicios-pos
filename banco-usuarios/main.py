from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user(name= "Fabricio", job= "DEV")
print(resposta)

resposta = service.add_user(name= "Tales", job= "Eng")
print(resposta)

resposta = service.add_user(name= "Tales", job= "Eng")
print(resposta)

resposta = service.remove_user(name= "Tales")
print(resposta)

resposta = service.add_user(name= 1, job= "Eng")
print(resposta)

resposta = service.add_user(name= "Maria", job= 1)
print(resposta)

print("parte 2 .....")

resposta = service.add_user(name= "Jose", job= "Tester")
print(resposta)

resposta = service.add_user(name= "Jose", job= "Dev")
print(resposta)

resposta = service.add_user(name= "Jose", job= "Dev")
print(resposta)

print("parte 3 .....")

resposta = service.get_user_by_name(name= 14)
print(resposta)
