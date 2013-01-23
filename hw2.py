# Name:
# Section:
# hw2.py
import math
import random

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

#def f1(x):
    #print x + 1

#def f2(x):
    #return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####

# Test cases for not_equal
##### YOUR CODE HERE #####

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
def roll_dice(sides, amt):
    total = 0
    for i in amt:
        roll = random.randint(1, sides)
        print roll,
        total += roll
        
    print "The total of your dice rolls is", total, "that is all."
        
# Test Cases
quit = False
while not quit:
    sides = int(raw_input("How many sides do the dice you are rolling have?\n"))
    amt = int(raw_input("How many dice will you be rolling this turn?\n"))
    roll_dice(sides, amt)
    quit = raw_input("Please enter 'q' if you would like to quit.")
    if quit.lower() == 'q':
        quit = True
    else:
        quit = False


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
