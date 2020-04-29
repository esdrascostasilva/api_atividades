from models import Pessoas

# Insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Vanessa', idade=30)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Vanessa').first()
    print(pessoa.idade)

# Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ze Roberto').first()
    pessoa.nome = 'Ze Manoel'
    pessoa.save()

# Exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Vanessa').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()
    exclui_pessoa()
