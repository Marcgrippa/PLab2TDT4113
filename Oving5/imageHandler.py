from Oving5 import imager2
from PIL import Image



class ImageHandlerFor2Pictures():

    def __init__(self, img1_filepath, img2_filepath ):
        self.img1_filepath = img1_filepath
        self.img2_filepath = img2_filepath

    def createImage(self):
        self.img1 = imager2.Imager(self.img1_filepath)
        self.img2 = imager2.Imager(self.img2_filepath)


    def resizeImage(self):
        self.img1 = imager2.Imager.resize(self.getSize(), self.getSize())

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size


def run():
    i = ImageHandlerFor2Pictures("images/kdfinger.jpeg", "images/einstein.jpeg")
    i.createImage()
    i.setSize(250)
    i.resizeImage()




run()


