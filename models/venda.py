# models/venda.py
class Venda:
    def __init__(self, db):
        self.db = db

    def atualizar_estoque(self, codigo_produto, quantidade):
        query= "UPDATE estoque SET quantidade = quantidade - %s WHERE codigo_produto = %s"
        #query = """
        #INSERT INTO vendas (codigo_produto, quantidade, data_venda)
        #VALUES (%s, %s, CURRENT_DATE)
        #"""
        
        self.db.cursor.execute(query, (quantidade, codigo_produto))
        #self.db.cursor.execute(query, (codigo_produto, quantidade))
        #self.db.cursor.execute()
        self.db.commit()

    def venda_produto(self, codigo_produto, quantidade, desconto):
        """query = "INSERT INTO vendas (codigo_produto, quantidade, data_venda) VALUES (%s, %s, CURRENT_DATE)"

        self.db.cursor.execute(query, (codigo_produto, quantidade))
        #self.db.cursor.execute()
        self.db.commit
        """
        #Calcular o valor total da venda
        #Selecionando valor no banco
        query_preco = "SELECT preco FROM produtos WHERE codigo = %s "
        self.db.cursor.execute(query_preco, (codigo_produto,))#arrumar se necessario
        result = self.db.cursor.fetchone()

        if result:
            valor_unitario = float(result[0])

            valor_venda = (valor_unitario * quantidade) - desconto

         
        try:
            # Insere os dados da venda na tabela 'vendas'
            query_insert_venda = "INSERT INTO vendas (codigo_produto, quantidade, valor_unitario, desconto, valor_venda, data_venda) VALUES (%s, %s, %s, %s, %s, NOW())"
            self.db.cursor.execute(query_insert_venda, (codigo_produto, quantidade, valor_unitario, desconto, valor_venda))
            self.db.commit()

            #print("Venda registrada com sucesso no banco de dados.")  # Para ver no console
        except Exception as e:
            #print(f"Erro ao registrar venda: {e}")
            raise