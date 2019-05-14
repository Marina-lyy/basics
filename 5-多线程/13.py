#encoding=utf-8
import threading
import time

# Python2
# from Queue import Queue

# Python 3
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queue内容长度
            if queue.qsize() < 50:
                for i in range(10):
                    count = count +1
                    msg = '生成产品'+str(count)
                    # put是网queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 30:
                for i in range(3):
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(100):
        queue.put('初始产品 '+str(i))
    for i in range(3):
        p = Producer()
        p.start()
    for i in range(6):
        c = Consumer()
        c.start()
