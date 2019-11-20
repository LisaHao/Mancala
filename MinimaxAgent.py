import heuristicminimax
class Agent:
    def __init__(self, problem):
        self.__problem = problem
        self.__type = "human"
        self.__defaultOrder = False
        self.__heuristicEvalClass = DefaultHeuristicEval
        self.__orderHeuristicClass = DefaultOrderHeuristic

    def getMove(self, problem):
        move, numNodes = heuristicminimax.getMove(problem.getState(), problem.getTurn(), 4, self.heuristicEval, self.orderHeuristic)


        return move

    def setDefaultOrder(self, defaultOrder):
        self.__defaultOrder = defaultOrder

class DefaultHeuristicEval:
    def __init__(self, problem):
        self.__problem = problem
        ###If you want to do any pre-processing, do it here
        ###(note: time limit for the constructors is 2 seconds!)

    def eval(self, state):
        '''Gives a heuristic evaluation of the given state.'''

        curState = self.__problem.getState()
        self.__problem.setState(state)

        #####YOUR CODE BEGINS HERE#####
        eval = 0
        ######YOUR CODE ENDS HERE######

        self.__problem.setState(curState)
        return eval


class DefaultOrderHeuristic:
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