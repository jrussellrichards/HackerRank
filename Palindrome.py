import copy

def is_palindrome(word):
    aux_palindrome= ""
    for index,char in enumerate(word):
        aux_palindrome = aux_palindrome + word[len(word)-1 - index]
         
    return aux_palindrome == word

def palindromeIndex(word):
    if(is_palindrome(word)):
        return (-1)
    
    for index,char in enumerate(word):
        word_aux=word[0:index]+word[index+1:len(word)]
        print(word_aux)
        if(is_palindrome(word_aux)):
            return index
    return 0        

print(palindromeIndex('abbax'))