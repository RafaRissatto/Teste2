from appparabuscarfotodeperfilgit.spam.enviador_de_email import Enviador


def teste_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    enviador.enviar(
        'rafaelrissatto9@gmail.com',
        'vkmoveis@gmail.com',
        'Testando o email com python',
        'Esse email foi criado por Rafael para teste'
        )
