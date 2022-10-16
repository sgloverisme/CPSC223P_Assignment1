#Sarah Glover
#date 8/24/2022
#file purpose: multiple hello functions
import math  #math library

def helloworld():   #making a funtion w/ no paramaters
    return "hello World!"

def helloname(name):         #making a function w paramaters 
    return "Hello " + name + " !"

def printlist():
    list=["the", "oak", "tree", "hehe"]
    return list

def doingadd(a,b):
   return a + b  #adding

def subtracting(a,b):
    return b-a #subtracting

def div(a,b):
    return b/a #dividing

def mul(a,b):
    return a*b   #multiplying

def evenOdd(a):
    if a%2==0:
        return "number is even"
    else:
        return "number is odd"

def factorial(x):
    return math.factorial(x)