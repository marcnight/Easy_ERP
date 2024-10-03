# models/fornecedor.py
class Fornecedor:
    def __init__(self, db):
        self.db = db

    def cadastrar_fornecedor(self, nome, cnpj, categoria):
        query = "INSERT INTO fornecedores (nome, cnpj, categoria) VALUES (%s, %s, %s)"
        self.db.cursor.execute(query, (nome, cnpj, categoria))
        self.db.commit()
