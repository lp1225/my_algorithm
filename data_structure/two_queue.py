# ywo queue to stack
import queue


class ArrayQueue(object):

    def __init__(self):
        self.queue1 = queue.Queue(5)
        self.help = queue.Queue(5)

    def push(self, data):
        """模仿压栈"""
        if self.queue1.full() == True:
            raise RuntimeError('the stack is full')
        self.queue1.put(data)

    def pop(self):
        """模仿弹栈"""
        if self.queue1.empty():
            raise RuntimeError('the stack is empty')
        while self.queue1.qsize() != 1:
            self.help.put(self.queue1.get())

        result = self.queue1.get()
        temp = self.queue1
        self.queue1 = self.help
        self.help = temp

        return result


if __name__ == '__main__':
    q = ArrayQueue()
    for i in range(5):
        q.push(i)
    for i in range(5):
        print(q.pop())
    # q.push(3)

