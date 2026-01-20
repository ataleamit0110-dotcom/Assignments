#1 WAP to accept one char and ceck whether that char is vowel or not
#Input  a
# Output vowel

def checkVowels(ch):
    #vowels = "aeiou"
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return True
    else:
        return False
    # if vowels.__contains__(ch.lower()):
    #     return True
    # else:
    #     return False
    
result = checkVowels('a')
print("Is vowel:", result)