def high_and_low(numbers):
    # ...
    
    numbers = [int(i) for i in numbers.split()]
    numbers.sort()
    numbers = [numbers[-1], numbers[0]]
    numbers = ' '.join(str(i) for i in numbers)
    
    return numbers
