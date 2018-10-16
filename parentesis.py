def isBalanced(sequence): 
    stack=[] #stack en el cual almaceno los simbolos de entrada
    list_sequence=list(sequence)   #Para tratar la sequencia como lista pero no influye en nada
    for i,brace in enumerate(list_sequence): #Recorro toda la sequencia
        if(brace=="{" or brace=="[" or brace=="("): # Agrego al stack auxiliar los simbolos de apertura
            stack.append(brace)    
        else:
            if(len(stack)>0): #Si hay simbolos agregados al stack comparo el ultimo elemento de este con el simbolo actual, verificando que sea su contraparte de cierre.
                #En caso de no serlo, retorno falso. 
                last_opened=stack.pop()            
                if((brace=="}" and last_opened!="{")
                or (brace=="]" and last_opened!="[")
                or (brace==")" and last_opened!="(")):
                    return "NO"
            else:
                return "NO"            
                
            
    if(len(stack)==0):#Si el stack es vacio entonces retorno verdadero, esto quiere decir que todos los elementos abiertos tuvieron sus pares
        return "Yes"
    else: # Esta condicion es para casos borde en donde las secuencias sean mayoritariamente elementos abiertos. Ejemplo: [[ 
        return "NO" 


print("ingrese la secuencia a comparar")
sequence=input()
print(isBalanced(sequence))
