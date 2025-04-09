import mysql.connector
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

def criar_conexao():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def criar_manifestacao(tipo, descricao):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)", (tipo, descricao))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_manifestacoes():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM manifestacoes")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def listar_por_tipo(tipo):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE tipo = %s", (tipo,))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def buscar_por_id(id_manifestacao):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE id = %s", (id_manifestacao,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def contar_manifestacoes():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM manifestacoes")
    resultado = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return resultado

def remover_manifestacao(id_manifestacao):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM manifestacoes WHERE id = %s", (id_manifestacao,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas_afetadas > 0
