def isLowPoint(graph, i : int, j : int):
    if i > 0 and graph[i-1][j] <= graph[i][j]:
        return False
    if j > 0 and graph[i][j-1] <= graph[i][j]:
        return False
    if i+1 < len(graph) and graph[i+1][j] <= graph[i][j]:
        return False
    if j+1 < len(graph[i]) and graph[i][j+1] <= graph[i][j]:
        return False
    return True

def fileToGraph(path : str):
    graph = []
    with open(path) as file:
        for l in file.readlines():
            graph.append([])
            for c in l:
                if c != '\n':
                    graph[-1].append(int(c))
    return graph

def getRisk(graph):
    risk = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if isLowPoint(graph,i,j):
                risk += graph[i][j] + 1
    return risk

# Test Cases:
if __name__ == "__main__":
    print("--------------------------------- TC1 ---------------------------------")
    tg1 = [[2,1,9,9,9,4,3,2,1,0], [3,9,8,7,8,9,4,9,2,1], [9,8,5,6,7,8,9,8,9,2], [8,7,6,7,8,9,6,7,8,9], [9,8,9,9,9,6,5,6,7,8]]
    assert getRisk(tg1) == 15, "Failed test 1"
    print("--------------------------------- TC2 ---------------------------------")
    tg2 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    assert getRisk(tg2) == 4, "Failed test 2"
    print("--------------------------------- TC3 ---------------------------------")
    tg3 = [[9, 9, 9], [9, 9, 9], [9, 9, 8]]
    assert getRisk(tg3) == 9, "Failed test 3a"
    tg3 = [[9, 9, 9], [9, 9, 8], [9, 9, 9]]
    assert getRisk(tg3) == 9, "Failed test 3b"
    tg3 = [[9, 9, 9], [8, 9, 9], [9, 9, 9]]
    assert getRisk(tg3) == 9, "Failed test 3c"
    tg3 = [[9, 9, 9], [9, 9, 9], [8, 9, 9]]
    assert getRisk(tg3) == 9, "Failed test 3d"
    tg3 = [[9, 9, 8], [9, 9, 9], [9, 9, 9]]
    assert getRisk(tg3) == 9, "Failed test 3e"
    print("--------------------------------- TC4 ---------------------------------")
    tg4 = [[9, 9, 9], [9, 8, 9], [9, 9, 9]]
    assert getRisk(tg4) == 9, "Failed test 4"
    print("--------------------------------- TC5 ---------------------------------")
    tg5 = [[9, 8, 7], [9, 9, 9], [9, 9, 9]]
    assert getRisk(tg5) == 8, "Failed test 5"
    # Final case
    print("------------------------------- PUZZLE --------------------------------")
    g2 = fileToGraph("Day09/input.txt")
    print(getRisk(g2))