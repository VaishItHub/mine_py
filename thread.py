import threading
import time

def printToBefore(id,sec):
    print(f"start T{id}")
    time.sleep(sec)
    print(f"end T{id}: after {sec} sec")
t1=threading.Thread(target=printToBefore,args=(1,5))
t2=threading.Thread(target=printToBefore,args=(2,2))
t3=threading.Thread(target=printToBefore,args=(3,7))
t1.start()
t2.start()
t3.start()