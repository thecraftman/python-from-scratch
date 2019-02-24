class simple():

    def __init__(self,value):

        self.value = value

    def add_to_value(self,amount):

        self.value = self.value + amount
        print("We just added {} to your value".format(amount))

    
