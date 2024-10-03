# models/estoque.py
class Estoque:
    def __init__(self, db):
        self.db = db

    def registrar_estoque(self, codigo_produto, quantidade):
        #Registra o poroduto no estoque
        query = "INSERT INTO estoque(codigo_produto, quantidade) VALUES(%s, %s)"
        self.db.cursor.execute(query, (codigo_produto, quantidade))
        self.db.commit()

    def registrar_entrada(self, codigo, quantidade):
        #Registra o historico de entradas
        query = "INSERT INTO estoque_entradas(codigo_produto, quantidade, data_entrada) VALUES(%s, %s, NOW())"

        self.db.cursor.execute(query, (codigo, quantidade))
        self.db.commit()
