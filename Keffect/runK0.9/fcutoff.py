import numpy as np
from ef import solve_ecc
from scipy.optimize import fsolve
from constants import *

# def sigma(e):
#     w=e**(12/19)/(1-e**2)*(1+121/304*e**2)**(870/2299)
#     return w


# def get_e(f,f0,e0):
#     chi=f/f0
#     beta=chi**(2/3)/sigma(e0)
#     w1=((16.83-3.814*beta**.3858)/(16.04+8.1*beta**1.637))
#     return w1

def get_k(Mc,eta,f,f0,e0):
    M=Mc/eta**(3/5)
    e=solve_ecc(f0, e0, f)
    #e=get_e(f,f0,e0)
    x=(2*np.pi*G*M*f/c**3)**(2/3)
    w2=3*x/(1-e**2)
    return w2

def opt_fun_k(Mc,eta,f,f0,e0,kcutoff):
    return (get_k(Mc,eta,f,f0,e0)-kcutoff)


def get_f_cutoff(Mc,eta,f0,e0,kcutoff):
    M=Mc/eta**(3/5)
    f0=fsolve(lambda f: opt_fun_k(Mc,eta,f,f0,e0,kcutoff),1e-7)[0]
    
    return f0