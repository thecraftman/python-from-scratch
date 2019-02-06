#for loops are traditionally used
#when you have a block of code which
#you want to repeat a fixed number of times

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist = [100,200,300,400,500]
for num in mylist:
    print(num)

#adding if
for num in mylist:
    #check for even
    if num % 2 ==0:
        print(num)
    else:
        print(f'odd number:{num}') #prints it one after the other

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
print(list_sum)

mystring = 'hello world'
for letter in mystring:
    print(letter)

#more examples
tup = (1,2,3)
for item in tup:
    print(item)

mylist = [1,2,3,4,5,6]
len (mylist)

mylist = [(1,2),(3,4),(5,6),(7,8)]
len (mylist)
for item in mylist:
    print(item)
for a in mylist:
    print(a)

#more examples
mylist = [(1,2,3),(5,6,7),(8,9,10)]
for item in mylist:
    print(item)
