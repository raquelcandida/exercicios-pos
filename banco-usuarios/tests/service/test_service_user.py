from src.service.service_user import ServiceUser


class TestServiceUser:

# Validação do USER:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário adicionado a lista!"

        #Chamada
        resposta = service.add_user(name="Fabricio", job="Eng")
        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_existente(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário já existe!"
        service.add_user(name="Fabricio", job="Eng")

        # Chamada
        resposta=service.add_user(name="Fabricio", job = "Eng")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário removido da lista!"
        service.add_user(name="Fabricio", job = "Eng")

        # Chamada
        resposta = service.remove_user(name="Fabricio")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_não_existe(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário não existe!"
        service.add_user(name="Fabricio", job="Eng")

        # Chamada
        resposta = service.remove_user(name="Carlos")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_inválido(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido!"
        service.add_user(name="Joao", job="Eng")

        # Chamada
        resposta = service.remove_user(name=None)

        # Avaliação
        assert resposta_esperada == resposta


    def test_remove_user_inválido_name_numerico(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name = "Fabricio", job = "Eng")

        # Chamada
        resposta=service.remove_user(name = 1)

        # Avaliação
        assert resposta_esperada == resposta


    def test_remove_user_não_existe_name_vazio(self):
        # Setup
        service=ServiceUser()
        resposta_esperada = "Usuário inválido!"
        service.add_user(name="Fabricio", job="Eng")

        # Chamada
        resposta = service.remove_user(name="")

        # Avaliação
        assert resposta_esperada == resposta

    # Validação do NAME:
    def test_add_user_com_falha_name_none(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido!"

        #Chamada
        resposta = service.add_user(name= None, job="Eng")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_numerico(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido!"

        #Chamada
        resposta = service.add_user(name= 1, job="Eng")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_vazio(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido!"

        #Chamada
        resposta = service.add_user(name= "", job="Eng")

        #Avaliação
        assert resposta_esperada == resposta

    # Validação job:

    def test_add_user_com_falha_job_none(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"

        # Chamada
        resposta=service.add_user(name="Tales", job=None)

        # Avaliação
        assert resposta_esperada == resposta


    def test_add_user_com_falha_job_numerico(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"

        # Chamada
        resposta=service.add_user(name="Tales", job=123)

        # Avaliação
        assert resposta_esperada == resposta


    def test_add_user_com_falha_job_vazio(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"

        # Chamada
        resposta=service.add_user(name="Tales", job="")

        # Avaliação
        assert resposta_esperada == resposta

# Validação do update_user:
    def test_update_com_sucesso(self):
        # Setup
        service=ServiceUser()
        resposta_esperada ="Job alterado!"
        service.add_user(name="Tales", job="Eng")

        # Chamada
        resposta=service.update_user(name="Tales", job="Dev")

        # Avaliação
        assert resposta_esperada == resposta

    def test_update_com_falha_nome_none(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="Eng")

        # Chamada
        resposta=service.update_user(name=None, job="Eng")

        # Avaliação
        assert resposta_esperada == resposta


    def test_update_user_com_falha_nome_numerico(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="Eng")

        # Chamada
        resposta=service.update_user(name=123, job="Eng")

        # Avaliação
        assert resposta_esperada == resposta


    def test_update_user_com_falha_nome_vazio(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="Eng")

        # Chamada
        resposta=service.update_user(name="", job="Eng")

        # Avaliação
        assert resposta_esperada == resposta


    def test_update_user_com_falha_job_None(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta=service.update_user(name="Tales", job=None)

        # Avaliação
        assert resposta_esperada == resposta


    def test_update_user_com_falha_job_Numerico(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta=service.update_user(name="Tales", job=1)

        # Avaliação
        assert resposta_esperada == resposta


    def test_update_user_com_falha_job_vazio(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta=service.update_user(name="Tales", job="")

        # Avaliação
        assert resposta_esperada == resposta

# Validação do Get_User_By_Name:
    def test_get_user_by_name_com_sucesso(self):
        # Setup
        service=ServiceUser()
        resposta_esperada = "Eng"
        service.add_user(name="Jose", job="Eng")

        # Chamada
        resposta = service.get_user_by_name(name="Jose")

        # Avaliação
        assert resposta_esperada == resposta


    def test_get_user_by_name_usuario_nao_existe(self):
        # Setup
        service=ServiceUser()
        resposta_esperada = "Usuário não existe!"
        service.add_user(name="Jose", job="Eng")

        # Chamada
        resposta = service.get_user_by_name(name="Victor")

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_usuario_None(self):
        # Setup
        service=ServiceUser()
        resposta_esperada = "Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta = service.get_user_by_name(name=None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_usuario_Numerico(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta=service.get_user_by_name(name=1)

        # Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_usuario_vazio(self):
        # Setup
        service=ServiceUser()
        resposta_esperada="Usuário inválido!"
        service.add_user(name="Tales", job="DEV")

        # Chamada
        resposta=service.get_user_by_name(name="")

        # Avaliação
        assert resposta_esperada == resposta
