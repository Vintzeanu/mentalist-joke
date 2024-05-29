import itertools
from sys import stdout as terminal
from time import sleep
from threading import Thread

def animatie(done_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        terminal.write('\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\rGata!    \n')
    terminal.flush()

def run_animatie():
    done_event = ThreadEvent()
    t = Thread(target=animatie, args=(done_event,))
    t.start()
    sleep(5)  # Durata animației
    done_event.set()
    t.join()

class ThreadEvent:
    def __init__(self):
        self.done = False

    def is_set(self):
        return self.done

    def set(self):
        self.done = True

# Bucla pentru a solicita un număr valid
while True:
    val = input("Gândește-te la un număr: ")
    if val.isnumeric():
        break
    else:
        print("Am zis să introduci un număr! \"" + str(val) + "\" nu este număr")

print("Analizez undele cerebrale")
run_animatie()

print("Scanez memoria")
run_animatie()

print("Calculez posibilitățile")
run_animatie()

print("Decodific gândurile")
run_animatie()

print("Te-ai gândit la numărul: " + val + "\n")