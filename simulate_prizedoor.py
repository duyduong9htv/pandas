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
    answer = np.floor(3*np.random.random((nsim, 1)))
    
    return answer 