import numpy
def sqrt(x):
    numpy.sqrt(x)
x = input("square root from ")
try:    
    debug = int(x)
except:
    print("ERROR: Are you sure your number is valid?")
print(f"square root from {x} is {sqrt(int(x))}")