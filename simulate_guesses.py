# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:38:37 2013

Author: DD Tran

On n'a pas tous les jours 20 ans. 
Ca nous arrive une fois seulement 
"""

"""
Function
--------
simulate_guess

Return any strategy for guessing which door a prize is behind. This
could be a random strategy, one that always guesses 2, whatever.

Parameters
----------
nsim : int
    The number of simulations to generate guesses for

Returns
-------
guesses : array
    An array of guesses. Each guess is a 0, 1, or 2

Example
-------
>>> print simulate_guess(5)
array([0, 0, 0, 0, 0])
"""
import numpy as np 

def simulate_guesses(nsim):
    answer = np.floor(3*np.random.random((nsim, 1)))
    
    return answer 
    