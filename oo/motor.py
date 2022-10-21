class Motor:

    def __init__(self, velocidade:int = 0):
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        if self.velocidade <=2:
            self.velocidade = 0
        else:
            self.velocidade -=2
motor = Motor()

motor.acelerar()
motor.acelerar()
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)



