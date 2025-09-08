from pymongo import MongoClient

client = MongoClient(f'mongodb+srv://{user}:{password}@cluster0.fpdjnbn.mongodb.net/')

db = client.get_database('movies')
movies_collection = db.get_collection('movies_collection')

def inserir_novo_filme():
    nome_filme = input('Digite o nome do filme que deseja inserir: ')
    ano_lancamento = int(input('Digite o ano de lançamento do filme: '))
    genero = input('Digite o gênero do filme: ')
    duracao_minutos = int(input('Digite a duração em minutos do filme: '))
    novo_filme = {
        'nome': nome_filme,
        'ano_lancamento': ano_lancamento,
        'genero': genero,
        'duracao_minutos': duracao_minutos
    }
    movies_collection.insert_one(novo_filme)
    print('Filme adcionado!')

def filmes_disponiveis():
    for movie in movies_collection.find():
        print(f'Título: {movie['nome']}')

def dados_filme():
    nome_filme = input('Digite o nome do filme que deseja ver as informações: ')
    esta_na_lista = movies_collection.find_one({'nome': nome_filme})
    if esta_na_lista:
        print(f'Nome: {esta_na_lista['nome']}\nAno Lançamento: {esta_na_lista['ano_lancamento']}\nGênero: {esta_na_lista['genero']}\nDuração Minutos: {esta_na_lista['duracao_minutos']}')
    else:
        print(f'{nome_filme} não foi encontrado.')

def atualizar_filme():
    nome_filme = input('Digite o nome do filme que deseja alterar as informações: ')
    campo_desejado = int(input('Digite o número do campo que deseja alterar a informação:\n1 - Nome\n2 - Ano Lançamento\n3 - Gênero\n4 - Duração Minutos\nDigite: '))
    if campo_desejado == 1:
        campo_alterado = 'nome'
    elif campo_desejado == 2:
        campo_alterado = 'ano_lancamento'
    elif campo_desejado == 3:
        campo_alterado = 'genero'
    elif campo_desejado == 4:
        campo_alterado = 'duracao_minutos'
    else:
        print('Opção Inválida')
    valor_alterado = input('Digite a informação nova: ')
    movies_collection.update_one({'nome': nome_filme, }, {'$set':{campo_alterado:valor_alterado}})

def deletar_filme():
    nome_filme = input('Digite o nome do filme que deseja apagar: ')
    esta_na_lista = movies_collection.find_one({'nome': nome_filme})
    if esta_na_lista:
        movies_collection.delete_one({'nome': nome_filme})
        print('Filme deletado!')
    else:
        print('Não existe este filme no catálogo!')

def main():
    escolha = int(input('O que você deseja?\n\n1 - Cadastrar Filme\n2 - Consultar Filmes Disponíveis\n3 - Ver Detalhes de Um Filme\n4 - Atualizar Dados de Um Filme\n5 - Deletar um Filme\n\nDigite o número da sua escolha: '))
    if escolha == 1:
        inserir_novo_filme()
    elif escolha == 2:
        filmes_disponiveis()
    elif escolha == 3:
        dados_filme()
    elif escolha == 4:
        atualizar_filme()
    elif escolha == 5:
        deletar_filme()
    else:
        print('Opção Inválida.')

if __name__ == '__main__':
    main()

