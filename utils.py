from models import Pessoas, Usuarios

# Insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Vanessa', idade=30)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Vanessa').first()
    #print(pessoa.idade)

# Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ze Roberto').first()
    pessoa.nome = 'Ze Manoel'
    pessoa.save()

# Exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Vanessa').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('esdras','1234')
    insere_usuario('vanessa', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
