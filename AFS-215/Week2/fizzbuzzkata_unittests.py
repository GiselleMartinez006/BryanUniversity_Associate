from fizzbuzzkata import fizzBuzz
from random import random


def can_i_call_fizzbuzz():
    rand = round(random()*100)
             
    print(rand)
    # print(fizzBuzz(rand))
    
    if fizzBuzz: return "I can call fizzbuzz = " + fizzBuzz(rand) 

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    return retVal == expectedRetVal
    
def test_1():
    return checkFizzBuzz(1, "1")
    
def test_2():
    return checkFizzBuzz(2, "2")
    
def test_3():
    return checkFizzBuzz(3, "Fizz")

def test_5():
    return checkFizzBuzz(5, "Buzz")
    
def test_multiple3():
    return checkFizzBuzz(6, "Fizz")
    
def test_multiple5():
    return checkFizzBuzz(10, "Buzz")

def test_multiple3_5():
    return checkFizzBuzz(15, "FizzBuzz")    
    
print(can_i_call_fizzbuzz())
print(test_1())
print(test_2())
print(test_3())
print(test_5())
print(test_multiple3())
print(test_multiple5())
print(test_multiple3_5())