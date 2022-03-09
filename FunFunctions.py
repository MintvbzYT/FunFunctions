# FunFunctions v1.7.5 - Released on Mar 9 2022 - Added functions. 

def define(word,definition):
    print('The definition of ' + word + ' is ' + definition +  '.')

def congrats(user,congrat):
    print("Congrats, " + user + " on " + congrat + "!")
    # a silly congratulate function!
    
def say(words):
    print(words)
    # a say function, easy alt for print

def announce(announcement):
    print("!!! " + announcement.upper() + " !!!")
    # an announcement function 

import time
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
    

import os
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
   
import webbrowser
def redirect(webpage):
    webbrowser.open(webpage)
    # opens a webpage
    
import sys
def stop():
    sys.exit("Process ended.")
    # stops the program

import datetime
def date():
   today = datetime.date.today()
   print('The date today is ' + str(today) + ".")
   # prints the current  date.
  
