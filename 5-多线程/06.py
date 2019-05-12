import time
import threading

def fun():
    print("Start fun")
    time.sleep(4)
    print("end fun")

print("Main thead")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(2)
print("Main thread end")