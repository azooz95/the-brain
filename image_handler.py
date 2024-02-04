import cv2 as cv
from PyPDF2 import PdfReader
from paddleocr import PaddleOCR


class ImageHandler():
    
    ocr = PaddleOCR(use_angle_cls=False, lang='en')

    
    def img2txt(self, img):
        return self.ocr.ocr(img, cls=True)
    
    @staticmethod
    def read_img(path):
        return cv.imread(path)