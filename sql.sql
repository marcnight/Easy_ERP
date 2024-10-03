-- Tabela para Fornecedores
CREATE TABLE fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    categoria VARCHAR(50)
);

-- Tabela para Produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    id_fornecedor INT NOT NULL REFERENCES fornecedores(id),
    categoria varchar(50)
);

-- Tabela para Funcionários
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    cargo VARCHAR(50),
    setor varchar(50)
);

--Tabela para o Estoque
CREATE TABLE estoque (
    id SERIAL PRIMARY KEY,
    codigo_produto varchar(50) REFERENCES produtos(codigo),
    quantidade INT DEFAULT 0
);
-- Tabela para Entrada de Estoque (Histórico de Entradas)
CREATE TABLE estoque_entradas (
    id SERIAL PRIMARY KEY,
    codigo_produto VARCHAR(50) REFERENCES produtos(codigo),
    quantidade INT NOT NULL,
    data_entrada TIMESTAMP
);

-- Tabela para Vendas (Saída de Estoque)
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    codigo_produto VARCHAR(50) REFERENCES produtos(codigo),
    quantidade INT NOT NULL,
    data_venda TIMESTAMP NOT NULL,
    valor_venda FLOAT,
    valor_unitario FLOAT,
    desconto FLOAT
);
