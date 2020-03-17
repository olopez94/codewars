def getCount(inputStr):
    num_vowels = 0
    vowels = "a","e","i","o","u"


    for char in inputStr:
        if char in vowels:
            num_vowels = num_vowels+1     

    return num_vowels



