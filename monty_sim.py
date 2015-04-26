# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:31:24 2013

Author: DD Tran

On n'a pas tous les jours 20 ans. 
Ca nous arrive une fois seulement 
"""

import numpy as np 
from montyhall import * 

if __name__ == "__main__":
    N = 50000
    guesses = simulate_guesses(N)
    prizes = simulate_prizedoor(N)
    goats = goat_door(guesses, prizes)
    new_guesses = switch(guesses, goats)
    
    diff = guesses - prizes 
    new_diff = new_guesses - prizes 
    
    inds1 = np.where(diff == 0)[0]
    inds2 = np.where(new_diff == 0)[0]
    
    print "not switching :" 
    print len(inds1)
    
    print "switching :" 
    print len(inds2)