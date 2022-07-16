class MathDojo:
    def __init__(self):
        self.result = 0
    
    def __repr__(self) -> str:
        return f" Result is {self.result}"  
    
    # method to add any number of arguments
    def add(self, num, *args):
        self.result = num
        for number in args:
            self.result += number
        return self.result
    
    #method to subtract any number of arguments
    
    def subtract(self, num, *args):
        self.result = num
        for number in args:
            self.result -= number
        return self.result

# create an instance:
md = MathDojo()
# to test:
x = md.add(2)
y = md.add(2,5,1)
print(x)	# should print 5
# run each of the methods a few more times and check the result!
y = md.add(5,7)
z = md.subtract(3,2,1)


