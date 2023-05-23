import threading

class Racer(threading.Thread):
    def __init__(self, racer_number):
        threading.Thread.__init__(self)
        self.racer_number = racer_number

    def run(self):
        while True:
            print(f"Racer {self.racer_number} - imprimindo")

# Exemplo de criação e instanciação da classe Racer
racer1 = Racer(1)
racer2 = Racer(2)

# Iniciando as threads
racer1.start()
racer2.start()