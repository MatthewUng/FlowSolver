from parsePhoto import *
from flow import *


if __name__ == '__main__':
    name = raw_input("Name of file: ")
    i = ImageParser(name)
    b = board(*i.parse())
    s = solver(b)
    print s.solve()
