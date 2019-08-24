def getMinimumCost(numberOfClients, costFlowers):
    costFlowers.sort(reverse = True) 
    currentClient=1
    multiplier=1
    minimumCost=0
    for flower in costFlowers:
        minimumCost=flower*multiplier
        if(currentClient==numberOfClients):
            multiplier+=1
            currentClient=1
        else:
            currentClient=1
    return minimumCost

print()
        

