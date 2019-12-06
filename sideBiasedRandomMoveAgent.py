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

            #####YOUR CODE BEGINS HERE#####
            # You should take a look at connectfour.py to see what methods self.__problem has, but here are some that will probably be helpful:
            # get/setState()
            # getTurn() -- returns a number indicating whose turn it is in the current state: -1 for min, 1 for max, 2 if the state is terminal
            # getSuccessors(state) -- returns the successors of the given state as 4-tuples: (next state, action to get there, whose turn it is in that state, the final score)
            # getTile(row, col) -- returns the contents of the given position on the board ("X" for max, "O" for min, "." for empty)
            # getHeights() -- returns a list of the heights of the stacks in the 7 columns
            scorePositions = [6, 13]
            board = self.__problem._board
            player1StoneScore = 0
            player2StoneScore = 0
            for i in range (0, scorePositions[0]):
                player1StoneScore += board[i] / 2
            player1StoneScore += board[scorePositions[0]]
            for i in range (scorePositions[0] + 1, scorePositions[1]):
                player2StoneScore += board[i] / 2
            player2StoneScore += board[scorePositions[1]]
            if (player1StoneScore + player1StoneScore == 0):
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
            orderedSuccessors = []
            # utilize a priority queue to return successor who most likely has the best value
            q = queue.PriorityQueue()
            for successor in successors:
                # if it's a win, put as first successor to enqueue
                if successor[3] != None:
                    q.put([-500, successor])
                # else, compute the value of the successor and put in priority queue
                else:
                    value = self.compute_value(successor)
                    q.put([value, successor])
            orderedSuccessors = []
            while not q.empty():
                orderedSuccessors.append(q.get()[1])
            successors = orderedSuccessors
            ######YOUR CODE ENDS HERE######
            self.__problem.setState(curState)
            return successors

        def compute_value(self, successor):
            value = 0
            action = successor[1]
            problem = self.__problem
            board = problem._board
            # want to prioritize earlier actions first
            value -= action%6
            scoreDifference = board[6] - board[13]
            value += random.choice([-2, -1, 0, 1, 2])
            return value

    def __init__(self, problem):
        super().__init__(problem)
        self.problem = problem
        self.heuristicEval = self.MancalaHeuristicEval
        self.orderEval = self.MancalaOrderHeuristic