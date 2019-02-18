def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My choice of fruit is {}'.format(kwargs['fruit']))

    else:
        print('I did not find any fruit here')


myfunc(fruit = 'apple')



############### ARGS AND KWARGS
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I woud like {} {}'.format(args[0],kwargs['food']))
