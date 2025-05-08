#!/usr/bin/env python3

from looping import happy_new_year, square_integers, fizzbuzz

import io
import sys

class TestHappyNewYear:
    '''happy_new_year() in looping.py'''

    def test_prints_10_to_1_hny(self):
        '''prints 10 to 1 countdown then "Happy New Year!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        happy_new_year()
        sys.stdout = sys.__stdout__
        answer = captured_out.getvalue()
        
        #answer.split(\n) produces a list that ends in ''
        answer_list = answer.split('\n')
        #second to last value should be the HNY string
        assert answer_list[-2] == "Happy New Year!", "Your final line does not match 'Happy New Year!', check spelling/capitalization!"
        digit_strings = [str(i) for i in range(1,11)]
        remaining_digits = [i for i in digit_strings if i not in answer_list] 
        assert remaining_digits == [], f"You didn't print all digits 1-10, missing {', '.join(remaining_digits)}"

class TestSquareIntegers:
    '''square_integers() in looping.py'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        assert(square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25])
        assert(square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25])

import io
import sys
from lib.looping import fizzbuzz  # Ensure fizzbuzz is imported from the correct module

class TestFizzBuzz:
    def test_prints_1_to_100_fizzbuzz(self):
        '''prints 1 to 100 with fizz 3s, buzz 5s, fizzbuzz 3and5s'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fizzbuzz()  # Call the fizzbuzz function
        sys.stdout = sys.__stdout__
        output = captured_out.getvalue().strip().split("\n")
        
        # Validate the output
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                assert output[i - 1] == "FizzBuzz"
            elif i % 3 == 0:
                assert output[i - 1] == "Fizz"
            elif i % 5 == 0:
                assert output[i - 1] == "Buzz"
            else:
                assert output[i - 1] == str(i)