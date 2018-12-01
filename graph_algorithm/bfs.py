# BFS 广度优先遍历

#    graph = {
#        'A': ['B', 'C'],
#        'B': ['A', 'C', 'D'],
#        'C': ['A', 'B', 'D'],
#        'D': ['B', 'C', 'E', 'F'],
#        'E': ['C', 'D', 'F'],
#        'F': ['D']
#    }

def BFS(graph, start):
    """广度优先搜索,start为起点"""
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex, end=' ')

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    BFS(graph, 'A')
    print()
    BFS(graph, 'E')
