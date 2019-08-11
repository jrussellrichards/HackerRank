def minimumBribes(queue):
    bribes=0
    for position,person in enumerate(queue):
        if(person-(position+1)>2):
            return 'Too chaotic'
        for previous_person in queue[position:len(queue)]:
            if(person>previous_person):
                bribes+=1
    return bribes


print(minimumBribes([1 ,2 ,5 ,3 ,7 ,8 ,6 ,4]))
