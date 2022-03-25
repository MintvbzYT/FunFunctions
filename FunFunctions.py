# Fun Functions v2.0 - Released on Mar 25, 2022 - New look + added functions!
# Get easy updates at https://github.com/MintvbzYT/FunFunctions

############### Word Functions #################

def uppercase(word):
    word = word.upper()
    print(word)
    # uppercases the desired word
    
def lowercase(word):
    word = word.lower()
    print(word)
    # lowercases the desired word
    
def define(word,definition):
    print('The definition of ' + word + ' is ' + definition +  '.')
    
    
############### Time Functions #################

import time
def wait(wait_time):
    time.sleep(wait_time)
    # an easy solution to time.sleep
    
import datetime
def date():
   today = datetime.date.today()
   print('The date today is ' + str(today) + ".")
   # prints the current  date

############### Number Functions #################

def count_letters(word):
    print("There are " + str(len(word)) + " letters in your word.")
    # this will count the letters in a word and print the value.
    
def count_to(number_to_count):
    num = 0
    while num < number_to_count:
        wait(1)
        num += 1
        print(num)
    # a function that counts to a number from zero
    
############### Important Functions #################

import sys
def stop():
    sys.exit("Process ended.")
    # stops the program
    
import webbrowser
def redirect(webpage):
    webbrowser.open(webpage)
    # opens a webpage
    
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    # clears the console of all prints
    
############### FUN FUNCTIONS #################

def ask(prompt):
    answer = input(prompt)
    # a simple ask and receive answer function
    
def fancy_word(word):
    for letter in word:
        word = [{letter}]
        print(word)
    # a fancy way to print a word
    
def congrats(user,congrat):
    print("Congrats, " + user + " on " + congrat + "!")
    # a silly congratulate function!
    
def say(words):
    print(words)
    # a say function, easy alt for print
 
def announce(announcement):
    print("!!! " + announcement.upper() + " !!!")
    # an announcement function 

###########################################
# Update log
#v2.0 - Released on Mar 25, 2022 - Organized functions and changed the looks.
# v1.7.5 - Released on Mar 9, 2022 - Fixed some issues and organized funcitions
# v1.5 - Released on Mar 9, 2022 - Added Functions
# v1.2 - Released on Mar 8, 2022 - Fixed bugs and added functions
# v1.0 - Released on Mar 7, 2022 - First release.
