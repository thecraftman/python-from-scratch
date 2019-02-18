def makes_twenty(n1,n2):
    if n1+n2 ==20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

    #or
    return (n1+n2) ==20 or n1==20 or n2 ==20


makes_twenty(20,10)
