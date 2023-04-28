import cv2
import numpy as np
img = cv2.imread("erigido.jpg")
cv2.imshow("original", img)
altura, largura, bytesPorPixel = np.shape(img)
print("Original Altura: ", altura, "Largura: ", largura)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
altura, largura = np.shape(gray)
print ("Gray Altura: ", altura, "Largura: ", largura)

gray_wh = cv2.resize(gray, (300,300), interpolation = cv2.INTER_AREA)
cv2.imshow("Resize_wh", gray_wh)
altura, largura = np.shape(gray_wh)
print ("Resize: 300x300 Altura: ", altura , "Largura: ", largura)

gray_percent = cv2 .resize(gray, (0,0), None, 0.50, 0.50 )
cv2.imshow("Resize_%", gray_percent)
altura, largura = np.shape(gray_percent)
print ("Resize %: 50% Altura: ", altura,"Largura: ", largura)

cv2.waitKey()
cv2.destroyAllWindows()

