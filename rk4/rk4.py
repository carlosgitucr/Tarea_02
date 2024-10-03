import numpy as np
oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])
def dyn_generator(oper, state):
    """Función que genera la dinámica del problema.

    Examples:

         >>> dyn_generator(oOper, yInit)
         array([[0.-0.j, 0.+1.j],
                [0.-1.j, 0.-0.j]])


    Args:
        oper (ndarray): Operador lineal O
        state (ndarray): Estado Dinámico actual

    Returns:
        array (ndarray): Operación conmutativa con el operador lineal en el eje complejo negativo.

    """
    return -1*1.0j*(np.dot(oper,state)-np.dot(state,oper))






def rk4(func, oper, state, h):
    """Método RK4.

    Examples:
    
        >>> rk4(dyn_generator, oOper, yInit, 0.7 )
        array([[0.59003333+0.j        , 0.        +0.47133333j],
               [0.        -0.47133333j, 0.40996667+0.j        ]])
    
    Args:
        func (function): Función geradora
        oper (ndarray): Operador lineal O
        state (ndarray): Estado Dinámico actual
        h (float): Paso temporal

    Returns:
        array (ndarray): estado temporal en y(t+h)

    """
    k_1= h*func(oper,state)
    k_2=h*func(oper,state+k_1/2)
    k_3=h*func(oper,state+k_2/2)
    k_4=h*func(oper,state+k_3)
    return state+1/6*(k_1+2*k_2+2*k_3+k_4)
