import time
from concurrent.futures import ThreadPoolExecutor
import threading



def func(seconds):
    print(f"Sleeping for {seconds} seconds")

    time.sleep(seconds)
# #Normal Code
# ti = time.time()
# func(4)
# func(3)
# func(2) # SO these three func are executed one by one 
# # but to execute them parallely we can use multithreading
# ti2 = time.time()-ti
# print(ti2)

# Same code using threading
  # Same code using Threads
# tti = time.time()
# t1 = threading.Thread(target=func, args=[4])
# t2 = threading.Thread(target=func, args=[2])
# t3 = threading.Thread(target=func, args=[1])
# t1.start() #t1,t2 and t3 are started and background mai chal 
# t2.start() #raha hai tab tak aage wala code execute kro 
# t3.start()
# t1.join() #tab tak rukunga jab tak khatam nahi ho jata
# t2.join()
# t3.join()
# print(time.time()-tti)
# Threading had i wide usecase when downloading multipile File
# we can use  threading and save our time


# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(func, 3)
#     # future2 = executor.submit(func, 2)
#     # future3 = executor.submit(func, 4)
#     # print(future1.result())
#     # print(future2.result())
#     # print(future3.result())
#     l = [3, 5, 1, 2]
#     results = executor.map(func, l)
#     for result in results:
#       print(result)
# # This concepts executes the things parallely for if i want 
# # to download something from the mulitple url

# poolingDemo()