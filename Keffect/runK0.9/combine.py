import numpy as np 
import pickle


sizem, ncore=np.loadtxt('sizearr.txt').transpose()
sizem=int(sizem)
ncore=int(ncore)

P=np.shape(pickle.load(open('dEdfr_1.pkl', 'rb')))
dEdfr=np.zeros((sizem,P[1],P[2],P[3]))
freq=np.zeros((sizem,P[1],P[2],P[3]))



for i in range(ncore):
    dEdfri=pickle.load(open('dEdfr_'+str(i)+'.pkl', 'rb'))
    freqi=pickle.load(open('freq_'+str(i)+'.pkl', 'rb'))
    P=np.shape(dEdfri)
    for i1,i2 in enumerate(range(i*round(sizem/ncore),i*round(sizem/ncore)+P[0])):
        dEdfr[i2]=dEdfri[i1]
        freq[i2]=freqi[i1]
        


def savearr(A,name):
    file = open(name, 'ab')
    pickle.dump(A,file)
    return file.close()


savearr(dEdfr,'dEdfrK.pkl')
savearr(freq,'freqK.pkl')