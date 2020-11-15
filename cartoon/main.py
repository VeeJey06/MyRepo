import cv2
from pathlib import Path
import os


class Cartoonize:
    def __init__(self, src, dest):
        self.img = cv2.imread(src)

    def convert(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        color = cv2.bilateralFilter(self.img, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        cv2.imwrite(dest + os.sep + "output.png", cartoon)
        # cv2.imshow("ss", cartoon)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    src = r"C:\Users\SManigan\Pictures\IMG_20201010_053403_690.jpg"
    dest = r"C:\Users\SManigan\Pictures"
    c = Cartoonize(src, dest)
    c.convert()
