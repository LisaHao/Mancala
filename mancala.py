class Mancala:
    def __init__(self):
        self.totalHoles = 14
        self.board = []
        self.initBoard()
        self.turn = 0 # 0 = left, 1 = right

    # the ends are the stores (left and right) and the middle is the holes. bottom holes first, CCW
    #  OOOOOO
    # X       Y
    #  EEEEEE
    #
    #XEEEEEEYOOOOOO
    #0123456789ABCD
    #6->8, 5->7..
    def initBoard(self):
        board = [0]  # X
        for i in range(6):  # E
            board.append(4)
        board.append(0)  # Y
        for i in range(6):  # O
            board.append(4)
        self.board = board

    def move(self, position):
        turn = self.turn
        storePositions = [0, 7]
        enemyTurn = 1 - turn
        stones = self.board[position]
        self.board[position] = 0
        placementPosition = position

        while (stones > 0):
            placementPosition += 1
            placementPosition %= self.totalHoles
            if (placementPosition != storePositions[enemyTurn]):
                print(placementPosition)
                self.board[placementPosition] += 1
                stones -= 1
        if (self.board[placementPosition] == 1):
            oppositePosition = self.getOppositePosition(placementPosition)
            if (self.board[oppositePosition] != 0):
                extraStones = 1 + self.board[oppositePosition]
                self.board[placementPosition] = 0
                self.board[oppositePosition] = 0
                self.board[storePositions[turn]] += extraStones

        if placementPosition != storePositions[turn]:
            self.changeTurn()

    def getOppositePosition(self, position):
        return 2 * self.totalHoles - position

    def changeTurn(self):
        self.turn = 1 - self.turn

    def printBoard(self):
        holes = self.totalHoles
        halfHoles = holes//2
        print(self.reverse(str(self.board[halfHoles + 1:])))
        print(str(self.board[0]) + "  " * halfHoles + str(self.board[halfHoles]))
        print(self.board[1:halfHoles])

    def reverse(self, string):
        string = string[::-1]
        return string


