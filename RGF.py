##Thiis is to practice git and RGF 
import numpy as np
from matplotlitb import pyplot as plt

def Hamiltonian_normal_metal ( m, B, nx, ny, boundary_condition = 'PBC' ):
	H = B*( np.eye(nx*ny, k=1) + np.eye(nx*ny, k=-1) ) + m* np.eye(nx*ny, k=0)	
	if( boundary_condition == 'PBC'):
		H[nx*ny-1,0]= B
		H[0, nx*ny -1]=B	
	return H

def diagonalize_Hamiltonian(H):
	eigen_values, eigen_vect = np.linalg.eig(H)
	return eigen_values, eigen_vect	

