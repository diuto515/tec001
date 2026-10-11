import math
def value(diameter_cm, price):
    diameter_m = diameter_cm/100
    area = (math.pi * diameter_m/2)
    unit_price = price/ area
    return unit_price

print('Pizza 1: ')
d1= float(input('diameter_cm: '))
p1= float(input('price: '))

print('Pizza 2: ')
d2= float(input('diameter_cm: '))
p2= float(input('price: '))

pizza1= value (d1, p1)
pizza2= value (d2,p2)

print(f'1 bills: {pizza1:}')
print(f'2 bills: {pizza2:}')

if pizza1 < pizza2:
    print('pizza1 affordable than pizza2')
elif pizza1 > pizza2:
    print('pizza2 affordable than pizza1')
else:
    print('Both equal')


