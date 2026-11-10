numbers = []
while True:
    text = input("Enter a number (empty to quit): ")
    if text == "":
        break
    numbers.append(float(text))

numbers.sort(reverse=True)
print("5 greatest numbers:", numbers[:5])


numbers=[]