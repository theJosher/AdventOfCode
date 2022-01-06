from collections import deque
import heapq

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

    
def appendNeighbors(graph, i : int, j : int, q):
    if i > 0:
        q.append((i-1,j))
    if j > 0:
        q.append((i,j-1))
    if i+1 < len(graph):
        q.append((i+1,j))
    if j+1 < len(graph[i]):
        q.append((i,j+1))

def fileToGraph(path : str):
    graph = []
    with open(path) as file:
        for l in file.readlines():
            graph.append([])
            for c in l:
                if c != '\n':
                    graph[-1].append(int(c))
    return graph


def findBasins(graph):
    h = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if isLowPoint(graph,i,j):
                v = 0
                seen = set()
                q = deque()
                q.append((i,j))
                while len(q) > 0:
                    n = q.popleft()
                    x = n[0]
                    y = n[1]
                    if graph[x][y] < 9 and not (x,y) in seen:
                        graph[x][y] = graph[i][j]
                        v += 1
                        appendNeighbors(graph,x,y,q)
                        seen.add((x,y))
                print(v)
                heapq.heappush(h,v)
    if(len(h)<3):
        print("Oh shit, there weren't enough blah")
    l = heapq.nlargest(3,h)
    return l[0] * l[1] * l[2]

# Test Cases:
if __name__ == "__main__":
    print("--------------------------------- TC1 ---------------------------------")
    tg1 = [[2,1,9,9,9,4,3,2,1,0], [3,9,8,7,8,9,4,9,2,1], [9,8,5,6,7,8,9,8,9,2], [8,7,6,7,8,9,6,7,8,9], [9,8,9,9,9,6,5,6,7,8]]
    assert findBasins(tg1) == 1134, "Failed test 1"
    # Final case
    print("------------------------------- PUZZLE --------------------------------")
    g2 = fileToGraph("Day09/input.txt")
    print(findBasins(g2))