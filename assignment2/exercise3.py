def value():
    sex = input('Male/Female ')
    g_l = float(input('your value is: '))
    if sex == 'Male':
        if g_l < 117:
            print('Low')
        elif g_l >= 117 and g_l <= 155:
            print ('Normal')
        else:
            print ('High')

    if sex == 'Female':
        if g_l < 134:
            print('Low')
        elif g_l >= 134 and g_l <= 167:
            print('Normal')
        else:
            print('High')

value()       