import cv2
from sympy import im



img =  cv2.imread('E:\\Visual Cryptograpyh\\input_image\\color_cat.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('E:\\Visual Cryptograpyh\\input_image\\gray_cat.png', img_gray)