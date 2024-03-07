import cv2
#import numpy as np
import matplotlib.pyplot as plt
#Lectura de imagen
#lectura de escala de grices
imgray = cv2.imread('kirby.png', 0)
#Lectura a color
imgRGB = cv2.imread("kirby.png", 1)
#Lectura general 
img = cv2.imread("kirby.png")
#Extre atributos principalesde imgray
tema =imgray.shape
tipo = imgray.dtype
print("Tamaño Gray  | Tipo de dato |", tema, tipo)
#Extrae los atributos principales de imgRGB
temargb = imgRGB.shape
tiporgb = imgRGB.dtype
print("Tamaño RGB  | Tipo de dato |", temargb, tiporgb)
#Correccion de color
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#Se muestra la imgen
cv2.imshow("Gray", imgray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)
#Mostrar
plt.imshow(img)
plt.show()
#Mover con teclado
cv2.waitKey(0)