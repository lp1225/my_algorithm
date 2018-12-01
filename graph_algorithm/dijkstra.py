# 迪杰斯特拉搜索 Dijkstra
import heapq
import math


graph = {
    'A': {'B':5, 'C':1},
    'B': {'A':5, 'C':2, 'D':1},
    'C': {'A':1, 'B':2, 'D':4, 'E':8},
    'D': {'B':1, 'C':4, 'E':3, 'F':6},
    'E': {'C':8, 'D':3},
    'F': {'D':6}
}

def init_distance(graph,start):
    distance = {start: 0}
    for vertex in graph:
        if vertex != start:
            # 正无穷大
            distance[vertex] = math.inf 
    return distance

def dijkstra(graph, start):
    """带权最短路径搜索问题"""
    pqueue = []
    heapq.heappush(pqueue, (0, start))
    # 要在队列中弹出才能压人seen中
    seen = set()
    partent = {start: None}
    # 最短距离
    distance = init_distance(graph, start)
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist+graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist+graph[vertex][w], w))
                    partent[w] = vertex
                    distance[w] = dist+graph[vertex][w]

    return partent, distance

partent, distance = dijkstra(graph, 'A')
print(partent)
print(distance)
print()
# 求到F点的最短路径
v = 'F'
while v != None:
    print(v, end=' ')
    v = partent[v]
