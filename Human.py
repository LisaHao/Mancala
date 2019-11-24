class Agent:
    def __init__(self, problem):
        self.problem = problem
    def getMove(self, problem):
        print("Enter a move for player " + str(problem.getTurn()))
        i = input()
        if int(i) not in problem.legalMoves():
            print("Invalid Move. Please enter a number in this range:", problem.legalMoves())
            problem.displayBoard()
            return self.getMove(problem)
        else:
            return int(i)