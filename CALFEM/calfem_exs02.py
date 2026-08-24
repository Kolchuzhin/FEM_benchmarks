#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 
@author: Jan
# 02.04.2026 rev.0.1

https://github.com/CALFEM/calfem-python
pip install calfem-python

run: python calfem_exs02
the example from the CALFEM manual exs2.py: one dimensional heat flow
https://calfem-python-bagus.readthedocs.io/en/latest/examples/exs2.html
"""
# Physical model:
# 3-layers wall
#                   0.07m   0.10m   0.10m
#                 o-------o-------o-------o
#         To=-17C |   1   |   2   |   3   | Ti=20C
#   R=0.04 m^2K/W o-------o-------o-------o R=0.13 m^2K/W
#                 
# thermal conductivity lambda1=1.7W/mK  
# thermal conductivity lambda2=0.04/mK
# thermal conductivity lambda3=1.7W/mK
#                        
# FEM model:
# dof == temperature
#
#    BC:     1    2       3       4       5    6  BC:
#    T1=-17 >o----o-------o-------o-------o----o< T6=20
#              ke1   ke2     ke3  ^   ke4   ke5
#                                 |
#                                  q4 (heat source)

import numpy as np
import calfem.core as cfc
 #import calfem.vis as cfv
 #import calfem.utils as cfu
 #import calfem.shapes as cfs
 #import calfem.solver as cfslv 

# mesh topology
#Edof = array([])
Edof = np.array([[1, 2],[2, 3],[3, 4],[4, 5],[5, 6]])
#print(Edof)

K = np.zeros((6, 6))
F = np.zeros((6, 1)) 

# load
F[4-1] = 10         # heat source at node 4

# material properties 
ep1 = 1.0/0.04      # spring stiffnesses =        A/R, W/K
ep2 = 1.7/0.070     # spring stiffnesses = lambda*A/L, W/K
ep3 = 0.040/0.100   # spring stiffnesses = lambda*A/L, W/K
ep4 = 1.7/0.100     # spring stiffnesses = lambda*A/L, W/K
ep5 = 1.0/0.13      # spring stiffnesses =        A/R, W/K

# spring element matrices 2x2: spring1e
ke1 = cfc.spring1e(ep1)
ke2 = cfc.spring1e(ep2)
ke3 = cfc.spring1e(ep3)
ke4 = cfc.spring1e(ep4)
ke5 = cfc.spring1e(ep5)
#print(ke1)

# global matrix assembly
cfc.assem(Edof[0, :], K, ke1)   
cfc.assem(Edof[1], K, ke2)
cfc.assem(Edof[2, :], K, ke3)
cfc.assem(Edof[3], K, ke4)
cfc.assem(Edof[4, :], K, ke5)
print("Stiffness matrix K:\n")
print(K,"\n")

# boundary condition
bc = np.array([1, 6])
bcVal = np.array([-17.0, 20.0])

# solution
u, r = cfc.solveq(K, F, bc, bcVal)  # {u}={F}/[K]
print("nodal temperature:\n",u,"\n")
print("reaction forces:\n",r,"\n")