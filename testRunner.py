import importlib

import mancala

numTrials = 20
def play(program1, program2, name1, name2):

    problem = mancala.Mancala()
    initState = problem.getState()
    agent1 = program1.Agent(problem)
    agent2 = program2.Agent(problem)
    defaultOrder = []

    totalwins = [0, 0]
    swaps = 2
    wins, times, turns, nodes, defaultNodes = mancala.playMancala(problem, initState, [name1, name2], [agent1, agent2],
                                                          numTrials, swaps, defaultOrder, toPrint=False)
    return wins, times, nodes, turns

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
    programNames = ["randomAgent.py", "endScoreAgent.py", "perfectStonesAgent.py", "scoredStonesAgent.py",
                   "scoredStonesMoveAgent.py", "sideBiasedAgent.py",
                   "sideBiasedMoveAgent.py", "sideBiasedRandomMoveAgent.py",
                    "eminimaxAgent.py"]
    programList = []
    results = []
    timeResults = []
    nodeResults = []
    for name in programNames:
        program = importlib.import_module(".".join(name.split("/")[-1].split(".")[:-1]))
        programList.append(program)
        results.append([name])
        timeResults.append([name])
        nodeResults.append([name])

    for i in range(len(programList)):
        for j in range(i + 1, len(programList)):
            wins, times, nodes, turns = play(programList[i], programList[j], programNames[i], programNames[j])
            results[i].append(str(wins[0]) + "-" + str(wins[1]) + "-"+ str(wins[2]))
            timeResults[i].append(str(int(round(times[0]))) + "-" + str(int(round(times[1]))))
            nodeResults[i].append(str(int(round(nodes[0] / max(turns[0], 1)))) + "-" + str(int(round(nodes[1]/turns[1]))))
            print("finished trial " +str(i) + "-" + str(j))
    print("scores:")
    printResults(results, programNames)
    print("times:")
    printResults(timeResults, programNames)
    print("nodes:")
    printResults(nodeResults, programNames)



if __name__ == '__main__':
    main()