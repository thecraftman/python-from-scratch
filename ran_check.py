# checks whether a number is in range includes high and low
def ran_check(num,low,high):
    #check if number is between low and high (including low and high)
    if num in range(low,high):
        print " %s is in the range" %str(num)
    else:
        print "The number is outside the range"





    ####

    def up_low(s):
    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print "original string : ",s
    print "No. of upper case characters : ",d ["upper"
    print "No. of lower case characters : ",d["lower"]
