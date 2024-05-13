from appparabuscarfotodeperfilgit.spam.enviador_de_email import Enviador
import pytest


def teste_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['rafaelrissatto9@gmail.com', 'fffbar@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'vkmoveis@gmail.com',
        'Testando o email com python',
        'Esse email foi criado por Rafael para teste'
        )
    assert remetente in resultado
