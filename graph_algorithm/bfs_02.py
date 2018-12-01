# BFS最短路径问题
# 构建存储了上一个节点位置消息的partent节点

def BFS_MIN(graph, start):
    """最短路径问题， 树的结构"""
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start:None}
    # 开始BFS搜索
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
    return parent


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
    }
    partent = BFS_MIN(graph, 'A')
    print(partent)
    print()
    # 查询最短路径
    v = 'E'
    while v != None:
        print(v)
        v = partent[v]
