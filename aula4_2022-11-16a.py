#1o. passo: importar a biblioteca sqlite3
import sqlite3


#PASSOS 2 e 3 VIRARÃO função conectar()
def conectar():
  #2o. passo: Vamos estabelecer uma
  #conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #3o. passo: criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor


  import aula4_2022_11_16c as bd

con, cur = bd.conectar()

nome = input("Informe o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o)")

#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cur.execute(sql)
pessoa_id = cur.fetchone()[0]

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

