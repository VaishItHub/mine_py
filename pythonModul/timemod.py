import time
# print(time.time())------------------>print time from 1jan 1970
#------------------------------------------------
# print("start")----------->pause for given second
# time.sleep(2)
# print("end")
# -----------------------------------
# print(time.ctime())------------->current time and date//time display in readable str(strformat)
# -------------------------------------------
# print(time.localtime())        -----------------------take input secondes and covrt into urrent day time date
# print(time.localtime().tm_year)
# print(time.localtime().tm_mday)
# print(time.localtime().tm_wday)
# print(time.localtime().tm_yday)
# print(time.localtime().tm_isdst)
# -----------------------------------------
# t=time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S %p",t))  ----------->tuple to str
# ---------------------------------------------------
# t=time.strptime("2024-10-0 13 :45:56","%Y-%m-%d %H:%M:%S %p")--->str to tuple
# print(t)
# -----------------------------------------------------
# performance counter-------------------count the performance in second which can store in any format
# start=time.perf_counter()
# for i in range(200):
#      print(i)
# end=time.perf_counter()
# print(f"performace: {round(end-start,3)} sec")