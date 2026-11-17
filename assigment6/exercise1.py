numbers = []
while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(float(entry))

numbers.sort(reverse=True)
print("The five greatest numbers:")
for n in numbers[:5]:
    print(n)