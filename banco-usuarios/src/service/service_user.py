from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def find_user(self, name):
        if name != None and str == type(name):
            for item_user in self.store.bd:
                if item_user.name == name:
                    return item_user
        return None

    def add_user(self, name, job):
        if name != None and str == type(name) and name!="" and job != None and str == type(job) and job != "":
            user = self.find_user(name)
            if user != None:
                return "Usuário já existe!"
            else:
                user = User(name, job)
                self.store.bd.append(user)
                return "Usuário adicionado a lista!"
        else:
            return "Usuário inválido!"

    def remove_user(self, name):
        if name != None and str == type(name) and name != "":
            user=self.find_user(name)
            if user == None:
                return "Usuário não existe!"
            else:
                self.store.bd.remove(user)
                return "Usuário removido da lista!"
        else:
            return "Usuário inválido!"

    def update_user(self, name, job):
        if name != None and str == type(name) and name != "" and job != None and str == type(job) and job != "":
            user=self.find_user(name)
            if user == None:
                return "Usuário não existe!"
            else:
                user.job = job
                return "Job alterado!"
        else:
            return "Usuário inválido!"

    def get_user_by_name(self, name):
        if name != None and str == type(name) and name != "":
            user=self.find_user(name)
            if user == None:
                return "Usuário não existe!"
            else:
                return user.job
        else:
            return "Usuário inválido!"