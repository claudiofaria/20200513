from banco import bd

class Mensagem:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

    @staticmethod
    def recupera_todas():
        sql = '''select usuario, texto from mensagens order by id desc'''
        cur = bd().execute(sql)
        mensagens = []
        for usuario, texto in cur.fetchall():
            mensagem = Mensagem(usuario, texto)
            mensagens.append(mensagem)
        return mensagens

    def gravar_mensagem(self):
        sql = '''insert into mensagens (usuario, texto) values (?, ?)'''
        primeiro_interrogacao = self.usuario
        segundo_interrogacao = self.texto
        bd().execute(sql, [primeiro_interrogacao, segundo_interrogacao])
        bd().commit()
