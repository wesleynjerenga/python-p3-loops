#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i)
    print("Happy New Year!")  # Print the final message

def square_integers(int_list):
    return [x ** 2 for x in int_list]  # Return a list of squared integers

def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # Print "FizzBuzz" for multiples of 3 and 5
        elif i % 3 == 0:
            print("Fizz")  # Print "Fizz" for multiples of 3
        elif i % 5 == 0:
            print("Buzz")  # Print "Buzz" for multiples of 5
        else:
            print(i)  # Print the number if no other condition is met
