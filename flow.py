from collections import deque

def parse():
    """a - number of color
       n - width of board
       m - height of board"""
    a,n,m = map(int, raw_input().split())
    board = [[ ' ' for _ in range(n)] for _ in range(m)]
    for i in range(a):
        l = raw_input().split()
        l = [int(x.strip('(,)')) for x in l]
        y,x,Y,X = l
        board[x][y] = chr(ord('A')+i)
        board[X][Y] = chr(ord('A')+i)
    return board, a


class board:
    def __init__(self, board, a):
        self.heads = dict()
        for i in range(a):
            self.heads[chr(ord('A')+i)] = set()
        self.board = board
        for tup in self.getStartHeads():
            self.heads[self.board[tup[0]][tup[1]]].add(tup)
            

    def getStartHeads(self):
        out = list()
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if ord('A') <= ord(self.board[x][y]) <= ord('Z'):
                    out.append((x,y))
        return out
                
    def move(self, color, moveX, moveY):
        #color is uppercase
        if self.board[moveX-1][moveY].upper() == color and moveX > 0:
            self.board[moveX][moveY] = color.lower()
            return True
        elif self.board[moveX][moveY].upper() == color and moveY > 0:
            self.board[moveX][moveY] = color.lower()
            return True
        elif self.board[moveX+1][moveY].upper() == color and moveX < len(self.board):
            self.board[moveX][moveY] = color.lower()
            return True
        elif self.board[moveX][moveY+1].upper() == color and \
          moveY< len(self.board[0]):
            self.board[moveX][moveY] = color.lower()
            return True
        else:
            return False


    def findConnections(self,color):
        """finds a connection between 2 heads of the same color"""
        #color is uppercase
        #out would contain all the possible connections
        heads = self.heads[color]
        heads = list(heads)
        start, end = heads[0], heads[1]
        
        out = list()
        visited = list()

        #queue contains possible paths
        queue = deque()
        queue.append([start])
        #sample path = (start, stuff, stuff, stuff, end)
        while len(queue) != 0:
            temp = queue.popleft()
            last = temp[-1]

            #if path is a connection
            if last == end:
                out.append(temp)
                continue
            else:
                for value in self.getAdjacentXY(last[0], last[1]):
                    if self.board[value[0]][value[1]] != ' ': 
                        if value == end:
                            pass
                        else:
                            continue

                    toAdd = temp+[value]
                    #check if similar path is already visited
                    if set(toAdd) in visited:
                        continue
                    else:
                        visited.append(set(toAdd))
                        queue.append(toAdd)
        return out


    def connectionCheck(self, connections):
        #connections is dictionary 
        #connections = {'A':[(0,0), ..., (3,0)], ... }
        board = self.board[:]
        for color, connection in connections.items():
            for tup in connection:
                board[tup[0][tup[1]] = color.lower()
        return self.boardCheck(board)
        
    def boardCheck(self, board):
        """returns True if the board is valid and False otherwise"""
        #empty square can not be adjacent to only 1 empty square
        #all heads must be adjacent to an empty square
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.board[x][y] == ' ':
                    if self.findAdjacentBoard(x,y,board).count(' ') == 1:
                        return False
                elif color,(x,y) in heads.items():
                    adj = self.findAdjacentBoard(x,y,board)
                    if adj.count(' ') + adj.count(color.lower()) == 0:
                        return False
        return True

    def getAdjacentBoard(self, x,y,board):
        """gets adjacent values of a square of a particular board"""
        out = list()
        for tup in self.getAdjacentXY(x,y):
            out.append(board[tup[0]][tup[1]])
        return out

    def getAdjacent(self, x,y):
        """gets adjacent values of a square"""
        out = list()
        for tup in self.getAdjacentXY(x,y):
            out.append(self.board[tup[0]][tup[1]])
        return out
         
    def getAdjacentXY(self, x,y):
        """gets adjacent coords of a square"""
        out = list()
        if y > 0:
            out.append((x,y-1))
        if x > 0:
            out.append((x-1,y))
        if x < len(self.board)-1:
            out.append((x+1, y))
        if y < len(self.board[0])-1:
            out.append((x,y+1))
        return out
        
    def __repr__(self):
        out = ''
        for line in self.board:
            out += str(line) + '\n'
        return out
    
class solver:
    def __init__(self, board):
        stack = deque()
        stack.append(board)

    def solve(self):
        while len(stack) != 0:
            #TODO: solve the problem here lel
            break


if __name__ == '__main__':
    stuff = parse()
    b = board(*stuff)
    print b
    l = b.findConnections('A')
    print len(l)
    f = open('temp', 'w+')
    for path in l:
        f.write(str(path))
        f.write('\n')
