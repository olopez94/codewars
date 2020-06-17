def descending_order(num):
    # Bust a move right he
    listNum = list(str(num))
    listNum = sorted(listNum, reverse = True)
    ans = ''.join(listNum[:])
    return int(ans)
