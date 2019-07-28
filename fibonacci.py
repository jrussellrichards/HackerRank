#Sequencia de Fibonacci mediante algoritmo de fuerza bruta. Falta aplicar programacion dinamica. 
def F(n):
    if n == 0: return 0
    elif n == 1: return 1

    return  F(n-1)+F(n-2)

if __name__ == "__main__":

    print(F(5))
    