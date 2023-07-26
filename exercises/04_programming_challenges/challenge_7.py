# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:43:11 2023

@author: wooihaw
"""

from random import shuffle, choice

animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot', 'gorilla', 'dolphin', 'snake']

while True:
    answer = choice(animals)
    
    guess = list(answer)
    
    shuffle(guess)
    
    question = ''.join(guess)
    
    ans = input(f"Please guess what animal is {question}: ").lower()
    
    if ans == answer:
        print("You are a genius!")
    else:
        print(f"You are wrong. The answer is {answer}")
    
    res = input("Do you want to play again? ").lower() or 'n'
    
    if res in ('y', 'yes'):
        continue
    print("Bye!")
    break
