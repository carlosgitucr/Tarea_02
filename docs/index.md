# Método Runge-Kutta de orden 4 (RK4) para Sistemas Dinámicos.

Para documentación visitar [github.com](https://github.com/carlosgitucr/Tarea_02).

## Sistemas dinámicos.
Los sistemas dinámicos son modelos de suma importancia en las ciencias. En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico $y$ mediante la ecuación dinámica
\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}

En esta notación, $y$ corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, $t$ corresponde a la variable temporal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como **problema de condición inicial**. 


## Problema a resolver.
Asumamos que queremos estudiar la evolución temporal de un estado $\mathbf{y}(t)$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genra la dinámica del problema es 

$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$

donde $\mathbf{O}$ es otro operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es un operación de conmutación. Note que **la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal**.



## Runge-Kutta 4
Se utilizara el metodo de Runge Kutta 4 para resolver el problema. Ver la sección de "Explanation" para más detalle. 
