# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:24:25 2013

Author: DD Tran

On n'a pas tous les jours 20 ans. 
Ca nous arrive une fois seulement 
"""

"""
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
sims : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
"""
import numpy as np 

def simulate_prizedoor(nsim):
    #compute here

    answer = np.floor(3*np.random.random((nsim, 1))) + 1
    
    return answer


def simulate_guesses(nsim):
    answer = 1+ np.floor(3*np.random.random((nsim, 1)))
    
    return answer 
    
def goat_door(guesses, prizes):
#return a door that has no prize, and not hte door that the user guessed 
    nsim = len(guesses)
    answer = []
    for k in range(nsim):
        this_guess = guesses[k]
        this_prize = prizes[k]
        answer1 = []
        for m in range(1, 4):
            if m != this_guess and m != this_prize:
                answer1.append(m)
        M = len(answer1)
        k1 = np.floor(M*np.random.random(1))
        answer.append(answer1[k1])
    return answer        

def switch(guesses, goats):
    nsim = len(guesses)
    new_guesses = a[]
    for k in range(nsim):
        this_guess = guesses[k]
        this_goat = goats[k]
        for m in range(1, 4):
            if m != this_guess and m !=this_goat:
                new_guesses.append(m)
    return new_guesses.T
         
    