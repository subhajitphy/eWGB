import numpy as np
import scipy
from scipy.special import jv

def F(e):
	l2=(1+73/24*e**2+37/96*e**4)/((1-e**2)**(7/2))
	return l2
def gp(p,e):
	gpe=p**4/64*((jv(p-2,p*e)-2*e*jv(p-1,p*e)+2/p*jv(p,p*e)
		+2*e*jv(p+1,p*e)-jv(p+2,p*e))+np.sqrt(1-e**2)*
		(jv(p-2,p*e)-2*jv(p,p*e)+jv(p+2,p*e)))**2
	return gpe
def gn(p,e):
	gne=p**4/64*((jv(p-2,p*e)-2*e*jv(p-1,p*e)+2/p*jv(p,p*e)
		+2*e*jv(p+1,p*e)-jv(p+2,p*e))-np.sqrt(1-e**2)*
		(jv(p-2,p*e)-2*jv(p,p*e)+jv(p+2,p*e)))**2
	return gne

def g0(p,e):
	return p**2/24*jv(p,p*e)**2
def g(p,e):
	return np.array([gn(p,e),g0(p,e),gp(p,e)])
def gT(p,e):
	return (gn(p,e)+g0(p,e)+gp(p,e))

def peak_freq(f,e):
	return f*1293/181*(e**(12/19)/(1-e**2)*(1+121/304*e**2)**(870/2299))**(3/2)



