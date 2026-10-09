def ex1():
    length = float(input('how many centimet'))
    if length < 42:
        print('bring back lake')
        cm_short= 42 - length
        print (f'u lack {cm_short} centimet')
    else:
        print(' good fish')

ex1()