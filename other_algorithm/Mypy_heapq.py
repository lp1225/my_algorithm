# heapq是提供了小根堆来维护实现优先级队列的
import heapq

q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# queue.PriorityQueue
from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while q.empty() == False:
    next_item = q.get()
    print(next_item)
