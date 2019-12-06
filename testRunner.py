import importlib

import mancala

def play(program1, program2, name1, name2):
    numTrials = 10
    problem = mancala.Mancala()
    initState = problem.getState()
    agent1 = program1.Agent(problem)
    agent2 = program2.Agent(problem)
    defaultOrder = []

    totalwins = [0, 0]
    swaps = 2
    wins, times, turns, nodes, defaultNodes = mancala.playMancala(problem, initState, [name1, name2], [agent1, agent2],
                                                          numTrials, swaps, defaultOrder, toPrint=False)
    return wins

def printResults(results, programNames):
    tab= " \t"
    for i in range(len(programNames)):
        print(str(i) + ":" + programNames[i] + tab, end ="")
    print("")
    print(tab, end="")
    for i in range(1, len(programNames)):
        print(str(i) + tab, end ="")
    print("")
    for i in range(len(results)):
        print(str(i) + (i + 1)* tab, end ="")
        for j in range(1, len(results[i])):
            print(results[i][j] + tab, end ="")
        print("")

def main():
    x = 4
    programNames = ["endScoreAgent.py", "randomAgent.py", "scoredStonesAgent.py",
                   "scoredStonesMoveAgent.py", "sideBiasedAgent.py",
                   "sideBiasedMoveAgent.py", "sideBiasedRandomMoveAgent.py"]
    programList = []
    results = []
    for name in programNames:
        program = importlib.import_module(".".join(name.split("/")[-1].split(".")[:-1]))
        programList.append(program)
        results.append([name])

    for i in range(len(programList)):
        for j in range(i + 1, len(programList)):
            wins = play(programList[i], programList[j], programNames[i], programNames[j])
            results[i].append(str(wins[0]) + "-" + str(wins[1]) + "-"+ str(wins[2]))
            print("finished trial " +str(i) + "-" + str(j))
    printResults(results, programNames)



if __name__ == '__main__':
    main()