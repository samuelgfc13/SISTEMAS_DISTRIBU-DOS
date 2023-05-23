import threading
import time

class Racer(threading.Thread):
    def __init__(self, racer_id):
        super().__init__()
        self.racer_id = racer_id

    def run(self):
        print(f"Racer {self.racer_id} started")
        time.sleep(1)  # Tempo de espera de 1 segundo
        print(f"Racer {self.racer_id} finished")

class Race:
    def __init__(self):
        self.racers = []

    def create_racers(self):
        for i in range(1, 11):
            racer = Racer(i)
            self.racers.append(racer)

    def start_race(self):
        for racer in self.racers:
            racer.start()

        for racer in self.racers:
            racer.join()

race = Race()
race.create_racers()
race.start_race()

# A) Como se deu o comportamento dos prints?

# Ocorreu uma ordem aleatória dos numeros significa que a ordem de início e término
# dos corredores pode variar a cada execução

# B) Adiciona um tempo de espera (usando o método sleep) nos Racers, o
# que houve com comportamento do sistema?

#  Adicionando um timea a ordem de término dos corredores será determinística, mas a ordem de
#  início ainda pode variar. O comportamento do sistema pode parecer mais sincronizado,
#  pois os corredores agora têm uma pausa uniforme antes de terminar.

# C) Utilize o método setPriority (java) para definir as condições decorrida. Houve mudanças na execução?

# não há um método de setPriority em python ja que  threads é  tratada automaticamente pelo interpretador Python 