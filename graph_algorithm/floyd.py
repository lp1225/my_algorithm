# 弗洛伊德最短路径问题
import math

inf = math.inf
graph = [
    [0, 2, 6, 4],
    [inf, 0, 3, inf],
    [7, inf, 0, 1],
    [5, inf, 12, 0]
]

def Floyd(graph, s, e):
    """弗洛伊德算法"""
    end = len(graph[0])
    for k in range(end):
        for i in range(end):
            for j in range(end):
                # 更新经过i点的最短路径
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]
    # 查看最短路劲
    print(graph[s-1][e-1])

    return graph
    
print(type(inf))
print(graph)
print('-----------------------------')
g = Floyd(graph,4, 3)
print(g)
