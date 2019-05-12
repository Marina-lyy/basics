import time
import threading

def fun():
    print("Start fun")
    time.sleep(4)
    print("end fun")

print("Main thead")

t1 = threading.Thread(target=fun, args=())
# 社会守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)
# t1.daemon = Ture
t1.start()

time.sleep(2)
print("Main thread end")