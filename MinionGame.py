def minion_game(string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    alphabet=list(map(chr, range(65, 91)))+list(map(chr, range(97, 123)))
    consonant=list(filter(lambda x: x not in (vowels) ,alphabet))
    answer=''

    def calculate_score(string,start_chars_allowed):
        words={}
        score=0
        # vowels_in_string=list(filter(lambda x: x in (vowels) ,string))
        for start,char in enumerate(string):
            if(char in start_chars_allowed):
                for end in range(start,len(string)):
                    substring=string[start:end+1]
                    if( substring in words):
                        words[substring]+=1
                    else:
                        words[substring]=1
        
        score=sum(words[key] for key in words.keys())

        return score

    stuart_score=calculate_score(string,consonant)
    kevin_score=calculate_score(string,vowels)

    if(stuart_score>kevin_score):
        answer='Stuart'+' '+str(stuart_score)
    elif(stuart_score<kevin_score):
        answer='Kevin'+' '+str(kevin_score)
    else:
        answer='Draw'

    
    return print(answer)

minion_game('Banana')
    
