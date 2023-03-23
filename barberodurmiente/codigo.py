import threading
import time
import queue
import random
ip = int(0)
numero = int(input("Ingrese el numero de sillas de espera: "))
class Barbero(threading.Thread):
    def __init__(self, clientes,posicion):
        threading.Thread.__init__(self)
        self.clientes = clientes
        self.posicion = posicion

      
    def run(self):

        while True:
            try:
                cliente = self.clientes.get(block=False)
                print("Atendiendo a cliente ")
                time.sleep(random.randint(1,2))
                print("Terminó de atender a cliente")
                self.clientes.task_done()
                
            except queue.Empty:
                print("Durmiendo...")
                time.sleep(1)

class Cliente(threading.Thread):
    def __init__(self, clientes):
        threading.Thread.__init__(self)
        self.clientes = clientes
    
    def run(self):
        self.clientes.put(self)
        print("Cliente llegó a la barbería",)

clientes = queue.Queue(maxsize=numero)
barbero = Barbero(clientes,0)
barbero.start()

while True:
    try:
        cliente = Cliente(clientes)
        cliente.start()
        time.sleep(random.randint(0,2))
    except KeyboardInterrupt:
        break
