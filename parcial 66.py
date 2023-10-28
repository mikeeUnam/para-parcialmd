import time 
import random

def multiplicacion():
    resultado = random.randint(1,10) * random.randint(1,10)
    print(f"Resultado de la multiplicacion {resultado}")

def division():
    resultado = random.randint(1,10) / random.randint(1,10)
    print(f"Resultado de la division {resultado}")

def suma():
    resultado = random.randint(1,10) + random.randint(1,10)
    print(f"Resultado de la suma {resultado}")

def resta():
    resultado = random.randint(1,10) - random.randint(1,10)
    print(f"Resultado de la resta {resultado}")

operaciones= [resta, suma, multiplicacion, division, multiplicacion, suma, resta]

contador = 0

while contador < len(operaciones):
        operador = operaciones[contador]
        tiempo_aleatorio = random.uniform(1,5)
        start_time= time.time()
        while time.time() - start_time < tiempo_aleatorio:
            operador()
            time.sleep(1)
        contador += 1