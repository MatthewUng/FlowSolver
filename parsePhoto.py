from PIL import Image
import os

class ImageParser:
    #(0,0,0) is black
    #outline color
    #(123,123,63)
    
    def __init__(self, filename):
        self.name = filename
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.array = self.toArray(Image.open(self.directory+ '\\' + filename))

    def parse(self):
        pass
    

    def toArray(self, image):
        #size = (w,h)
        data = list(image.getdata())
        size = image.size
        out = list()
        for i in range(size[1]):
            out.append(data[size[0]*i:size[0]*(i+1)])
        return out

    def save(self):
        self.image.save(self.directory+r"\test\{}".format(os.path.basename(self.name)))

    def show(self):
        self.image.show()
        
    def mode(self):
        return self.image.mode



if __name__ == '__main__':
    #(1440, 2560)  width x height
    directory = os.path.dirname(os.path.realpath(__file__))
    image = Image.open(directory+'\\'+r'\test\7x7v1.png')
    size = image.size
    

