import numpy as np 
import pickle


sizem, ncore=np.loadtxt('sizearr2.txt').transpose()
sizem=int(sizem)
ncore=int(ncore)

P=np.shape(pickle.load(open('specarr_0.pkl', 'rb')))
specarr=np.zeros((sizem,P[1],P[2],P[3]))




for i in range(ncore):
    specarri=pickle.load(open('specarr_'+str(i)+'.pkl', 'rb'))
    P=np.shape(specarri)
    for i1,i2 in enumerate(range(i*round(sizem/ncore),i*round(sizem/ncore)+P[0])):
        specarr[i2]=specarri[i1]
        


def savearr(A,name):
    file = open(name, 'ab')
    pickle.dump(A,file)
    return file.close()


savearr(specarr,'specarrK.pkl')
