from cv2 import cv2
import pytesseract
# import numpy as np

#gives the text from image

pytesseract.pytesseract.tesseract_cmd='C:/Users/LENOVO/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('images/cv3.jpg')

#convert imge to grayscale
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#remove the noise from image 
def remove_noise(image):
    return cv2.medianBlur(image,5)

#thresholding : replacing image pixels with black or white
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY,cv2.THRESH_OTSU)[1]


#try the funcitons on the image 
treated_img = get_grayscale(img) 
treated_img = remove_noise(img) 
treated_img = thresholding(img)

print(ocr_core(img))

