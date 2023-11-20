import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmac"
)

cursor = conexao.cursor()

# Menu principal
menu_principal = '''1 - Alunos
2 - Funcionarios
3 - Personal
4 - Modalidades'''

# Opções disponíveis
opcoes = '''1 - Adicionar
2 - Deletar
3 - Alterar
4 - Exibir
5 - Trocar tabela'''

# Dados para a tabela de Alunos
dados_alunos = ['Nome:', 'CPF:', 'Telefone:', 'Endereço:']
dados_aluno = [''] * 4

# Dados para a tabela de Funcionarios
dados_funcionarios = ['Nome:', 'CPF:', 'Departamento:', 'Salario:']
dados_funcionario = [''] * 4

# Dados para a tabela de Personal
dados_personal = ['Nome:', 'CREF:']
dados_personais = [''] * 2

# Dados para a tabela de Modalidades
dados_modalidades = ['Nome', 'Duração']
dados_modalidade = [''] * 2

print(menu_principal)

while True:
    escolha_tabela = int(input("Escolha a TABELA:"))

    if escolha_tabela == 1:    # Operações para a tabela de Alunos
        print("-" * 20)
        print("Tabela ALUNOS")
        print("-" * 20)
        print(opcoes)
        operacao = int(input("Escolha a operação:"))

        if operacao == 1:     # Adicionar aluno
            print("-" * 20)
            print("Adicionar ALUNO")
            print("-" * 20)
            sql = "INSERT INTO alunos (nome, telefone, cpf, endereco) VALUES (%s, %s, %s, %s)"
            for c in range(4):
                dados_aluno[c] = str(input(f"Insira o {dados_alunos[c]}"))
            data = (dados_aluno[0], dados_aluno[2], dados_aluno[1], dados_aluno[3])
            cursor.execute(sql, data)
            conexao.commit()
            userid = cursor.lastrowid

        elif operacao == 2:   # Deletar aluno
            pesquisa = 'SELECT * FROM alunos;'
            cursor.execute(pesquisa)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)
            deletar = int(input("ID do aluno:"))
            sql_deletar = f'DELETE FROM alunos WHERE matricula = {deletar}'
            cursor.execute(sql_deletar)
            conexao.commit()
            userid = cursor.lastrowid

        elif operacao == 3: # Alterar aluno
            pesquisa = 'SELECT * FROM alunos;'
            cursor.execute(pesquisa)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)
            aluno_id = int(input("ID do aluno:"))
            print(f'1 - para {dados_alunos[0]}/n2 - para {dados_alunos[1]}/n3 - para {dados_alunos[2]}/n4 - para {dados_alunos[3]}')
            update_opcao = int(input("O que você quer mudar?"))
            if update_opcao == 1:
                valor_novo = str(input(f"Novo {dados_alunos[update_opcao - 1]}"))
                sql_update = f'UPDATE alunos SET nome = {valor_novo} WHERE matricula = {aluno_id};'
                cursor.execute(sql_update)
                conexao.commit()
                userid = cursor.lastrowid

        elif operacao == 4:
            # Exibir alunos
            pesquisa = 'SELECT * FROM alunos;'
            cursor.execute(pesquisa)
            resultado = cursor.fetchall()
            for x in resultado:
                print(x)

    if escolha_tabela == 2:
        print("-" * 20)
        print("Tabela FUNCIONARIOS")
        print("-" * 20)
        print(opcoes_operacao)
        operacao = int(input("Escolha a operação:"))

        if operacao == 1:
            print("-" * 20)
            print("Adicionar Funcionario")
            print("-" * 20)
            query_insercao = 'insert into funcionarios(nome, cpf, departamento, salario) values (%s, %s, %s, %s)'
            for indice in range(4):
                dados_funcionarios[indice] = str(input(f"Insira o {dados_funcionarios[indice]}"))
            parametros = (dados_funcionarios[0], dados_funcionarios[1], dados_funcionarios[2], dados_funcionarios[3])
            cursor.execute(query_insercao, parametros)
            conexao.commit()
            userid = cursor.lastrowid

    if escolha_tabela == 3:
        print("-" * 20)
        print("Tabela PERSONAL")
        print("-" * 20)
        print(opcoes_menu)

        # Obtendo a operação desejada
        operacao = int(input("Escolha a operação (1 a 5):"))

        if operacao == 1:
            print("-" * 20)
            print("Adicionar Personal")
            print("-" * 20)
            query_insercao = 'insert into personal(nome, cref) values (%s, %s)'
            for indice in range(2):
                dados_personal[indice] = str(input(f"Insira o {dados_personal[indice]}"))
            dados_insercao = (dados_personal[0], dados_personal[1])
            meu_cursor.execute(query_insercao, dados_insercao)
            conexao_banco.commit()
            id_inserido = meu_cursor.lastrowid

        elif operacao == 2:
            query_selecao = 'select * from personal;'
            meu_cursor.execute(query_selecao)
            resultados = meu_cursor.fetchall()
            for linha in resultados:
                print(linha)
            id_deletar = int(input("ID do personal:"))
            query_delecao = f'''delete from personal where cod_personal = {id_deletar}'''
            meu_cursor.execute(query_delecao)
            conexao_banco.commit()
            id_deletado = meu_cursor.lastrowid

        elif operacao == 4:
            query_selecao = 'select * from personal;'
            meu_cursor.execute(query_selecao)
            resultados = meu_cursor.fetchall()
            for linha in resultados:
                print(linha)

    elif escolha_tabela == 4:
        print("-" * 20)
        print("Tabela MODALIDADES")
        print("-" * 20)
        print(opcoes_menu)

        # Obtendo a operação desejada
        operacao = int(input("Escolha a operação (1 a 5):"))

        if operacao == 1:
            print("-" * 20)
            print("Adicionar Modalidade")
            print("-" * 20)
            query_insercao = 'insert into modalidade(nome, duracao) values (%s, %s)'
            for indice in range(2):
                dados_modalidades[indice] = str(input(f"Insira o {dados_modalidades[indice]}"))
            dados_insercao = (dados_modalidades[0], dados_modalidades[1])
            meu_cursor.execute(query_insercao, dados_insercao)
            conexao_banco.commit()
            id_inserido = meu_cursor.lastrowid

        elif operacao == 2:
            query_selecao = 'select * from modalidade;'
            meu_cursor.execute(query_selecao)
            resultados = meu_cursor.fetchall()
            for linha in resultados:
                print(linha)
            id_deletar = int(input("ID da modalidade:"))
            query_delecao = f'''delete from modalidade where id_modalidade = {id_deletar}'''
            meu_cursor.execute(query_delecao)
            conexao_banco.commit()
            id_deletado = meu_cursor.lastrowid

        elif operacao == 4:
            query_selecao = 'select * from modalidade;'
            meu_cursor.execute(query_selecao)
            resultados = meu_cursor.fetchall()
            for linha in resultados:
                print(linha)


    elif escolha_tabela == 5:
        break

    else:
        print("Opção Inválida")
        escolha_tabela = int(input("Escolha a TABELA:"))