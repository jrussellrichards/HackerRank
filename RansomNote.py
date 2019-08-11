from collections import defaultdict

def returnDictWithCountWords(text):
    dictionary = {} 
    dictionary = defaultdict(lambda:0,dictionary)
    for word in text:
        dictionary[word]+=1
    
    return dictionary


def checkMagazine(magazine, note):

    dictMagazine=returnDictWithCountWords(magazine)
    dictNote=returnDictWithCountWords(note)

    for word in dictNote:
        if(word not in dictMagazine):
            return 'No'
        if(dictNote[word]>dictMagazine[word]):
            return 'No'
    return 'Yes'


print(returnDictWithCountWords('hola como estas'))