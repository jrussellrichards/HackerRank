

def minimumBribes(queue):
    bribes=0
    for position,ticket_person in enumerate(queue):
        if(ticket_person-(position+1)>2):
            return "Too chaotic"
        for j in range(max(0,ticket_person-2), position):
            if queue[j] > ticket_person:
                bribes+=1
    return bribes




print(minimumBribes([2,1,5,4,3]))
