import threading
import time

class Racer(threading.Thread):
    def __init__(self, racer_id):
        super().__init__()
        self.racer_id = racer_id

    def run(self):
        for i in range(1000):
            print(f"Racer {self.racer_id} - Count: {i+1}")

        print(f"Racer {self.racer_id} finished")

class Race:
    def __init__(self):
        self.racers = []

    def create_racers(self):
        for i in range(1, 11):
            racer = Racer(i)
            self.racers.append(racer)

    def start_race(self):
        odd_racers = []
        even_racers = []

        for racer in self.racers:
            if racer.racer_id % 2 == 0:
                even_racers.append(racer)
            else:
                odd_racers.append(racer)

        for racer in odd_racers:
            racer.start()

        for racer in odd_racers:
            racer.join()

        for racer in even_racers:
            racer.start()

        for racer in even_racers:
            racer.join()

race = Race()
race.create_racers()
race.start_race()