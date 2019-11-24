import time

import heuristicminimax

searchDepth = 4
class MinimaxAgent:
    class MancalaHeuristicEval:
        def __init__(self, problem):
            self.problem = problem

        def eval(self, state):
            return 0

    class MancalaOrderHeuristic:
        def __init__(self, problem):
            self.problem = problem

        def getSuccessors(self, state):
            curState = self.problem.getState()
            self.problem.setState(state)

            #####YOUR CODE BEGINS HERE#####
            successors = self.problem.getSuccessors(state)
            ######YOUR CODE ENDS HERE######

            self.problem.setState(curState)
            return successors
    def __init__(self, problem):
        self.problem = problem
        self.heuristicEval = self.MancalaHeuristicEval
        self.orderEval = self.MancalaOrderHeuristic
        self.nodes = 0
        self.turns = 0
        self.timeTaken = 0

    def getMove(self, problem):
        startT = time.time()
        move, numNodes = heuristicminimax.getMove(problem.getState(), problem.getTurn(), searchDepth, self.heuristicEval(problem), self.orderEval(problem))
        endT = time.time()
        self.timeTaken += endT - startT
        self.nodes += numNodes
        self.turns += 1
        return move

class Agent(MinimaxAgent):
    class MancalaHeuristicEval:
        def __init__(self, problem):
            self.__problem = problem
            ###If you want to do any pre-processing, do it here
            ###(note: time limit for the constructors is 2 seconds!)

        def eval(self, state):
            return 0
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