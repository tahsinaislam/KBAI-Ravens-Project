from PIL import ImageChops
from PIL import Image
import numpy as np
import cv2

img1 = Image.open('C:\dev\KBAI-Ravens-Project\A.png')
img2 = Image.open("C:\dev\KBAI-Ravens-Project\B.png")

img = cv2.imread('C:\dev\KBAI-Ravens-Project\A.png')
img1= cv2.imread('C:\dev\KBAI-Ravens-Project\B.png')
img2 = cv2.imread("C:\dev\KBAI-Ravens-Project\C.png")

  
# counting the number of pixels
number_of_white_pix = np.sum(img == 255)
number_of_black_pix = np.sum(img == 0)
ratio = np.sum(img == 0)/np.sum(img)
ratio2 = np.sum(img1 == 0)/np.sum(img1)
ratioC = np.sum(img2 == 0)/np.sum(img2)
avg = 1-(ratioC/(ratio+ratio2))

if (abs(1-(ratioC/(ratio+ratio2)))<0.06):
    print(True)

print(np.array_equal(img1,img))
  
print('Number of white pixels:', ratio, ratio2, ratioC)
print('Number of black pixels:', avg)