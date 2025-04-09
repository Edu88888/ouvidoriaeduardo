# 🗣️ Sistema de Ouvidoria - Luiz Eduardo

Projeto simples de um **Sistema de Ouvidoria** em **Python**, utilizando **MySQL** como banco de dados.  
O objetivo é registrar, listar, pesquisar e remover manifestações do tipo **reclamação**, **elogio** ou **sugestão**.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- **MySQL**
- **mysql-connector-python**
- **python-dotenv**

---

## 📁 Estrutura do Projeto


---

## 🔧 Configuração do Banco de Dados

1. Crie o banco no MySQL:

```sql
CREATE DATABASE ouvidoria;

USE ouvidoria;

CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    descricao TEXT
);

Crie um arquivo chamado .env na raiz do projeto com este conteúdo (substitua com seus dados reais):

DB_HOST=localhost
DB_NAME=ouvidoria
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

✅ Esse arquivo serve para manter os dados de acesso do banco separados do código, de forma segura e prática.

No terminal, instale as bibliotecas necessárias com:

pip install mysql-connector-python python-dotenv

Com tudo configurado, execute:

python ouvidoria.py

📋 Funcionalidades Disponíveis
Criar uma nova manifestação

Listar todas as manifestações

Listar por tipo (reclamação, sugestão, elogio)

Buscar por código

Exibir total de manifestações

Remover manifestação por código

💬 Exemplo do Menu

Ouvidoria Eduardo
1 - Listar Todas as Manifestações
2 - Listar Manifestações por Tipo
3 - Criar Nova Manifestação
4 - Exibir Quantidade de Manifestações
5 - Pesquisar Manifestação por Código
6 - Excluir Manifestação pelo Código
7 - Sair

👨‍💻 Desenvolvedor
Luiz Eduardo – 19 anos
Projeto feito para fins de estudo com integração entre Python e MySQL.
