celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp +32) for temp in celcius]
print(fahrenheit)

## OR

fahrenheit = []
for temp in celcius:
    fahrenheit.append(( (9/5)*temp +32))
print(fahrenheit)
