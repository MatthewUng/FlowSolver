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
    def __init__(self, board, a, solve = None):
        self.heads = dict()
        self.a = a
        self.colors = set()
        #init colors and heads dictionary
        for i in range(a):
            c = chr(ord('A')+i)
            self.heads[c] = set()
            self.colors.add(c)
        self.board = board
        for tup in self.getStartHeads():
            self.heads[self.board[tup[0]][tup[1]]].add(tup)

        #list of colors that are connected
        if solve:
            self.solve = solve
        else:
            self.solve = set()
            
    def getUnsolved(self):
        return self.colors - self.solve

    def getStartHeads(self):
        out = list()
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if ord('A') <= ord(self.board[x][y]) <= ord('Z'):
                    out.append((x,y))
        return out

    def implementConnection(self, color, connection):
        """implements a connection and returns a new board object"""
        #connection is a list of squares of a particular color
        b = [l[:] for l in self.board]
        for sq in connection[1:-1]:
            b[sq[0]][sq[1]]  = color.lower()
        return board(b, self.a, self.solve|set(color))

    def findConnections(self,color):
        """finds all connections between 2 heads of the same color"""
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


    def connectionCheck(self, connection, color):
        """checks if a connection is valid, True if valid"""
        #connection = [(0,0), ..., (3,4)]
        board = self.board[:]
        for tup in connection:
            board[tup[0]][tup[1]] = color.lower()
        return self.boardCheck(board)
        
    def boardCheck(self, board):
        """returns True if the board is valid and False otherwise"""
        #valid as in can potentially be partially solved

        #empty square can not be adjacent to only 1 empty square
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.board[x][y] == ' ':
                    if self.getAdjacentBoard(x,y,board).count(' ') == 1:
                        return False

        #all heads must be adjacent to an empty square
#        for color,tup in heads.items():
#            adj = self.findAdjacentBoard(tup[0],tup[1],board)
#            if adj.count(' ') + adj.count(color.lower()) == 0:
#                return False
        return True

    def solved(self):
        """returns True if the board is solved"""
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] ==' ':
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
        #queue contains board objects
        self.queue = deque()
        self.queue.append(board)

    def solve(self):
        while len(self.queue) != 0:
            temp = self.queue.popleft()

            #if solution 
            if temp.solved():
                return temp
                break

            
            c = temp.getUnsolved().pop()
            connections = temp.findConnections(c)
            for connection in connections:
                self.queue.append(temp.implementConnection(c,connection))


if __name__ == '__main__':
    stuff = parse()
    b = board(*stuff)
    s = solver(b)
    print s.solve()

