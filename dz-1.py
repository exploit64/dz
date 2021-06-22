from random import randint
from threading import Thread, Lock, Semaphore
from time import sleep


class Philosopher(Thread):
    def __init__(self, number, fork_left, fork_right):
        super().__init__()
        self.number = number
        self.fork_left = fork_left
        self.fork_right = fork_right

    def run(self):
        while True:
            print("Философ #%d ест вилками %d, %d" % (self.number, self.fork_left.get(), self.fork_right.get()))
            sleep(randint(1, 3))
            self.fork_left.free()
            self.fork_right.free()
            print("Философ #%d думает " % self.number)
            sleep(randint(1, 3))


class Fork:

    def __init__(self, number):
        self.number = number
        self.fork_lock = Lock()

    def get(self):
        # ждем, если 4 вилки взято
        with semaphore:
            self.fork_lock.acquire()
        return self.number

    def free(self):
        self.fork_lock.release()


semaphore = Semaphore(4)
forks = (Fork(0), Fork(1), Fork(2), Fork(3), Fork(4))

if __name__ == '__main__':
    # каждому философу передаем две возможные вилки
    for i in range(5):
        Philosopher(i, forks[i], forks[0] if i == 4 else forks[i + 1]).start()
