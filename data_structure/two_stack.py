# 两个对列实现栈
# 两个栈，必为空才能导数据，一次导完


class twostackQueue(object):

    def __init__(self):
        self.stack = []
        self.help = []

    def push(self, data):
        """模仿入队列"""
        if self.help != []:
            raise RuntimeError('the queue is not empty')
        self.stack.append(data)

    def poll(self):
        """模仿出队"""
        for i in range(len(self.stack)):
            self.help.append(self.stack.pop())
        while self.help != []:
            print(self.help.pop())


if __name__ == '__main__':
    s = twostackQueue()
    for i in range(5):
        s.push(i)
        print(i, end='')
    print()
    s.poll()
