def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U')
    newString = string 
    for item in string:
        if item in vowels:
            newString = newString.replace(item, "")
    
    return newString
