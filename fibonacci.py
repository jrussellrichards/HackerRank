#Sequencia de Fibonacci mediante algoritmo de fuerza bruta. Falta aplicar programacion dinamica. 
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    a=n-1
    b=n-2
    c=  F(a)+F(b)
    return c

if __name__ == "__main__":

    print(F(5))