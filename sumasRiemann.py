import numpy as np 
from typing import Callable

def tabulacion(x:np.array, y:np.array, precision:int=3) -> None:
    print(f"x\t\ty\n{'_'*30}")
    for i,j in zip(x,y):
        print(f"{round(i,precision)}\t\t{round(j,precision)}")

def sumaRiemann(function:Callable, rango:tuple[float], n:int) -> float:
    assert len(rango) == 2
    a,b = rango
    if not( isinstance(a,(float,int)) and isinstance(b,(float,int))):
        raise Exception("Invalid data types in range")
    delta_x = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = function(x)
    suma_inf = np.cumsum(y[:-1])*delta_x
    suma_sup = np.cumsum(y[1:])*delta_x
    tabulacion(x,y)
    return suma_inf, suma_sup
    

if __name__ == "__main__":
    f_x = lambda x: (2*x**3 - (3/x**2))
    g_x = lambda x: (np.sin(x) - (x/2)) 
    # for n in (5,10,15):
    #     sumaRiemann(f_x, (-1,3), n)
    for n in (3,12):
        suma_inf, suma_sup = sumaRiemann(g_x, (0,2.5), n)
        print(f"Suma inf = {suma_inf[-1]}")
        print(f"Suma sup = {suma_sup[-1]}")
        print("\n","_"*30)