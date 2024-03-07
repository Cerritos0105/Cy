import cv2
#import numpy as np
import matplotlib.pyplot as plt
#Creo la matris principal
img = cv2.imread("kirby.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Extraer los canales R G B
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
#imprimimos los valores de la imagen
print(img)
#comando pro
#R , G, B = cv2.split(img)
#Mostrammos los canales
fig = plt.figure()
#Canal rojo
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R)
ax1.set_title("Rojo pro")
#Canal verde
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G)
ax2.set_title("Verde pro")
#Canal azul
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B)
ax3.set_title("Azul pro")
#Imgaen original
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")
plt.show()
