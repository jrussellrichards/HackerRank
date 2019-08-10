#Sequencia de Fibonacci mediante  programacion dinamica. 
def Fibonacci(n,memory):
    if(type(n)!=int or n<0):
        raise TypeError("n debe ser un entero positivo")

    if n == 0: return 0
    elif n == 1: return 1

    if(memory[n]==None):
        memory[n]=Fibonacci(n-1,memory)+Fibonacci(n-2,memory)


    return  memory[n]

if __name__ == "__main__":

    memory=[None]*1000

    for i in range(1000):
        print(i,Fibonacci(i,memory))
    