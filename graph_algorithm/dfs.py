# 深度优先搜索 DFS

def DFS(graph, start):
    """深度优先搜索,start为起点"""
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
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
    DFS(graph, 'A')
    print()
    DFS(graph, 'E')
