import numpy as np
import matplotlib.pyplot as plt
#se genera una imajen en negro
img =  np.zeros((10,10,1), np.uint8)
img[0,1]=30
img[1,2]=50
img[2,3]=100
img[3,4]=200
img[4,5]=255

print(img)
plt.imshow(img, cmap='RGB')
plt.show()