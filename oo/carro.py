
'''
Composto por uma classe que possua duas classes, atributos compostos.

1-Motor
2-Direcao
    EXEMPLO:
    >>> ###Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> ##Testando direçaõ
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Norte'


    >>> carro1 = Carro(direcao, motor)
    >>> carro1.calcular_velocidade()
    0
    >>> carro1.acelerar()
    >>> carro1.calcular_velocidade()
    1
    >>> carro1.acelerar()
    >>> carro1.calcular_velocidade()
    2
    >>> carro1.acelerar()
    >>> carro1.calcular_velocidade()
    3
    >>> carro1.frear()
    >>> carro1.calcular_velocidade()
    1
    >>> carro1.frear()
    >>> carro1.calcular_velocidade()
    0
    >>> carro1.calcular_direcao()
    'Norte'
    >>> carro1.girar_direita()
    >>> carro1.calcular_direcao()
    'Leste'
    >>> carro1.girar_esquerda()
    >>> carro1.calcular_direcao()
    'Norte'
    >>> carro1.girar_esquerda()
    >>> carro1.calcular_direcao()
    'Oeste'
'''
class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao
    def calcular_velocidade(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    ##pq os parenteses(frear e acelerar sao funcoes da classe, velocidade é um metodo)
    def frear(self):
        return self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_direita(self):
        return self.direcao.girar_direita()
    def girar_esquerda(self):
        return self.direcao.girar_esquerda()


        
        
class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        if self.velocidade <= 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direcao:
    ##par chave valor com o uso de dicionário(no caso de if else muito longo)
    rotacao_direita_dct = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    rotacao_esquerda_dct = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.valor = NORTE
    def girar_esquerda(self):
##substituido por dicionarios
     self.valor = self.rotacao_esquerda_dct[self.valor]

     """if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor =LESTE
        elif self.valor == LESTE:
            self.valor = NORTE
    """
    def girar_direita(self):
        self.valor = self.rotacao_direita_dct[self.valor]
##substituido por dicionarios
    """
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE
    """
