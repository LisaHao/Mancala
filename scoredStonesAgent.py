import queue
import random
from minimaxAgent import MinimaxAgent

class Agent(MinimaxAgent):
    class MancalaHeuristicEval:
        def __init__(self, problem):
            self.__problem = problem
            ###If you want to do any pre-processing, do it here
            ###(note: time limit for the constructors is 2 seconds!)

        def eval(self, state):
            '''Gives a heuristic evaluation of the given state.'''
            curState = self.__problem.getState()
            self.__problem.setState(state)

            board = self.__problem._board
            stonePlayer1Score = 0
            perfectPlayer1Stones = 0
            confirmedPlayer1Stones = 0
            stonePlayer2Score = 0
            perfectPlayer2Stones = 0
            confirmedPlayer2Stones = 0
            confirmedPlayer1Stones += board[6]
            confirmedPlayer2Stones += board[13]
            for i in range(0, 6):
                stonePlayer1Score += board[i]
                if board[i] == 6 - i:
                    perfectPlayer1Stones += 1
            for i in range(7, 13):
                stonePlayer2Score += board[i]
                if board[i] == 1 + i%6:
                    perfectPlayer2Stones += 1
            eval = (stonePlayer1Score - stonePlayer2Score) + 3*(perfectPlayer1Stones - perfectPlayer2Stones) + 5*(confirmedPlayer1Stones - confirmedPlayer2Stones) / 100
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
    def __init__(self, problem):
        super().__init__(problem)
        self.problem = problem
        self.heuristicEval = self.MancalaHeuristicEval
        self.orderEval = self.MancalaOrderHeuristic