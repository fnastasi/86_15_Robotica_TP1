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


def Eul2RMat(phi=0, tita=0,psi=0):
    # los ángulos se pasan a radianes
    phi = phi*pi/180
    tita = tita*pi/180
    psi = psi*pi/180
    
    # Se escriben las matrices de rotación y con la función array se convierten en elementos
    # de numpy
    R_z_phi = [[cos(phi), -sin(phi), 0],[sin(phi), cos(phi), 0],[0,0,1]]
    R_z_phi = array(R_z_phi)
    #print(R_z_phi)
    
    R_y_tita = [[cos(tita), 0, sin(tita)], [0,1,0] , [-sin(tita), 0, cos(tita)]]
    R_y_tita = array(R_y_tita)
    #print(R_y_tita)
    
    R_z_psi = [[cos(psi), -sin(psi), 0],[sin(psi), cos(psi), 0],[0,0,1]]
    R_z_psi = array(R_z_psi)
    #print(R_z_psi)
    
    # Matriz de rotación calculada como el producto de las 3 matrices
    R = linalg.multi_dot([R_z_phi,R_y_tita,R_z_psi])
    # El índice de configuración
    sg_tita = sign(tita)
    return around(R,decimals=5),sg_tita




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
        