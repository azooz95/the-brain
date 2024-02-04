import cv2 as cv

import sys
sys.path.append("../../the brain")

from image_handler import ImageHandler

class ImageInfoExtractor():
    
    
    @staticmethod
    def text_extractor(info):
        text = ''
        for idx in range(len(info)):
            res = info[idx]
            for line in res:
                text+=line[-1][0]

        return text
    
    @classmethod
    def run(cls, img_path):
        img = ImageHandler.read_img(img_path)
        info = ImageHandler().img2txt(img)
        text = cls.text_extractor(info)
        return text
    

if __name__ == "__main__":
    img_path = '../data/sample_img.jpeg'
    print(ImageInfoExtractor.run(img_path))