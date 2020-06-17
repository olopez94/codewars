def descending_order(num):
    # Bust a move right he
    listNum = list(str(num))
    listNum = sorted(listNum, reverse = True)
    ans = ''.join(listNum[:])
    return int(ans)
'''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def descending_order(num):
    # Bust a move right here
    sortNum = sorted(str(num), reverse = True)
    ans = int(''.join(sortNum))
    
    return ans
'''
