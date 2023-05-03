import numpy as np
import math
from skimage import io
import cv2

def umbral(imagen1):
    valor_temporal = np.copy(imagen1)
    ancho = len(valor_temporal)
    largo = len(valor_temporal[0])
    valor_temporal = np.copy(imagen1)
    for i in range(ancho):
        for j in range(largo):

            nuevo_color1 = 128
            color1 = valor_temporal[i,j,0]
            if(color1 < 128):
                nuevo_color1 = 0
            if(color1 > 128):
                nuevo_color1 = 255
            valor_temporal[i,j,0] = nuevo_color1

            nuevo_color2 = 128
            color2 = valor_temporal[i,j,1]
            if(color2 < 128):
                nuevo_color2 = 0
            if(color2 > 128):
                nuevo_color2 = 255
            valor_temporal[i,j,1] = nuevo_color2

            nuevo_color3 = 128
            color3 = valor_temporal[i,j,2]
            if(color3 < 128):
                nuevo_color3 = 0
            if(color3 > 128):
                nuevo_color3 = 255
            valor_temporal[i,j,2] = nuevo_color3
    return valor_temporal

def suma(imagen1, imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(1, largo):
        for j in range(1, ancho):
            color0 = (imagen1[i, j,0] * 0.4) + (imagen2[i, j,0] * 0.6)
            temp[i, j,0] = color0

            color1 = (imagen1[i, j,1] * 0.4) + (imagen2[i, j,1] * 0.6)
            temp[i, j,1] = color1

            color2 = (imagen1[i, j,2] * 0.4) + (imagen2[i, j,2] * 0.6)
            temp[i, j,2] = color2
    return temp

def resta(imagen1, imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(0, largo):
        color = [0, 0, 0]
        for j in range(0, ancho):
            color[0] = imagen1[i, j, 0] * 1 - imagen2[i, j, 0] * 1
            color[1] = imagen1[i, j, 1] * 1 - imagen2[i, j, 1] * 1
            color[2] = imagen1[i, j, 2] * 1 - imagen2[i, j, 2] * 1

            temp[i, j, 0] = abs(color[0])
            temp[i, j, 1] = abs(color[1])
            temp[i, j, 2] = abs(color[2])

    return temp

def multiplicacion(imagen1, imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(1, largo):
        for j in range(1, ancho):
            color0 = imagen1[i, j, 0]*0.4 * imagen2[i, j, 0] * 0.6 / 255
            color1 = imagen1[i, j, 1]*0.4 * imagen2[i, j, 1] * 0.6 / 255
            color2 = imagen1[i, j, 2]*0.4 * imagen2[i, j, 2] * 0.6 / 255

            temp[i, j, 0] = color0
            temp[i, j, 1] = color1
            temp[i, j, 2] = color2
    return temp

def opOR(imagen1,imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(0, largo):
        for j in range(0, ancho):
            color = [0, 0, 0]
            try:
                if (imagen1[i, j, 0] or imagen2[i, j,0]):
                    color[0] = 255
                else:
                    color[0] = 0

                if (imagen1[i, j, 1] or imagen2[i, j,1]):
                    color[1] = 255
                else:
                    color[1] = 0

                if (imagen1[i, j, 2] or imagen2[i, j,2]):
                    color[2] = 255
                else:
                    color[2] = 0

                temp[i, j, 0] = color[0]
                temp[i, j, 1] = color[1]
                temp[i, j, 2] = color[2]
            except Exception:
                continue
    return temp

def opAND(imagen1,imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(0, largo):
        for j in range(0, ancho):
            color = [0, 0, 0]
            try:
                if (imagen1[i, j, 0] and imagen2[i, j,0]):
                    color[0] = imagen1[i, j, 0]

                if (imagen1[i, j, 1] and imagen2[i, j,1]):
                    color[1] = imagen1[i, j, 1]

                if (imagen1[i, j, 2] and imagen2[i, j,2]):
                    color[2] = imagen1[i, j, 2]

                temp[i, j, 0] = color[0]
                temp[i, j, 1] = color[1]
                temp[i, j, 2] = color[2]
            except Exception:
                continue
    return temp

def opXOR(imagen1,imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(0, largo):
        for j in range(0, ancho):
            color = [0, 0, 0]
            try:

                if (imagen1[i, j, 0] or imagen2[i, j,0]):
                    color[0] = 255
                else:
                    color[0] = 0

                if (imagen1[i, j, 1] or imagen2[i, j,1]):
                    color[1] = 255
                else:
                    color[1] = 0

                if (imagen1[i, j, 2] or imagen2[i, j,2]):
                    color[2] = 255
                else:
                    color[2] = 0

                if (imagen1[i, j, 0] and imagen2[i, j,0]):
                    color[0] = 0

                if (imagen1[i, j, 1] and imagen2[i, j,1]):
                    color[1] = 0

                if (imagen1[i, j, 2] and imagen2[i, j,2]):
                    color[2] = 0

                temp[i, j, 0] = color[0]
                temp[i, j, 1] = color[1]
                temp[i, j, 2] = color[2]
            except Exception:
                continue
    return temp

def opNAND(imagen1,imagen2):
    temp = np.copy(imagen1)
    largo = len(temp)
    ancho = len(temp[0])

    for i in range(0, largo):
        for j in range(0, ancho):
            color = [0, 0, 0]
            try:

                if (imagen1[i, j, 0] and not imagen2[i, j,0]):
                    color[0] = imagen1[i, j, 0]

                if (imagen1[i, j, 1] and not imagen2[i, j,1]):
                    color[1] = imagen1[i, j, 1]

                if (imagen1[i, j, 2] and not imagen2[i, j,2]):
                    color[2] = imagen1[i, j, 2]

                temp[i, j, 0] = color[0]
                temp[i, j, 1] = color[1]
                temp[i, j, 2] = color[2]
            except Exception:
                continue
    return temp

def aclarar(imagen):
    return None

def oscurecer(imagen):
    return None

def mejorar(imagen):
    return None
