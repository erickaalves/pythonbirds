class Direcao:
    def __init__(self, valor:str = 'Norte'):
        self.valor = valor
    def girar_esquerda(self):
        if direcao.valor == 'Norte':
            direcao.valor = 'Oeste'
        elif direcao.valor == 'Oeste':
            direcao.valor = 'Sul'
        elif direcao.valor == 'Sul':
            direcao.valor = 'Leste'
        elif direcao.valor == 'Leste':
            direcao.valor = 'Norte'

    def girar_direita(self):
        if direcao.valor == 'Norte':
            direcao.valor = 'Leste'
        elif direcao.valor == 'Leste':
            direcao.valor = 'Sul'
        elif direcao.valor == 'Sul':
            direcao.valor = 'Oeste'
        elif direcao.valor == 'Oeste':
            direcao.valor = 'Norte'


direcao = Direcao()

direcao.valor = 'Leste'
print(f'A direcao inicial é {direcao.valor}')
direcao.girar_esquerda()
print(f'Apos girar a esquerda é {direcao.valor}')
direcao.girar_direita()
print(f'Apos girar a direita é {direcao.valor}')
