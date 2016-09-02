from PIL import Image
import os

class ImageParser:
    #(0,0,0) is black
    #(104, 169, 66)
    def __init__(self, filename):
        self.name = filename
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.image = Image.open(self.directory+ '\\' + filename)

    def parse(self):
        pass

    def save(self):
        self.image.save(self.directory+r"\test\{}".format(os.path.basename(self.name)))

    def show(self):
        self.image.show()
        
    def mode(self):
        return self.image.mode



if __name__ == '__main__':
    l = [ [(104,169,66) for _ in range(100)]for _ in range(100)]    



