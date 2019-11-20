class Agent:
    def __init__(self, problem):
        self.__problem = problem
        self.__type = "human"

    def getMove(self, problem, program1, program2, order):
        i = input()
        if int(i) not in problem.legalMoves():
            print("Invalid Move. Please enter a number in this range:", problem.legalMoves())
            problem.displayBoard()
            return problem.getMove()
        else:
            return int(i)
