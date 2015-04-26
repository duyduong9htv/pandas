# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:42:54 2013

Author: DD Tran

On n'a pas tous les jours 20 ans. 
Ca nous arrive une fois seulement 
"""
import numpy as np 

A = np.random.rand(3, 3)
B = np.eye(3)
D = np.random.rand(3, 1)
C= A*B

print A, B, C


D1= B*D #element wise product 
D2 = np.dot(B, D) #use dot for matrix multiplication 


print D, D2


#can also use matrix instead of array 

x = np.arange(0, 3, 1)
x1 = np.mat(x) #convert x to matrix type 

np.shape(x)
np.shape(x1) 

# in matrix format can simply do multiplication a la Matlab 


#==============================================================================
# append to a matrix 
#==============================================================================

a1 = np.random.rand(1, 3) #np.shape(a1) should give (1, 3) as a tuple 
dim_a1 = np.shape(a1)
dim_a1[0]
dim_a1[1]

b1 = np.random.rand(2, 3)

c1 = np.append(a1, b1) #do not specify any axis to append, everything is flattened out 
c2 = np.append(a1, b1, axis = 0)

np.shape(c1)
np.shape(c2)


