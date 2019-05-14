import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:",ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull","out of q")
    print("Out of consumer:", ctime())## 词句执行完成，在转让主进程

def producer(sequence, output_q):
    print("Into procuder:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item,"into q")
    print("Out of procuder:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_p = multiprocessing.Process(target = consumer, args = (q,))
    cons_p.start()

    # 生产多个项，sequence代表要发送给消费者的项序列
    # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    # 等待所有项被处理
    q.put(None)
    cons_p.join()