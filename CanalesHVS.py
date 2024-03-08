import cv2
#import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("kirby.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imghvs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V= cv2.split(imghvs)
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(H, cmap="gray")
ax1.set_title("H")

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(S, cmap="gray")
ax2.set_title("S")

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(V, cmap= "gray")
ax3.set_title("V")

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")
plt.show()