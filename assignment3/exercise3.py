largest=None 
smallest=None
while True:
    typing = input('numbers(click enter to quit)')
    if typing == "":
        break
    numbers=float(typing)
    if largest == None and smallest == None:
        largest = numbers
        smallest = numbers
    else:
        if numbers > largest:
            largest = numbers
        if numbers < smallest:
            smallest = numbers

print('The largest number is: ',largest )
print('The smallest number is: ', smallest)