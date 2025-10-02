def bfs(graph, initial, visit, queue):
    visit.add(initial)
    queue.append(initial)
    while queue:
        edge = queue.pop(0)
        print(edge)
        for n in graph[edge]:
            if n not in visit:
                visit.add(n)
                queue.append(n)
    return visit

if __name__ == "__main__":
    graph = {
        'A':['B','C'],
        'B':['A','D','E'],
        'C':['A','F'],
        'D':['B'],
        'E':['B','F'],
        'F':['C','E']        
    }

    visit = set()
    queue = []
    bfs(graph, 'A', visit, queue)