def matchingStrings(strings, queries):

    values={}
    answer=[]

    for i in strings:
        if i  in values:
            values[i]+=1
        else:
            values[i]=1
    

    for i in queries:
        if(i in values):
            answer.append(values[i])
        else:
            answer.append(0)
    
    return answer



print(matchingStrings(['aba','baba','aba','xzxb'],['aba','xzxb','ab']))