
def doTheStuffOnTHefile(path : str):
    graph = None
    lines = 0
    with open(path) as file:
        for l in file.readlines():
            if graph is None:
              graph = [0 for x in range(len(l.strip()))]
            if len(l) < len(graph):
              continue
            lines += 1
            for i in range(len(graph)):
                if l[i] == '1':
                    graph[i] += 1
    gamma = []
    epsilon = []
    print(graph)
    for c in graph:
        if c >= lines / 2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(gamma)
    print(epsilon)
    print(lines)
    g = int("".join(str(x) for x in gamma),2)
    e = int("".join(str(x) for x in epsilon),2)
    print(g*e)

if __name__ == "__main__":
    print("--------------------------------- TC1 ---------------------------------")
    doTheStuffOnTHefile("Day03/input.txt")