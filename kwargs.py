def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My choice of fruit is {}'.format(kwargs['fruit']))

    else:
        print('I did not find any fruit here')
