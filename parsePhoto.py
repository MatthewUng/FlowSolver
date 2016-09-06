from math import sqrt
from PIL import Image
import os

class ImageParser:
    #(0,0,0) is black
    #outline color
    outline = (123,123,63)
    
    def __init__(self, filename):
        self.name = filename
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.image = Image.open(self.directory+ '\\' + filename) 
        #width x height (w,h)
        self.size = self.image.size
        self.array = self.toArray(self.image)


    def parse(self):
        """parses the data array"""
        out = list()
        gamerows = self.parserows()
        partitions = self.parseColumns(gamerows[0])

        for gamerow in gamerows:
            out.append(self.sepRow(gamerow, partitions))
        return self.colorParse(out)

    def colorParse(self, data):
        """parses a matrix of RGB tuples"""
        count = 0
        d = dict()
        l = list()
        c = ord('A')
        for x in range(len(data)):
            for y in range(len(data[0])):
                if data[x][y]:
                    if data[x][y] in l:
                        data[x][y] = d[data[x][y]]
                    else:
                        l.append(data[x][y])
                        d[data[x][y]] = chr(c)
                        data[x][y] = d[data[x][y]]
                        c += 1
                        count += 1
                else:
                    data[x][y] = ' '
        return data, count

    def sepRow(self, gamerow, partitions):
        """takes a gamerow and a list of partitions to return a list of objects"""
        out = list()
        start = None
        for tup in partitions:
            if start == None:
                start = tup
                continue
            square = [x[start[1]:tup[0]] for x in gamerow]
            start = tup
            out.append(self.parseSquare(square))

        return out

    def parseSquare(self, square):
        h = len(square)
        w = len(square[0])

        centerX = len(square)/2
        centerY = len(square[0])/2
        radius = int(min(len(square), len(square[0]))*.30)

        color = square[centerX][centerY]


        #color can't be black
        if color == (0,0,0): return False

        for x in range(len(square)):
            for y in range(len(square[0])):
                xdist = abs(x-centerX)
                ydist = abs(y-centerY)
                if xdist**2 + ydist**2 < radius**2:
                    if square[x][y] != color:
                        return False
        return color

    def parseColumns(self, gamerow):
        """parses the gamerow to find where the columns are"""
        out = list()
        start, end = None, None

        for i in range(len(gamerow[0])):
            if self.columnCheck(gamerow, i):
                if start == None:
                    start = i
            else:
                end = i-1
                if start != None:
                    out.append([start,end])
                    start = None

        if start != None:
            out.append([start, end])
        
        return out

    def parserows(self):
        """parses the rows of the image array"""
        firstrow = (False, None)
        secondrow = (False, None)
        gamerows = list()
        start, end = None, None
    
        for i in range(len(self.array)):
            secondrow = firstrow
            firstrow = self.rowCheck(i)

            #below barrier
            if secondrow[0] and not firstrow[0]:
                start = firstrow[1]

            #above barrier
            elif firstrow[0] and not secondrow[0]:
                end = firstrow[1]
                if start and end:
                    thing = self.array[start:end]
                    gamerows.append(thing)

        return gamerows

    def columnCheck(self, gameRow, i):
        """checks if the collumn i in a given is part of the partition"""
        for j in range(len(gameRow)):
            if gameRow[j][i] != ImageParser.outline:
                return False
        return True

    def rowCheck(self, i):
        """checks if a row i is part of the partition between squares"""
        #row is list of tuples
        #row represents a row of pixels of a photo
        row = self.array[i]
        if row.count(ImageParser.outline) > self.size[0]/2:
            return (True, i)
        else: return (False,i)

    def toArray(self, image):
        """converts the list of pixel values to a more useable matrix format"""
        #size = (w,h)
        data = list(image.getdata())
        size = image.size
        out = list()
        for i in range(size[1]):
            out.append(data[size[0]*i:size[0]*(i+1)])
        return out

    def save(self, name=None):
        if not name:
            self.image.save(self.directory+r"\test\{}".format(os.path.basename(self.name)))
        else:
            print "not implemented yet"

    def show(self):
        self.image.show()
        
    def mode(self):
        return self.image.mode

    def test(self):
    #TODO: for testing purposes
        thing, count = self.parse()
        print count
        for row in thing:
            print row
       
        return 
        thing = self.parse()
        data = [x[:] for x in self.array]
        for i in range(len(data)):
            for tup in thing:
                for j in range(tup[0], tup[1]+1):
                    data[i][j] = (256,256,256)
        out = list()
        for row in data:
            out.extend(row)
        self.image.putdata(out)
        self.image.show()
        
def photo(matrix):
    """takes a matrix and shows the respective image"""
    h,w = len(matrix), len(matrix[0])
    i = Image.new('RGB', (w,h))
    data = list()
    for row in matrix:
        data.extend(row)
    i.putdata(data)
    i.show()

if __name__ == '__main__':
    #(1440, 2560)  width x height
    i = ImageParser(r'photos\10x10v1.png')
    i.test()
