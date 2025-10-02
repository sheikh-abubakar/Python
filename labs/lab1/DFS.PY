def dfs(graph, initial, visit):
    visit.add(initial)
    print(initial)
    for neighbor in graph[initial]:
        if neighbor not in visit:
            dfs(graph, neighbor, visit)
    return visit
if __name__ == "__main__": 
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    visit = set()
    dfs(graph, 'A',visit)