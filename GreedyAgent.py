import queue
import random

class MancalaGreedyFunction:
    def __init__(self, problem):
        self.__problem = problem 
        ###If you want to do any pre-processing, do it here
        ###(note: time limit for the constructors is 2 seconds!)
        
    def getMove(self, state):
        '''Gives a heuristic evaluation of the given state.'''
        problem = self.__problem
        curState = problem.getState()
        bestAction = random.choice(problem.legalMoves())
        for a in problem.legalMoves():
            if a < 6 and problem.getBoard()[a] == 6 - a:
                bestAction = a
            elif a > 6 and problem.getBoard()[a] == 1 + a%6:
                bestAction = a
        #####YOUR CODE BEGINS HERE#####
        return bestAction