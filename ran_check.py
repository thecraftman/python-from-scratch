# checks whether a number is in range includes high and low
def ran_check(num,low,high):
    #check if number is between low and high (including low and high)
    if num in range(low,high):
        print " %s is in the range" %str(num)
    else:
        print "The number is outside the range"
        
