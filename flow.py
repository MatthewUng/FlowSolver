
def parse():
    """a - number of color
       n - width of board
       m - height of board"""
    a,n,m = map(int, raw_input().split())
    print a,n,m
    board = [[ '' for _ in range(n)] for _ in range(m)]
    for i in range(a):
        l = raw_input().split()
        l = [int(x.strip('(,)')) for x in l]
        y,x,Y,X = l
        board[x][y] = str(i)
        board[X][Y] = str(i)
    return board


class board:
    def __init__(self, board):
        this.heads = dict()
        this.board = board

    def getHeads(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):

    def copy(self):
        
print parse()
