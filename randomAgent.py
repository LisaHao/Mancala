import random


class Agent:
    def __init__(self, problem):
        self.problem = problem
    def getMove(self, problem):
        return random.choice(problem.legalMoves())