import numpy as np
from constants import *
from functions import g, F, peak_freq, gT
from ef import solve_ecc, k
from scipy import integrate
from numpy import log10 as lg
from compute_hc import dEdfrQf

sizef=20;sizem=80;sizez=80;

# FRACTOL=1e-4

# def dEdfrQf(f,Mc,eta,n_har,n_pts,fi,ff,f0,e0,z):
#     if type(f) is np.ndarray:
#         return np.array([dEdfrQf(f1,Mc,eta,n_har,n_pts,fi,ff,f0,e0,z) for f1 in f])
#     M=Mc/(eta**(3/5))
#     s1=0
#     s=np.zeros(n_har+1)
#     fr=f*(1+z)
#     for p in range(1,n_har+1):
#         phi_p=0
        
#         f_p=fr/p
#         e_p=solve_ecc(f0*(1.0+z), e0, f_p)
#         phi_p+=gT(p,e_p)/(F(e_p)*p**(2/3))
#         fac=1/3*(Mc*c**2/fr)*(2*np.pi*G*Mc*fr/c**3)**(2/3)
#         s[p]=fac*phi_p
#         s1+=s[p]
#     return s1


# def dEdfrQf(f,Mc,eta,n_pts,fi,ff,f0,e0,z):
#     if type(f) is np.ndarray:
#         return np.array([dEdfrtest(f1,Mc,eta,n_pts,fi,ff,f0,e0,z) for f1 in f])
#     M=Mc/(eta**(3/5))
#     s1=0
#     s,x=[],[]
#     fr=f*(1+z)
#     fractol=1
#     p=1
#     while fractol>=FRACTOL:
#         phi_p=0
#         f_p=fr/p
#         e_p=solve_ecc(f0*(1.0+z), e0, f_p)
#         phi_p+=gT(p,e_p)/(F(e_p)*p**(2/3))
#         fac=1/3*(Mc*c**2/fr)*(2*np.pi*G*Mc*fr/c**3)**(2/3)
#         s.append(fac*phi_p)
#         s2=s1
#         s1+=s[p-1]
#         if p==1:
#             fractol=1
#         else:
#             fractol=(s1-s2)/s2
#         x.append(fractol)
#         p+=1
#     return s1


e0=0.9
q=1
fi=1e-9
ff=1e-7
f0=1e-9
n_har=200
n_pts=100
eta=q/(1+q)**2




Mstar=1e8*MS
zstar=2
z1=0.2
z2=5

farr=np.logspace(lg(fi),lg(ff),sizef)
Mcarr=np.logspace(6,10,sizem)*MS
zarr=np.linspace(z1,z2,sizez)

Y=np.zeros((len(Mcarr),len(zarr),len(farr)))


for i in range(len(Mcarr)):
    for j in range(len(zarr)):
        print(i,j)
        for k in range(len(farr)):
            Y[i][j][k]=dEdfrQf(farr[k],Mcarr[i],eta,sizef,fi,ff,f0,e0,zarr[j])
    



import pickle

bigarr_file = open('bigarrQ.pkl', 'ab')

pickle.dump(Y,bigarr_file)

bigarr_file.close()
