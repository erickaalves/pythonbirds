
'''
Composto por uma classe que possua duas classes, atributos compostos.

1-Motor
2-Direcao
    EXEMPLO:
    >>>##Testando motor
    >>>motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    1
    >>> motor.acelerar()
    2
    >>> motor.acelerar()
    3
    >>> motor.frear()
    1
    >>> motor.frear()
    >>> motor.velocidade()
    0
    >>>##Testando direçaõ
    >>>direcao = Direcao()
    >>> direcao.valor()
    'Norte'
    >>> direcao.girar_direita()
    >>>direcao.valor()
    'Leste'
    >>>direcao.girar_direita()
    >>>direcao.valor()
    'Sul'
    >>> direcao.girar_direita()
    >>>direcao.valor()
    'Oeste'
    >>> direcao.girar_direita()
    >>>direcao.valor()
    'Norte'
    >>> direcao.girar_esquerda()
    >>>direcao.valor()
    'Oeste'
    >>> direcao.girar_esquerda()
    >>>direcao.valor()
    'Sul'
    >>> direcao.girar_esquerda()
    >>>direcao.valor()
    'Leste'
    >>> direcao.girar_esquerda()
    >>>direcao.valor()
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
    >>>carro1.calcular_direcao()
    'Norte'
    >>>carro1.girar_direita()
    >>>carro1.calcular_direcao()
    'Leste'
    >>>carro1.girar_esquerda()
    >>>carro1.calcular_direcao()
    'Norte'
    >>>carro1.girar_esquerda()
    >>>carro1.calcular_direcao()
    'Leste'
'''