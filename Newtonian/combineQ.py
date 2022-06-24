import numpy as np 
import pickle
import sys
import os

# src_dir = os.getcwd()



sizem, ncore=np.loadtxt('sizearr.txt').transpose()
sizem=int(sizem)
ncore=int(ncore)
P=np.shape(pickle.load(open('bigarrQ_1.pkl', 'rb')))
bigarr=np.zeros((sizem,P[1],P[2]))


for i in range(ncore):
    bigarri=pickle.load(open('bigarrQ_'+str(i)+'.pkl', 'rb'))
    P=np.shape(bigarri)
    for i1,i2 in enumerate(range(i*round(sizem/ncore),i*round(sizem/ncore)+P[0])):
        bigarr[i2]=bigarri[i1]
        


def savearr(A,name):
    file = open(name, 'ab')
    pickle.dump(A,file)
    return file.close()


savearr(bigarr,'bigarrQ.pkl')
