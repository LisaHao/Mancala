import queue

class MancalaHeuristicEval:
    def __init__(self, problem):
        self.__problem = problem
        ###If you want to do any pre-processing, do it here
        ###(note: time limit for the constructors is 2 seconds!)

    def eval(self, state):
        '''Gives a heuristic evaluation of the given state.'''
        '''Gives a heuristic evaluation of the given state.'''
        curState = self.__problem.getState()
        self.__problem.setState(state)

        board = self.__problem._board
        eval = 0
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

        # want to prioritize actions that make the biggest score difference
        value -= scoreDifference
        return value
