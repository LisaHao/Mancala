import random


class Agent:
    def __init__(self, problem):
        self.problem = problem
        self.turns = 0
    def getMove(self, problem):
        self.turns += 1
        return random.choice(problem.legalMoves())