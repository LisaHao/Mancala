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
        turn = self.__problem.getTurn()
        perfectPlayer1Stones = 0
        perfectPlayer2Stones = 0
        for i in range(0, 6):
            if board[i] == 6 - i:
                perfectPlayer1Stones += 1
        for i in range(7, 13):
            if board[i] == 1 + i%6:
                perfectPlayer2Stones += 1
        if perfectPlayer1Stones + perfectPlayer2Stones == 0:
            eval = 0
        else:
            eval = perfectPlayer1Stones - perfectPlayer2Stones / (perfectPlayer1Stones+perfectPlayer2Stones)
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
