import re

def sum_numbers(text):
    numbers = re.findall(r'\d+', text)   
    total = 0
    for n in numbers:
        total += int(n)                  
    return total

print(sum_numbers("Today is January 16, 2025. The temperature is 11 degrees Celsius."))