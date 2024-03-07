import cv2
import numpy as np
import matplotlib.pyplot as plt
#Se genera la imagen
img =100*np.ones((10,10,3), np.uint8)
#Extremos los canales R G Y B
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
#le quitamos valores a la matris roja
#R[:,:]=0
#Se modifica todas la matrices para obtener magenta
R[:,:] = 255
G[:,:] = 0
B[:,:] = 255 
#Modificamos la imagen
img[:,:,0]=R
img[:,:,1]=G
img[:,:,2]=B
print(img)
#Se muestra la imagen 
plt.imshow(img)
plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)