import time
import random
import heuristicminimax

import sideBiasedAgent
searchDepth = 4
epsilon = 0.25
class Agent(sideBiasedAgent.Agent):
    def getMove(self, problem):
        startT = time.time()
        if (random.uniform(0, 1) > epsilon):
            move, numNodes = heuristicminimax.getMove(problem.getState(), problem.getTurn(), searchDepth, self.heuristicEval(problem), self.orderEval(problem))
        else:
            move, numNodes = random.choice(problem.legalMoves()), 0
        endT = time.time()
        self.timeTaken += endT - startT
        self.nodes += numNodes
        self.turns += 1
        return move

    def __init__(self, problem):
        super().__init__(problem)
        self.problem = problem