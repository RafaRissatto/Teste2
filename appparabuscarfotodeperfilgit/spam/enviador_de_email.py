class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Emailinvalido(f'Email não valido {remetente}')
        return remetente


class Emailinvalido(Exception):
    pass