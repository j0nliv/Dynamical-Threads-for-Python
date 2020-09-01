#!/usr/bin/python3
import sys
import threading


threads = []
t_count = sys.argv[1]

def proc(myThread):
    print(myThread," : Started")

for i in range(1,int(t_count)+1):
    t = threading.Thread(target=proc,args=(i,))
    t.daemon = True
    threads.append(t)
    t.start()

for x,y in enumerate(threads):
    y.join()