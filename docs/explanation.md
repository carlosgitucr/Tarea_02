## Método Runge-Kutta de orden 4 (RK4)

Para la reolución del problema dinámico se utiliza el método Runge-Kutta de orden 4. El cual es un método para resolver problemas de valor inicial para ecuaciones diferenciales ordinarias. Este funciona al calcular 4 aproximaciones intermedias denotadas por $k_n$ y luego a partir de estas se calcula el estado del sistema $y en el tiempo $t+h$ donde $t$ es el tiempo actual y $h$ es el paso temporal.    

\begin{equation}
k_1 = hf(t_n,y)\\
\end{equation}

\begin{equation}
k_2 = hf(y_n+ \frac{k_1}{2},t + \frac{h}{2}), \\
\end{equation}

\begin{equation}
k_3 = hf(y_n+ \frac{k_2}{2},t + \frac{h}{2}), \\
\end{equation}

\begin{equation}
k_4 = hf(y_n+ k_3,t_n + h)\\
\end{equation}

\begin{equation}
y_n(t+h) = y(t) + \frac{1}{6} (k_1+ 2k_2 + 2k_3 +k_4)
\end{equation}

