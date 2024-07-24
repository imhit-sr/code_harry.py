# import time

# def count_odds(data):
#     time.sleep(2)
#     odds = [o for o in data if o%2 == 1]
#     return len(odds)


# data = [45,46,7,8,21]


# t1 = time.time()

# # if count_odds(data) >1:
# #     print(f"{count_odds(data)} odds")
# # Using Walrus for the same task

# if (n:=count_odds(data))>1: #Here the value of count_odds(data) is 
#     print(f"{n} odds")      #assigned to n and then checked for the >1 

# print(n:=count_odds(data)) # it assigns the value to n and return the value of n 

# t2 = time.time()

# print(f"Took {t2-t1} seconds.")