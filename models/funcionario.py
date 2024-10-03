# models/funcionario.py
class Funcionario:
    def __init__(self, db):
        self.db = db

    def cadastrar_funcionario(self, nome, cpf, cargo, setor):
        query = "INSERT INTO funcionarios (nome, cpf, cargo, setor) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(query, (nome, cpf, cargo, setor))
        self.db.commit()

    def ver_funcionario(self, nome, cpf, cargo, setor):
        query = "SELECT nome, cpf, cargo, setor from funcionarios"
        try:
            self.db.cursor.execute(query)
            rows = self.db.cursor.fetchall()
            #for row in rows:
                #tree.insert("", tk.END, values=row)
        except Exception as e:
            #messagebox.showerror("Erro", f"Erro ao buscar funcionários: {str(e)}")
            print("Erro")
            