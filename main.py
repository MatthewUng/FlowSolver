from parsePhoto import *
from flow import *


if __name__ == '__main__':
    i = ImageParser()
    b = board(*i.parse())
    s = solver(b)
    print s.solve()
