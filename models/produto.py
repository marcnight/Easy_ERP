# models/produto.py
class Produto:
    def __init__(self, db):
        self.db = db

    def cadastrar_produto(self, nome, codigo, preco, id_fornecedor):
        query = "INSERT INTO produtos (nome, codigo, preco, id_fornecedor) VALUES (%s, %s, %s, %s)"
        
        self.db.cursor.execute(query, (nome, codigo, preco, id_fornecedor))
        self.db.commit()

    