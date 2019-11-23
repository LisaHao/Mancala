import queue
import random

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
        eval = 0
        if board[6] - board[13] != 0:
            eval = board[6] - board[13] / (board[6] - board[13])
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
