import os
import time
from datetime import datetime
import random
import string
import re
import numpy as np
from termcolor import colored
from tabulate import tabulate
from class_definition_ecommerce import *

def print_centered(text):
    if len(text) > total_margin:
        print('Not possible to center')
    else:
        left = int(total_margin/2 - len(text)/2)
        print(left * ' ' + text)

def invalid_option():
    print('\n')
    print_centered('Please, type a valid option.')
    time.sleep(1)
    print('\n')

#******************************
#
#       global parameters
#
#******************************

total_margin = 60
identation = 4

#******************************
#
#        global objects
#
#******************************

users = {}
session_shopping_cart = shopping_cart()

#      products creation
random.seed(1)
products_dict = {}
for index in range(1, 9):
    products_dict[index] = product(round(random.uniform(300, 2500), 2), random.randint(5, 50), random.choice([0, 10, 15, 25, 30, 50]))
