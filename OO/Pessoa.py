class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
##metodo estatico eu nao dependo de classe ou objeto sao pra funçoes que serao usadas na class nao dentro da class

    @classmethod
    def metodo_de_classe(cls):
        nome_composto = pai1.nome, pai1.filhos
        print(nome_composto)



pessoa1 = Pessoa(nome='Erick')

pai1 = Pessoa(('Erick', 'Carol', 'Sara'), nome = 'Roberto', idade = 40)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.cumprimentar())
print(pai1.filhos)
for filhos in pai1.filhos:
    print(filhos)
pai1.sobrenome = 'Alves'
##atributo dinamico
##atributo complexo é como a lista podendo ser atributo

print (pai1.sobrenome)

print(pai1.__dict__)
##mostra todos os atributos de instância da Pessoa

print(f'O {pai1.nome} tem {pai1.olhos} olhos')
##olhos está sendo atributo da classe, já que tem um valor comum a todos da classe pessoa.

print(id(Pessoa.olhos), id(pai1.olhos))
## A menos que eu mude dentro de cada objeto o valor será o mesmo padrão da classe

pai1.olhos = 3
print(id(Pessoa.olhos), id(pai1.olhos))
##Os ids mudaram pq eu mudei o valor de olhos para o objeto pai 1 em relacao ao padrao da classe

print(Pessoa.metodo_estatico(), pai1.metodo_estatico())
##SEM USO DE OBJETOS OU CLASSE
print(Pessoa.metodo_de_classe(), pai1.metodo_de_classe())
##USANDO OS ATRIBUTOS DE CLASSE
