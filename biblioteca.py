# -*- coding: utf-8 -*-
#importando modulo de conexão com o banco mysql
import pymysql
#setando as configurações do banco
servidor ="localhost"
usuario ="root"
senha =""
banco ="biblioteca"
# Fazando a conexão com o banco de dados
pymysql.install_as_MySQLdb()
db = pymysql.connect(servidor, usuario, senha, banco)
cursor = db.cursor()
#Função para executar os comandos sql
def executa_sql(pSQL):
        try:
                cursor.execute(pSQL)
                db.commit()
        except:
                print("ERRO: Não foi possivél executar o comando SQL.")
                db.rollback()
#Função para ultilizar o Select
def buscar_sql(pSQL):
        try:
                cursor.execute(pSQL)
                results = cursor.fetchall()
                return results
        except:
                print("Erro: Não foi possível buscar os dados.")
                return 0

#Função para adicionar um novo livro 
def adicionar():

        Titulo = raw_input("Titulo: ")
        Autor = raw_input("Autor: ")
        Editora = raw_input("Editora: ")
        Categoria = raw_input("Categoria: ")

        executa_sql("INSERT INTO livro(titulo_livro, categoria_livro, autor_livro, editora_livro) VALUES('%s', '%s', '%s', '%s')" %(Titulo, Categoria, Autor, Editora))

#Função para Visualizar todos os livros cadastrados 
def visualizar():
	vResultado = buscar_sql("SELECT * FROM livro")
	
	print("+----------------------------------------------------------------------------------------------+")
	print("| Id  | Titulo                 | Autor                |Editora              |Categoria         |")
	print("+----------------------------------------------------------------------------------------------+")	
	for Row in vResultado:
		vId = Row[0]
		vTitulo = Row[1]
		vCategoria = Row[2]
		vAutor = Row[3]
		vEditora = Row[4]

		print("| %i" %vId +" | "+ vTitulo+ " | " + vAutor+ "  | "+ vEditora+" | "+vCategoria+" |")
		print("+----------------------------------------------------------------------------------------------+") 

#Função excluir		
def excluir():
	num_id = raw_input("\nId do livro que você deseja excluir: ")
	executa_sql("DELETE FROM livro WHERE id_livro = '%s'" %num_id)

#Função para atualizar dados do livro
def atualizar(): 
	num_id = raw_input("\nId do livro que deseja atualizar: ")
	vResultado = buscar_sql("SELECT * FROM livro WHERE id_livro ='%s'" %num_id)
	for Row in vResultado:
		vId = Row[0]
		vTitulo = Row[1]
		vCategoria = Row[2]
		vAutor = Row[3]
		vEditora = Row[4]
		print("+----------------------------------------------------------------------------------------------+")
		print("| %i" %vId +" | "+ vTitulo+ " | " + vAutor+ "  | "+ vEditora+" | "+vCategoria+" |")
		print("+----------------------------------------------------------------------------------------------+") 
	
	print("\nO que Alterar.\n")
	print(" 1- Titulo;\n 2- Autor;\n 3- Editora;\n 4- Categoria;\n 5- Todos")	
	
	opcao = raw_input("\nDigite a opção desejada: ")
	while opcao !=0 :
		if opcao =='1':
			nTitulo = raw_input("Novo Titulo: ")
			executa_sql("UPDATE livro SET titulo_livro='%s' WHERE id_livro='%s'" %(nTitulo, num_id))
			break
		if opcao =='2':
			nAutor = raw_input("Novo Autor: ")
			executa_sql("UPDATE livro SET autor_livro='%s' WHERE id_livro='%s'" %(nAutor, num_id))
			break
		if opcao =='3':
			nEditora = raw_input("Nova Editora: ")
			executa_sql("UPDATE livro SET editora_livro='%s' WHERE id_livro='%s'" %(nEditora, num_id))
			break
		if opcao =='4':
			nCategoria =raw_input("Nova Categoria: ")
			executa_sql("UPDATE livro SET categoria_livro='%s' WHERE id_livro='%s'" %(nCategoria, num_id))
			break
		if opcao =='5':
			nTitulo = raw_input("Novo Titulo: ")
			nAutor = raw_input("Novo Autor: ")
			nEditora = raw_input("Nova Editora: ")
			nCategoria =raw_input("Nova Categoria: ")
			executa_sql("UPDATE livro SET titulo_livro='%s', categoria_livro='%s', autor_livro='%s', editora_livro='%s' WHERE id_livro='%s'" %(nTitulo,nCategoria,nAutor,nEditora,num_id))
			break			
		else:
			print("Opção invalida.")
			break
#Função principal.
def biblioteca(): 
	opcao = ''
	while opcao != '0' :
	        if opcao == '1':
	                adicionar()
	        if opcao == '2':
	                visualizar()
	        if opcao == '3':
	        		atualizar()
	        if opcao =='4':
	        		excluir()
		print("\n\n+-----------------------------------------------------+")
		print("|              Biblioteca Talismã                     |")
		print("+-----------------------------------------------------+")
		print("|                                                     |")
		print("|      Menu de opções                                 |")
		print("|                                                     |")
		print("|     1- Adiciona um novo livro                       |")
		print("|     2- Visualiza livros disponiveis                 |")
		print("|     3- Alterar                                      |")
		print("|     4- Excluir livro                                |")
		print("|     0- sair                                         |")
		print("|                                                     |")
		print("+-----------------------------------------------------+\n")
		opcao = raw_input("Digite o número da opção escolhida: ")
		
		

biblioteca()               
db.close()
		
