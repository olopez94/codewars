def square_digits(num):
    ans = ''
    for i in str(num):
        ans += str(int(i)**2)
    return int(ans)
