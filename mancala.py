import random
import argparse
import time
import importlib
import signal
import os
import sys

try:
    signal.SIGALRM
except Exception as ex:
    print("ERROR: " + str(ex))
    print("WARNING: Timeouts will not be enforced.")
    
import heuristicminimax
from util.timeout import *

class Mancala:
    '''Represents the game Mancala.'''
    _default_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def __init__(self):
        '''Initializes the game with an empty board.'''      
        self._board = Mancala._default_board[:]
        self.__turn = 1
        
    def displayBoard(self):
        print("Play Mancala!")
        print("")
        print("Score | Player One | Player Two")
        print("        {0: >10} | {1: >10}".format(
            self.score()[0], self.score()[1]))
        print(self.getState())
        print("Player {0}'s Turn".format(self.getTurn()))

    def getState(self):
        '''Returns the state of the game (as a string).'''
        result = '    {0: >2} {1: >2} {2: >2} {3: >2} {4: >2} {5: >2}\n'.format(
            self._board[0], self._board[1], self._board[2],
            self._board[3], self._board[4], self._board[5])
        result += ' {0: >2}                   {1: >2} \n'.format(
            self._board[13], self._board[6])
        result += '    {0: >2} {1: >2} {2: >2} {3: >2} {4: >2} {5: >2}'.format(
            self._board[12], self._board[11], self._board[10],
            self._board[9], self._board[8], self._board[7])
        return result

    def setState(self, state):
        '''Takes a state (as returned by getState) and sets the state of the game.'''
        rows = state.split("\n")
        player1_holes = rows[0].split()
        score_holes = rows[1].split()
        player2_holes = rows[2].split()
        newBoard = []
        for i in range(len(player1_holes)):
            newBoard.append(int(player1_holes[i]))
        newBoard.append(int(score_holes[0]))
        for i in range(len(player2_holes)):
            newBoard.append(int(player2_holes[i]))
        newBoard.append(int(score_holes[1]))
        self._board = newBoard
        if self.isTerminal():
            self.__turn = 2

    def getSuccessors(self, state):
        '''Takes a state and returns the possible successors as 4-tuples: (next state, action to get there, whose turn in the next state, final score). For the last two items, see getTurn() and finalScore().'''
        currentState = self.getState()
        succ = []
        self.setState(state)
        for a in self.legalMoves():
            self.move(a)
            succ.append((self.getState(), a, self.getTurn(), self.finalScore()))
            self.setState(state)
        self.setState(currentState)
        return succ

    def legalMoves(self):
        '''Returns the set of legal moves in the current state (a move is a column index).'''
        legalMoves = []
        if self.__turn == 1:
            for i in range(6):
                if self._board[i] != 0:
                    legalMoves.append(i)
            return legalMoves
        elif self.__turn == -1:
            for i in range(6):
                if self._board[i+7] != 0:
                    legalMoves.append(i+7)
            return legalMoves
    
    def own_zone(idx, player):
        """True if index is in (boolean True == 1) player's zone"""
        if player:
            return idx <= 5 and idx >= 0
        else:
            return idx >= 7 and idx <= 12
    
    def move(self, idx):
        """Perform a move action on a given index, based on the current player"""
        # Illegal move if empty hole
        if self._board[idx] == 0:
            raise ValueError("No stones in hole")
        # # Illegal move if score hole chosen ... not really necessary but keep
        # # for now
        # something about legal moves
        if idx not in self.legalMoves():
            raise ValueError("Please choose from a move", self.legalMoves())
            
        # Calculate stones in chosen hole
        count = self._board[idx]

        self._board[idx] = 0
        current_idx = idx

        # While still stones to move
        while count > 0:
            current_idx = (current_idx + 1) % len(self._board)
            if self.__turn is 1 and current_idx == 13:
                continue
            if (self.__turn is not 1) and current_idx == 6:
                continue
            self._board[current_idx] += 1
            count -= 1  # one less stone to move

        # Capture rule
        if(self._board[current_idx] == 1 and self._board[12 - current_idx] >= 1 and
           Mancala.own_zone(current_idx, self.__turn is 1)):
            if((self._board[12 - current_idx] != sum(self._board[0:6]) and self.__turn is not 1) or
               ((self._board[12 - current_idx] != sum(self._board[7:13]) and self.__turn is 1))):
                extra_stones = 1 + self._board[12 - current_idx]
                self._board[12 - current_idx] = 0
                self._board[current_idx] = 0
                if self.__turn is 1:
                    self._board[6] += extra_stones
                else:
                    self._board[13] += extra_stones

        if self.side_empty():
            self._board[6] += sum(self._board[0:6])
            self._board[13] += sum(self._board[7:13])
            self._board[0:6] = [0, 0, 0, 0, 0, 0]
            self._board[7:13] = [0, 0, 0, 0, 0, 0]
        # If last stone ends in score go again
        if current_idx is not 6 and self.__turn is 1:
            self.__turn = -1
        elif current_idx is not 13 and self.__turn is -1:
            self.__turn = 1
                        
    def finalScore(self):
        '''If the game is not over, returns None. If it is over, returns -1 if min won, +1 if max won, or 0 if it is a draw.'''        
        if not self.over():
            return None
        else:
            if self.score()[0] > self.score()[1]:
                return -1
            if self.score()[0] < self.score()[1]:
                return 1
            else:
                return 0

    def score(self):
        """Returns the current score of the Mancala"""
        return Mancala.score_board(self._board)
    
    @staticmethod
    def score_board(board):
        """Scores a Mancala board"""
        return (board[6], board[13])
    
    def over(self):
        """True if the Mancala is over"""
        return self.side_empty() or self._board[6] >= 25 or self._board[13] >= 25

    def side_empty(self):
        """True is either player's side is empty of stones."""
        stones_left_01 = sum(self._board[0:6])
        stones_left_02 = sum(self._board[7:13])
        return stones_left_01 == 0 or stones_left_02 == 0

    def isTerminal(self):
        '''Returns true if the game is over and false otherwise.'''
        return self.finalScore() != None

    def getStones(self, idx):
        '''Returns the contents of the board at the given position ("X" for max, "O" for min, and "." for empty). NOTE: row 0 is the BOTTOM of the board.'''
        count = self._board[idx]
        return count

    def getTurn(self):
        '''Determines whose turn it is. Returns 1 for max, -1 for min, or 2 if the state is terminal.'''
        return self.__turn
    
    def __str__(self):
        '''Returns a string representing the board (same as getState()).'''
        return self.getState()
    
    def getMove(self):
        '''Allows the user to click to decide which column to move in.'''
        i = input()
        if int(i) not in self.legalMoves():
            print("Invalid Move. Please enter a number in this range:", self.legalMoves())
            self.displayBoard()
            return self.getMove()
        else:
            return int(i)


class DefaultMoveOrder:
    def __init__(self, problem):
        self.__problem = problem

    def getSuccessors(self, state):
        return self.__problem.getSuccessors(state)

def playMancala(problem, initState, players, playerPrograms, numTrials, swaps, testDefault):
    wins = [0, 0, 0]
    times = [0, 0]
    turns = [0, 0]
    nodes = [0, 0]
    defaultNodes = [0, 0]
    defaultOrder = DefaultMoveOrder(problem)
    for i in range(swaps):
        for t in range(numTrials):
            problem.setState(initState)
            while not problem.isTerminal():
                problem.displayBoard()
                turn = problem.getTurn()
                playerIdx = (1 - turn)//2
                playerIdx = (playerIdx + i)%2
                if players[playerIdx] == "random":
                    move = random.choice(problem.legalMoves())
                elif players[playerIdx] == "human":
                    move = problem.getMove()
                else: #minimax
                    startT = time.time()
                    try:
                        with timeout(2):
                            move, numNodes = heuristicminimax.getMove(problem.getState(), problem.getTurn(), 4, playerPrograms[playerIdx][0], playerPrograms[playerIdx][1])
                            nodes[playerIdx] += numNodes
                            endT = time.time()
                            times[playerIdx] += endT - startT
                            turns[playerIdx] += 1

                        if not tournament and testDefault[playerIdx]:
                            moveD, numNodesD = heuristicminimax.getMove(problem.getState(), problem.getTurn(), 4, playerPrograms[playerIdx][0], defaultOrder)
                            defaultNodes[playerIdx] += numNodesD

                    except TimeoutError:
                        print(players[playerIdx] + " timed out after 2 seconds. Choosing random action.")
                        move = random.choice(problem.legalMoves())
                problem.move(move)              
    
            if problem.finalScore() == 0:
                whoWon = "Draw"
                wins[2] += 1
            elif problem.finalScore() < 0:
                whoWon = players[(1+i)%2] + " wins!"
                wins[(1+i)%2] += 1
            elif problem.finalScore() > 0:
                whoWon = players[(0+i)%2] + " wins!"
                wins[(0+i)%2] += 1

            if swaps == 2:
                whoWon = players[(0+i)%2] + " vs. " + players[(1+i)%2] + " game " + str(t+1) + ": " + whoWon
            print(whoWon)
    return wins, times, turns, nodes, defaultNodes
    
def main():
    parser = argparse.ArgumentParser(description='Play Mancala with computer or human players.')
    parser.add_argument('-p1', '--player1', type=str, default='random', help='the name of a Python file containing a MancalaAgent, or "random" or "human" (default: random)')
    parser.add_argument('-p2', '--player2', type=str, default='random', help='the name of a Python file containing a MancalaAgent, or "random" or "human" (default: random)')
    parser.add_argument('-t', '--trials', type=int, help='plays TRIALS games, then swaps the players and plays TRIALS more games (has no effect if either player is human; with this option the game will not be displayed)')
    parser.add_argument('-d1', '--default1', action='store_true', default=False, help='measures nodes expanded by Player 1 with the default move order during the game (has no effect with -r)')
    parser.add_argument('-d2', '--default2', action='store_true', default=False, help='measures nodes expanded by Player 2 with the default move order during the game (has no effect with -r)')
    
    args = parser.parse_args()

    problem = Mancala()   
    initState = problem.getState()

    players = [args.player1, args.player2]

    if args.trials != None:
        swaps = 2
        numTrials = args.trials
    else:
        swaps = 1
        numTrials = 1

    if args.player1 == "human" or args.player2 == "human":
        swaps = 1
        numTrials = 1

    if swaps == 2:
        random.seed(42)
        
    playerPrograms = [None, None]
    for i in range(2):
        if players[i] != "random" and players[i] != "human":
            mod = importlib.import_module(".".join(players[i].split("/")[-1].split(".")[:-1]))
            with timeout(2):
                    leafEval = mod.MancalaHeuristicEval(problem)
                    order = mod.MancalaOrderHeuristic(problem)
                    playerPrograms[i] = (leafEval, order)
              
    defaultOrder = [args.default1, args.default2]
    wins, times, turns, nodes, defaultNodes = playMancala(problem, initState, players, playerPrograms, numTrials, swaps, defaultOrder)
            
    if swaps == 2:
        print("Stats:")
        print(players[0] + " wins: " + str(wins[0]))
        print(players[1] + " wins: " + str(wins[1]))
        print("Draws: " + str(wins[2]))
        
    for i in range(2):
        if turns[i] > 0:
            print(players[i] + ":\n  " + str(times[i]/turns[i]) + " seconds per step, on average")
            if not args.tournament:
                if defaultOrder[i]:
                    print("  " + str(defaultNodes[i]/turns[i]) + " nodes expanded per step, on average, using the default move order")
                print("  " + str(nodes[i]/turns[i]) + " nodes expanded per step, on average, using the order heuristic")
            
if __name__ == "__main__":
    main()
