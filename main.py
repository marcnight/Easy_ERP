# main.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db.connection import DatabaseConnection
from models.produto import Produto
from models.estoque import Estoque
from models.funcionario import Funcionario
from models.fornecedor import Fornecedor
from models.venda import Venda

class ERPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ERP Simples")
        self.db = DatabaseConnection()

        self.produto = Produto(self.db)
        self.estoque = Estoque(self.db)
        self.funcionario = Funcionario(self.db)
        self.fornecedor = Fornecedor(self.db)
        self.venda = Venda(self.db)

        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="ERP Simples", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Cadastrar Produto", command=self.cadastrar_produto_form, width=20).pack(pady=5)
        tk.Button(self.root, text="Registrar Entrada no Estoque", command=self.registrar_entrada_form, width=20).pack(pady=5)
        tk.Button(self.root, text="Cadastrar Funcionário", command=self.cadastrar_funcionario_form, width=20).pack(pady=5)
        tk.Button(self.root, text="Cadastrar Fornecedor", command=self.cadastrar_fornecedor_form, width=20).pack(pady=5)
        tk.Button(self.root, text="Registrar Venda", command=self.registrar_venda_form, width=20).pack(pady=5)

        # Botões para ver dados já cadastrados
        tk.Button(self.root, text="Ver Funcionários", command=self.ver_funcionarios, width=20).pack(pady=5)
        tk.Button(self.root, text="Ver Produtos", command=self.ver_produtos, width=20).pack(pady=5)
        tk.Button(self.root, text="Ver Histórico de Entradas", command=self.ver_entradas, width=20).pack(pady=5)
        tk.Button(self.root, text="Ver Fornecedores", command=self.ver_fornecedores, width=20).pack(pady=5)
        tk.Button(self.root, text="Ver Vendas", command=self.ver_vendas, width=20).pack(pady=5)
        tk.Button(self.root, text="Ver Estoque", command=self.ver_estoque, width=20).pack(pady=5)

    # Formulários que interagem com as classes de modelo ===================================================================================
    def cadastrar_produto_form(self):
        form = tk.Toplevel(self.root)
        form.title("Cadastrar Produto")

        tk.Label(form, text="Nome do Produto").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="Código do Produto").pack()
        codigo_entry = tk.Entry(form)
        codigo_entry.pack()

        tk.Label(form, text="Preço").pack()
        preco_entry = tk.Entry(form)
        preco_entry.pack()

        """
        tk.Label(form, text="Codigo Fornecedor").pack(  )
        codigo_fornecedor_entry = tk.Entry(form)
        codigo_fornecedor_entry.pack()
        """
        tk.Label(form, text="Fornecedor").pack()
        fornecedor_combo = ttk.Combobox(form)  # Combobox para selecionar o fornecedor
        fornecedor_combo.pack()

        # Preencher o combobox com fornecedores cadastrados
        query_fornecedor = "SELECT id, nome FROM fornecedores"
        self.db.cursor.execute(query_fornecedor)
        fornecedores = self.db.cursor.fetchall()
        fornecedor_combo['values'] = [f"{fornecedor[0]} - {fornecedor[1]}" for fornecedor in fornecedores]

        def salvar_produto():
            nome = nome_entry.get()
            codigo = codigo_entry.get()
            preco = float(preco_entry.get())
            #id_fornecedor = codigo_fornecedor_entry.get()

            fornecedor_selecionado = fornecedor_combo.get()
            id_fornecedor = int(fornecedor_selecionado.split(" - ")[0])

            try:
                self.produto.cadastrar_produto(nome, codigo, preco, id_fornecedor)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(form, text="Salvar", command=salvar_produto).pack()

    def registrar_entrada_form(self):
        form = tk.Toplevel(self.root)
        form.title("Registrar Entrada no Estoque")

        tk.Label(form, text="Código do Produto").pack()
        codigo_entry = tk.Entry(form)
        codigo_entry.pack()

        tk.Label(form, text="Quantidade").pack()
        quantidade_entry = tk.Entry(form)
        quantidade_entry.pack()

        def salvar_entrada():
            codigo = codigo_entry.get()
            quantidade = int(quantidade_entry.get())
            try:
                self.estoque.registrar_estoque(codigo, quantidade)
                self.estoque.registrar_entrada(codigo, quantidade)
                messagebox.showinfo("Sucesso", "Entrada registrada com sucesso!")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(form, text="Salvar", command=salvar_entrada).pack()

    def cadastrar_funcionario_form(self):
        form = tk.Toplevel(self.root)
        form.title("Cadastrar Funcionário")

        tk.Label(form, text="Nome").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="CPF").pack()
        cpf_entry = tk.Entry(form)
        cpf_entry.pack()

        tk.Label(form, text="Cargo").pack()
        cargo_entry = tk.Entry(form)
        cargo_entry.pack()

        tk.Label(form, text="Setor").pack()
        setor_entry = tk.Entry(form)
        setor_entry.pack()

        def salvar_funcionario():
            nome = nome_entry.get()
            cargo = cargo_entry.get()
            cpf = cpf_entry.get()
            setor = setor_entry.get()

            
            try:
                self.funcionario.cadastrar_funcionario(nome, cpf, cargo, setor)
                messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(form, text="Salvar", command=salvar_funcionario).pack()

    def cadastrar_fornecedor_form(self):
        form = tk.Toplevel(self.root)
        form.title("Cadastrar Fornecedor")

        tk.Label(form, text="Nome do Fornecedor").pack()
        nome_entry = tk.Entry(form)
        nome_entry.pack()

        tk.Label(form, text="CNPJ").pack()
        cnpj_entry = tk.Entry(form)
        cnpj_entry.pack()

        tk.Label(form, text="Categoria").pack()
        categoria_entry = tk.Entry(form)
        categoria_entry.pack()

        def salvar_fornecedor():
            nome = nome_entry.get()
            cnpj = cnpj_entry.get()
            categoria = categoria_entry.get()
            try:
                self.fornecedor.cadastrar_fornecedor(nome, cnpj, categoria)
                messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(form, text="Salvar", command=salvar_fornecedor).pack()

    def registrar_venda_form(self):
        form = tk.Toplevel(self.root)
        form.title("Registrar Venda")

        tk.Label(form, text="Código do Produto").pack()
        codigo_entry = tk.Entry(form)
        codigo_entry.pack()

        tk.Label(form, text="Quantidade").pack()
        quantidade_entry = tk.Entry(form)
        quantidade_entry.pack()

        tk.Label(form, text ="Desconto").pack()
        desconto_entry = tk.Entry(form)
        desconto_entry.pack()

        def salvar_venda():
            codigo = codigo_entry.get()
            quantidade = int(quantidade_entry.get())
            desconto = float(desconto_entry.get())

            try:
                self.venda.atualizar_estoque(codigo, quantidade)
                self.venda.venda_produto(codigo, quantidade, desconto)

                messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        tk.Button(form, text="Salvar", command=salvar_venda).pack()

    # Adicionar as funções de visualização ===================================================================================
    def ver_funcionarios(self):
        form = tk.Toplevel(self.root)
        form.title("Funcionários Cadastrados")

        tree = ttk.Treeview(form, columns=("Nome", "CPF", "Cargo", "Setor"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("CPF", text="CPF")
        tree.heading("Cargo", text="Cargo")
        tree.heading("Setor", text="Setor")
        tree.pack(fill=tk.BOTH, expand=True)

        query = "SELECT  nome, cpf, cargo, setor  FROM funcionarios"
        try:
            self.db.cursor.execute(query)
            rows = self.db.cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar funcionários: {str(e)}")
                
    def ver_produtos(self):
         form = tk.Toplevel(self.root)
         form.title("Produtos Cadastrados")

         tree = ttk.Treeview(form, columns=("Código", "Nome", "Preço"), show='headings')
         tree.heading("Código", text="Código")
         tree.heading("Nome", text="Nome")
         tree.heading("Preço", text="Preço")
         tree.pack(fill=tk.BOTH, expand=True)

         query = "SELECT codigo, nome, preco FROM produtos"
         try:
           self.db.cursor.execute(query)
           rows = self.db.cursor.fetchall()
           for row in rows:
                tree.insert("", tk.END, values=row)
         except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar produtos: {str(e)}")

    def ver_entradas(self):
        form = tk.Toplevel(self.root)
        form.title("Histórico de Entradas")

        tree = ttk.Treeview(form, columns=("Produto", "Quantidade", "Data"), show='headings')
        tree.heading("Produto", text="Produto")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Data", text="Data")
        tree.pack(fill=tk.BOTH, expand=True)

        query = "SELECT produto, quantidade, data_entrada FROM estoque_entradas"
        try:
            self.db.cursor.execute(query)
            rows = self.db.cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            print('Erro de execução ')

    def ver_fornecedores(self):
            form = tk.Toplevel(self.root)
            form.title("Fornecedores Cadastrados")

            tree = ttk.Treeview(form, columns=("ID", "Nome", "Cnpj"), show='headings')
            tree.heading("ID", text="Codigo Fornecedor")
            tree.heading("Nome", text="Nome")
            tree.heading("Cnpj", text="CNPJ")
            tree.pack(fill=tk.BOTH, expand=True)

            query = "SELECT id, nome, cnpj FROM fornecedores"
            try:
                self.db.cursor.execute(query)
                rows = self.db.cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)
            except Exception as e:
              messagebox.showerror("Erro", f"Erro ao buscar fornecedores: {str(e)}")

    def ver_vendas(self):
                form = tk.Toplevel(self.root)
                form.title("Histórico de Vendas")

                tree = ttk.Treeview(form, columns=("Produto", "Quantidade", "Data", "Valor_Venda", "Valor_Unitario", "Desconto"), show='headings')
                tree.heading("Produto", text="Produto")
                tree.heading("Quantidade", text="Quantidade")
                tree.heading("Data", text="Data")
                tree.heading("Valor_Venda", text="Valor da Venda")
                tree.heading("Valor_Unitario", text="Valor Unitario")
                tree.heading("Desconto", text="Desconto")

                tree.pack(fill=tk.BOTH, expand=True)

                query = """
                SELECT p.nome, v.quantidade, v.data_venda, v.valor_venda, v.valor_unitario, v.desconto
                FROM vendas v 
                JOIN produtos_estoque p ON v.codigo_produto = p.codigo
                """
                try:
                    self.db.cursor.execute(query)
                    rows = self.db.cursor.fetchall()
                    for row in rows:
                      tree.insert("", tk.END, values=row)
                except Exception as e:
                  messagebox.showerror("Erro", f"Erro ao buscar vendas: {str(e)}")

    def ver_estoque(self):
        form = tk.Toplevel(self.root)
        form.title("Estoque de Produtos")

        tree = ttk.Treeview(form, columns=("Produto", "Codigo", "Quantidade", "Fornecedor"), show='headings')
        tree.heading("Produto", text="Produto")
        tree.heading("Codigo", text="Codigo")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Fornecedor", text="Fornecedor")

        tree.pack(fill=tk.BOTH, expand=True)
        
        query = """
                SELECT p.nome, e.codigo_produto, e.quantidade, f.nome  
                FROM estoque e 
                JOIN 
                produtos p on p.codigo = e.codigo_produto
                JOIN 
                fornecedores f on p.id_fornecedor = f.id 
                """
        try:
            self.db.cursor.execute(query)
            rows = self.db.cursor.fetchall()
            for row in rows:
                    tree.insert("", tk.END, values=row)
        except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar estoque: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ERPApp(root)
    root.mainloop()