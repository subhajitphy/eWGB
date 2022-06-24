import numpy as np
from constants import *
from ef import solve_ecc, k
from functions import g, F, peak_freq, gT
#from tqdm import tqdm
from fcutoff import get_f_cutoff


FRACTOL=1e-4


xy=[-2,0,2]
itr=4

def dEdfrQf(f,Mc,eta,n_pts,fi,ff,f0,e0,z):
    if type(f) is np.ndarray:
        return np.array([dEdfrQf(f1,Mc,eta,n_pts,fi,ff,f0,e0,z) for f1 in f])
    M=Mc/(eta**(3/5))
    s1=0
    s,x=[],[]
    fr=f*(1+z)
    fractol=1
    p=1
    while fractol>=FRACTOL:
        phi_p=0
        f_p=fr/p
        e_p=solve_ecc(f0*(1.0+z), e0, f_p)
        phi_p+=gT(p,e_p)/(F(e_p)*p**(2/3))
        fac=1/3*(Mc*c**2/fr)*(2*np.pi*G*Mc*fr/c**3)**(2/3)
        s.append(fac*phi_p)
        s2=s1
        s1+=s[p-1]
        if p==1:
            fractol=1
        else:
            fractol=(s1-s2)/s2
        x.append(fractol)
        p+=1
    return s1



def eval_fe_p(kp,p,fr,e0,f0,M,z):
#     if kp>=0.5:
#         return np.zeros(3), np.zeros(3)
    kpq=[[],[],[]]
    fpq=[[],[],[]]
    freq_pq=[]
    e_pq=[]
    #k_pq=[]
    for d,q in enumerate(xy):
        for i in range(itr):
            if kp<0.5:
                fpq[d].append(fr/(p+q*kp))
                kpq[d].append(k(fpq[d][i],e0,f0,M,z))
                kp=kpq[d][i]
        if kp<0.5:
            freq_pq.append(fpq[d][i])
            e_pq.append(solve_ecc(f0*(1.0+z), e0, fpq[d][i]))
            #k_pq.append(kpq[d]) 
    return freq_pq, e_pq       

def dEdfr_kshifted(Mc,eta,n_pts,fi,f0,e0,z,kcutoff):
    M=Mc/(eta**(3/5))
    sum1,freq=[],[]
    f_arr=np.logspace(np.log10(fi),np.log10(get_f_cutoff(Mc,eta,f0,e0,kcutoff)),n_pts)
    k_arr=[]

    for f in f_arr:
        s1=0
        s,x=[],[]

        fr=f*(1+z)
        K=k(fr,e0,f0,M,z)
        if K>=0.25:
            break
        fractol=1
        p=1
        while fractol>=FRACTOL:
            fp=fr/p
            kp=k(fr/p,e0,f0,M,z)

            phi_nq=0
            f_p,e_p=eval_fe_p(kp,p,fr,e0,f0,M,z)
            if f_p==[]:
                break
            for d,q in enumerate(xy):

                phi_nq+=g(p,e_p[d])[d]/F(e_p[d])*1/p**(2/3)
            fac=1/3*Mc*c**2/fr*(2*np.pi*G*Mc*fr/c**3)**(2/3)
            s.append(fac*phi_nq)
            s2=s1
            s1+=s[p-1]
            if p==1:
                fractol=1
            else:
                fractol=s[p-1]/s2
            p+=1
        sum1.append(s1)
        freq.append(f)
    sum1=np.array(sum1);freq=np.array(freq)
    del_index=np.where(sum1 == 0)[0]
    sum1=np.delete(sum1,del_index)
    freq=np.delete(freq,del_index)
    return np.array(freq), np.array(sum1)


