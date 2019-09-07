#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:39:11 2019

@author: franco
"""


# In[]
# Se importa la biblioteca numpy para aplicar operaciones similares a como se usan en matlab
from numpy import *

# In[]

"""
Eul2RMat es la función que resuelve el problema directo de los ángulos de Euler
Los parámetros de entrada son los ángulos tita, phi y psi
Ejemplo de como utilizar la función para phi = 45°, tita = 45° y psi =0° :
    (R,sg_tita) = Eul2RMat(phi =45,tita=45,psi=0 )
"""

def Eul2RMat(phi=0, tita=0,phi=0):
    return R,sg_tita


# In[]
    """
RMat2Eul es la función que resuelve el problema inverso de los ángulos de Euler
Los parámetros de entrada son la matriz de rotación R, el indice de configuración, y 
el ángulo phi actual
Ejemplo de como utilizar la función para una matriz de rotación R_rot, indice de
configuración, ind_conf y un ángulo actual ang_act
    ang_euler = RMat2Eul(R = R_rot, sg_tita = ind_conf, phi_act = ang_act )
"""
def RMat2Eul(R=eye(3),sg_tita = 1,phi_act = 0):
    return
        