from appparabuscarfotodeperfilgit.spam.enviador_de_email import Emailinvalido, Enviador
import pytest


def teste_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['rafaelrissatto9il.com', 'fffbargmail.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(Emailinvalido):
        enviador.enviar(
            remetente,
            'vkmoveis@gmail.com',
            'Testando o email com python',
            'Esse email foi criado por Rafael para teste'
            )
