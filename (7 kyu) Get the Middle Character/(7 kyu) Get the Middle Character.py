def get_middle(s):
    #code
    s_len = len(s)
    number1 = int(s_len / 2)

    if len(s) <= 2:
        middle = s
    
    elif len(s)  % 2 == 1:
        middle = s[number1]
    
    else:
        middle = s[(number1-1):(number1+1)]


    return middle
