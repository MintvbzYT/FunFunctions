# FunFunctions v1.2 - Released on Mar 8 2022 - Added Count Letters and Ask Function

import time
import os
answer = ""

def say(words):
    print(words)
    # a say function, easy alt for print

def announce(announcement):
    print("!!! " + announcement.upper() + " !!!")
    # an announcement function 

def wait(wait_time):
    time.sleep(wait_time)
    # an easy solution to time.sleep
    
def count_to(number_to_count):
    num = 0
    while num < number_to_count:
        wait(1)
        num += 1
        print(num)
    # a function that counts to a number from zero
    


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    # clears the console of all prints

def uppercase(word):
    word = word.upper()
    print(word)
    # uppercases the desired word
    
def lowercase(word):
    word = word.lower()
    print(word)
    # lowercases the desired word
    
def fancy_word(word):
    for letter in word:
        word = [{letter}]
        print(word)
    # a fancy way to print a word
    
def count_letters(word):
    print("There are " + str(len(word)) + " letters in your word.")
    # this will count the letters in a word and print the value.

def ask(prompt):
    answer = input(prompt)
    # a simple ask and receive answer function


    

    
    
    
    

