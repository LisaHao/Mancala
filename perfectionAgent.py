import heuristicminimax

class Agent:
    def __init__(self, problem):
        self.__problem = problem

    def getMove(self, problem, program1, program2, order):
        #heuristicEval = MancalaHeuristicEval(problem)
        #moveOrderEval = MancalaOrderHeuristic(problem)
        return heuristicminimax.getmove(problem.getState(), problem.getTurn(), program1, program2, order)


class MancalaHeuristicEval:
    def __init__(self, problem):
        self.__problem = problem
        ###If you want to do any pre-processing, do it here
        ###(note: time limit for the constructors is 2 seconds!)

    def eval(self, state):
        '''Gives a heuristic evaluation of the given state.'''

        curState = self.__problem.getState()
        self.__problem.setState(state)

        #####YOUR CODE BEGINS HERE#####
        # You should take a look at connectfour.py to see what methods self.__problem has, but here are some that will probably be helpful:
        # get/setState()
        # getTurn() -- returns a number indicating whose turn it is in the current state: -1 for min, 1 for max, 2 if the state is terminal
        # getSuccessors(state) -- returns the successors of the given state as 4-tuples: (next state, action to get there, whose turn it is in that state, the final score)
        # getTile(row, col) -- returns the contents of the given position on the board ("X" for max, "O" for min, "." for empty)
        # getHeights() -- returns a list of the heights of the stacks in the 7 columns
        scorePositions = [6, 13]
        standardHoleCount = 6
        board = self.__problem._board
        player1StoneScore = standardHoleCount * (standardHoleCount - 1) / 2
        player2StoneScore = standardHoleCount * (standardHoleCount - 1) / 2
        for i in range (0, scorePositions[0]):
            player1StoneScore -= abs(board[i] - (scorePositions[0] - i))
        player1StoneScore += board[scorePositions[0]]
        for i in range (scorePositions[0] + 1, scorePositions[1]):
            player2StoneScore -= abs(board[i] - (scorePositions[1] - i))
        player2StoneScore += board[scorePositions[1]]
        if (player1StoneScore + player2StoneScore == 0):
            eval = 0
        else:
            eval = (player1StoneScore - player2StoneScore) / (player1StoneScore + player2StoneScore)
        ######YOUR CODE ENDS HERE######

        self.__problem.setState(curState)
        return eval


class MancalaOrderHeuristic:
    def __init__(self, problem):
        self.__problem = problem
        ###If you want to do any pre-processing, do it here
        ###(note: time limit for the constructors is 2 seconds!)

    def getSuccessors(self, state):
        curState = self.__problem.getState()
        self.__problem.setState(state)

        #####YOUR CODE BEGINS HERE#####
        successors = self.__problem.getSuccessors(state)
        ######YOUR CODE ENDS HERE######

        self.__problem.setState(curState)
        return successors
