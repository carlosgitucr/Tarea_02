``` py linenums="1"
import numpy as np
import matplotlib.pyplot as plt
from rk4.rk4 import rk4
from rk4.rk4 import dyn_generator

oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])

times=np.linspace(0,10,num=100)

h=times[1]-times[0]

yCopy = yInit.copy()

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

for tt in range(times.size):
    # Guarde el valor de las entradas (0,0) y (1,1) en los arreglos que definimos
    # Obtenga estos valores de las entradas de yInit
    # Código aquí ->
    stateQuant00[tt]=yInit[0,0].real
    stateQuant11[tt]=yInit[1,1].real


    # Invoque rk4 operando sobre yInit
    # y devuelva el resultado a un nuevo yN
    # Código aquí ->
    yN=rk4(dyn_generator,oOper, yInit,h)
    # Ahora asignamos yN a yInit
    # De esta manera, en la siguiente iteración, el operador de esta iteración se convierte en el inicial
    # de la siguiente iteración
    yInit = yN

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(times, stateQuant00, label='Estado (0,0)', linewidth=2.0, color='blue')
plt.plot(times, stateQuant11, 'x', label='Estado (1,1)', markeredgewidth=2, color='green')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Evolución del estado con Runge-Kutta 4')
plt.legend()
plt.grid(True)
plt.show()

# Probar con diferentes valores de h para analizar estabilidad
colors = ['green', 'orange', 'magenta', 'blue']  # Colores diferentes para cada h
h_values = [0.05, 0.1, 0.5, 1.0]

for i, new_h in enumerate(h_values):
    yInit = yCopy.copy()
    stateQuant00 = np.zeros(times.size)
    stateQuant11 = np.zeros(times.size)
    
    for tt in range(times.size):
        stateQuant00[tt] = yInit[0, 0].real
        stateQuant11[tt] = yInit[1, 1].real
        yN = rk4(dyn_generator, oOper, yInit, new_h)
        yInit = yN

    plt.plot(times, stateQuant00, label=f'h={new_h}', color=colors[i])

plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Evolución del estado con diferentes valores de h')
plt.legend()
plt.grid(True)
plt.show()

```
