import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
from constants import *
from compute_hc import dEdfr_kshifted

sizea, ncore=np.loadtxt('sizearr.txt').transpose()
sizea=int(sizea)
ncore=int(ncore)

e0=0.9;sizef=40;sizem=sizea;sizez=sizea;sizeeta=sizea


fi=1e-9
ff=10**(-6.5)
f0=1e-9

kcutoff=1/4

Mstar=1e8*MS
zstar=2
z1=0.02
z2=5


farr=np.logspace(lg(fi),lg(ff),sizef)
Mcarr=np.logspace(6,10,sizem)*MS
zarr=np.linspace(z1,z2,sizez)
etaarr=np.linspace(0.08,0.25,sizeeta)

A=np.zeros((len(Mcarr),len(etaarr),len(zarr),len(farr)))
B=np.zeros((len(Mcarr),len(etaarr),len(zarr),len(farr)))


for i in range(sizem):
    
    for j1 in range(sizeeta):
        print(i,j1)
        for j in range(sizez):
            
            Z=dEdfr_kshifted(Mcarr[i],etaarr[j1],sizef,fi,f0,e0,zarr[j],kcutoff)
            
            for k in range(len(Z[0])):
                
                A[i][j1][j][k]=Z[0][k]
                B[i][j1][j][k]=Z[1][k]



import pickle

freq_file = open('freq.pkl', 'ab')
dEdfr_file = open('dEdfr.pkl', 'ab')

pickle.dump(A,freq_file)
pickle.dump(B,dEdfr_file)

freq_file.close()
dEdfr_file.close()
