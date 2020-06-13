import re

def get_count(input_str):
    num_vowels = re.compile(r'[aeiouAEIOU]')
    num_vowels = len(num_vowels.findall(input_str))
    
    return num_vowels
