a= int(input('Enter your month: '))
seasons= ['Spring', 'Summer', 'Autumn',  'Winter']
if 3 <= a <= 5:
    print(seasons[0])
elif 6<= a <=8:
    print(seasons[1])
elif 9 <= a <= 11: 
    print(seasons[2])
elif a == 12 or a == 1 or a == 2:
    print(seasons[3])
else:
    print('Invalid')
