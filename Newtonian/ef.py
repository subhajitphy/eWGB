from constants import *
import numpy as np



#######################################################################
def A(a, b, e):
    return ( 1 + (a * e**(18/19) * (1 - e**2)**(-3/2) * (304 + 121*e**2)**(1305/2299)) )**(-b)

def alpha(e):
    return e**(18/19) * (1-e**2)**(-3/2) * (304+121*e**2)**(1305/2299)

def alphaprime(e):
    return (3 * (96 + 292*e**2 + 37*e**4)) / (e**(1/19) * (1 - e**2)**(5/2) * (304 + 121*e**2)**(994/2299))

def freq_from_ecc(f0, e0, e):
    return f0 * alpha(e0) / alpha(e)

def solve_ecc(f0, e0, f, eps=1e-15, prn=False):  
    if f0==f:
    	return e0
    a = 0.036516381909547736
    b = 0.7767738693467336
    chi = (f0/f) * alpha(e0)
    X = (1 + a*chi)**(-b)
    
    e_prv = -1 
    e_now = A(a, b, X)
    
    niter = 0
    
    while abs(e_now - e_prv) > eps:
        e_prv = e_now
        e_now = e_now - (alpha(e_now) - chi)/alphaprime(e_now)
        niter += 1
    
    if prn:
        print("Number of iterations = ", niter)
    
    return e_now
      
#############################################################
def k(f,e0,f0,M,z_0):
    return 3/(1-solve_ecc(f0*(1.0+z_0),e0,f)**2)*(2*np.pi*G*M*f/c**3)**(2/3)
##############################################################

