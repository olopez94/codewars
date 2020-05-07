def positive_sum(arr):
    # Your code here
    n = 0
    i = 0
    for i in arr:
        if i > 0:
            n += i
    return n
