import copy

def isPalindrome(word):
    aux_palindrome= word[::-1]
         
    return aux_palindrome == word

def palindromeIndex(word):
    for index in range((len(word)+1)//2):
        if word[index] != word[len(word)-index-1]:
            if isPalindrome(word[:index]+word[index+1:]):
                return index
            else:
                return len(word)-index-1
    return -1     

print(palindromeIndex('abbax'))