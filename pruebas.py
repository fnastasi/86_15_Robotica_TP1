#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:23:54 2019

@author: franco
"""

# In[]

# Se importa la biblioteca numpy para aplicar operaciones similares a las que se usan en matlab
# Adenás esta biblioteca tiene funciones para cargar datos desde un archivo csv
import numpy as np
# In[]

# Cargo el archivo de prueba con la función loadtxt
file_name = "angulos_prueba.txt"
datos_prueba = np.loadtxt(file_name, delimiter=',', skiprows=1)

# Verificación: Primero se calcula la matrix de rotación y luego se aplica la operación inversa
for ind, Euler_ang in enumerate(datos_prueba):
    phi_act = Euler_ang[0] # Defino phi_actu como el valor de phi que se están probando
    R, ind_conf = Eul2RMat(*Euler_ang) # Calculo la matriz de rotación y el índice de configuración
    
    """
    print("DEBUG")
    print("Línea " + str(ind+2))
    print(Euler_ang)
    print(RMat2Eul(R,ind_conf,phi_act))
    print("\n\n")
    """
    # Verifico si al resolver el problema inverso, se obtiene los mismos ángulos
    Euler_ang_res = RMat2Eul(R,ind_conf,phi_act)
    
    tol = 1e-6
    if ( not np.all(np.abs(Euler_ang_res - Euler_ang)) < tol):
        print("Error para los ángulos que se encuentran en la línea: " + str(ind + 2))
        

# In[]

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html
        
from scipy.spatial.transform import Rotation as Rot

       
# Cargo el archivo de prueba con la función loadtxt
file_name = "angulos_prueba.txt"
datos_prueba = np.loadtxt(file_name, delimiter=',', skiprows=1) 
        
        
for ind, Euler_ang in enumerate(datos_prueba):
    r = Rot.from_euler('ZYZ', Euler_ang, degrees=True)
    R, ind_conf = Eul2RMat(*Euler_ang)
    tol = 1e-6
    if(not np.all(np.abs( R - r.as_dcm() ) < tol)):
        print("Error para los ángulos que se encuentran en la línea: " + str(ind + 2))
