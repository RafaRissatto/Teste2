from appparabuscarfotodeperfilgit.spam.enviador_de_email import Enviador


def teste_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None