def high_and_low(numbers):
    # ...
    
    numbers = [int(i) for i in numbers.split()]
    numbers.sort()
    numbers = [numbers[-1], numbers[0]]
    numbers = ' '.join(str(i) for i in numbers)
    
    return numbers


'''
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
'''
