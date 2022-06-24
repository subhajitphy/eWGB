import numpy as np
from scipy.interpolate import interp1d
from constants import *
from numpy import log10 as lg
from scipy.integrate import simps
import sys
import os
import shutil
import numpy as np
import re
import pickle
from tqdm import tqdm


def savearr(A,name):
    file = open(name, 'ab')
    pickle.dump(A,file)
    return file.close()

dEdfr=pickle.load(open('multicore/dEdfrK.pkl', 'rb'))
freq=pickle.load(open('multicore/freqK.pkl', 'rb'))


sizem=np.shape(dEdfr)[0]
sizeg=np.shape(dEdfr)[1]
sizez=np.shape(dEdfr)[2]
sizef=np.shape(dEdfr)[3]

fi=1e-9
ff=10**(-6.5)
f0=1e-9


Mc1=1e6*MS;Mc2=1e10*MS
Mstar=1e8*MS
zstar=2
z1=0.02
z2=5
eta1=0.08
eta2=0.25

dn0=1e-4*Mpc**(-3)/Gyr
H0=70*1e3/(Mpc)

farr=np.logspace(lg(fi),lg(ff),sizef)
Mcarr=np.logspace(lg(Mc1/MS),lg(Mc2/MS),sizem)*MS
zarr=np.linspace(z1,z2,sizez)
etaarr=np.linspace(eta1,eta2,sizeg)

def comoving_density_AN(Mc,z):
    dzdt=(1+z)*np.sqrt(0.3*(1+z)**3+0.7)
    w=((1+z)**2*np.exp(-Mc/Mstar)*np.exp(-z/zstar))/dzdt
    allf=w/Mc*dn0/H0
    return allf

fnew=np.logspace(-9,-7,sizef)
specarr=np.zeros((sizem,sizeg,sizez,sizef))

for i in range(sizem):
    print(i,)
    for i2 in range(sizeg):
        for j in range(sizez):
            for l in range(sizef):

                del_index=np.where(dEdfr[i][i2][j] == 0)[0]
                if len(del_index)>=sizef-5:
                    break
                um1=np.delete(dEdfr[i][i2][j],del_index)
                um2=np.delete(freq[i][i2][j],del_index)
                m=Mcarr[i];z=zarr[j]
                um=comoving_density_AN(m,z)*um1/um2*4*G/(np.pi*c**2)

                f2= interp1d(um2,um, fill_value='extrapolate')

                specarr[i][i2][j][l]=f2(fnew[l])

savearr(specarr,'specarr.pkl')
