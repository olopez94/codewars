def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U')
    newString = string 
    for item in string:
        if item in vowels:
            newString = newString.replace(item, "")
    
    return newString

'''
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
'''

'''
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
'''
