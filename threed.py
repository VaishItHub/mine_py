import time
import threading

def timespace(id,sec):
    print(f"start T{id}")
    time.sleep(sec)
    print(f"start time {id} after {sec} sec")
t1=timespace