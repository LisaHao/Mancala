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
        action = random.choice(problem.legalMoves())
        print(action)
        #####YOUR CODE BEGINS HERE#####
        return action