def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

my_list = [3, 7, 1, 9, 5]
result = sum_of_list(my_list)
print(f"The sum is {result}")