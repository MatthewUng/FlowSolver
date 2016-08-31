from collections import deque

def parse():
    """a - number of color
       n - width of board
       m - height of board"""
    a,n,m = map(int, raw_input().split())
    board = [[ '' for _ in range(n)] for _ in range(m)]
    for i in range(a):
        l = raw_input().split()
        l = [int(x.strip('(,)')) for x in l]
        y,x,Y,X = l
        board[x][y] = str(i)
        board[X][Y] = str(i)
    return board, a


class board:
    def __init__(self, board, a):
        self.heads = dict()
        for i in range(a):
            self.heads[str(i)] = set()
        self.board = board
        for tup in self.getStartHeads():
            self.heads[self.board[tup[0]][tup[1]]].add(tup)
            

    def getStartHeads(self):
        out = list()
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if ord('0') <= ord(self.board[x][y]) <= ord('9'):
                    out.append((x,y))
        return out
                
    def copy(self):
        #TODO: return copy to board object
        pass

    def move(self, color, moveX, moveY):
        if self.board[moveX-1][moveY] == color[0] and moveX > 0:
            self.board[moveX][moveY] = color+"'"
            return True
        elif self.board[moveX][moveY] == color[0] and moveY > 0:
            self.board[moveX][moveY] = color+"'"
            return True
        elif self.board[moveX+1][moveY] == color[0] and moveX < len(self.board):
            self.board[moveX][moveY] = color+"'"
            return True
        elif self.board[moveX][moveY+1]==color[0] and moveY< len(self.board[0]):
            self.board[moveX][moveY] = color+"'"
            return True
        else:
            return False

    def __repr__(self):
        out = ''
        for line in self.board:
            out += line + '\n'
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
