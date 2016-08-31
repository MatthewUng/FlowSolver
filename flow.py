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

def boardCheck(board, heads):
    """board is the board and heads is the set of heads"""
    #empty square must be adjacent to at least two other empty squares/heads
    #all heads must be adjacent to an empty square
    for x in range(len(board)):
        for y in range(len(board[0])):
            if square == ' ':
                emptyCount = 0
                if x > 0 and board[x-1][y] == ' ':
                    emptyCount += 1
                elif y > 0 and board[x][y-1] == ' ':
                    emptyCount += 1
                elif x < len(board) and board[x+1][y] == ' ':
                    emptyCount += 1
                elif y < len(board) and board[x][y+1] == ' ':
                    emptyCount += 1
                if emptyCount < 2:
                    return False
            elif (x,y) in heads:
                

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
                
    def copy(self):
        #TODO: return copy to board object
        pass

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

    def getAdjacent(self, x,y):
        out = list()
        if y > 0:
            out.append(self.board[x][y-1])
        elif x > 0:
            out.append(self.board[x-1][y])
        elif x > len(self.board):
            out.append(
        elif self.board[moveX][moveY+1].upper() == color and \
          moveY< len(self.board[0]):
            self.board[moveX][moveY] = color.lower()
            return True
         

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
    b.move('
