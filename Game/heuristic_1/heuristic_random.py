import time
from random import randrange


class HeuristicRandom:
    def __init__(self):
        self.start_time = time.time()
        self.value = randrange(10)
