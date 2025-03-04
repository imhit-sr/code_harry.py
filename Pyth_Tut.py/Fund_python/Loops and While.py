name = 'Abhishek'
for i in name:
    print(i, end="")


colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x,end = " ")


# for k in range(5):
#   print(k + 1)




# While Loops 
# i = int(input("Enter the number: "))
# print(i)
# while(i<=38):
#   i = int(input("Enter the number: "))
#   print(i)

# print("Done with the loop")

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else:
#   print("I am inside else")
# else stat is executed as soon as the while loop condition becomes false

# print("I am inside else")

# # do while loop
# while True:
#   number = int(input("Enter a positive number: "))
#   print(number)
#   if not number > 0:
#     break

#  A break statement terminates the  loop it lies within.

# for i in range(1,101,1):
#     print(i ,end=" ")
#     if(i==330):
#         break
# else:
#     print("hello")
# print("Thank you")

# Continue statement skips is used to skip that iteration 

# for i in [2,3,4,6,8,0]:
#     if (i%2!=0):
#         continue
#     print(i)




# for loop with else


# the statements in the else block will be executed only after all iterations are completed. 
# where you need to execute certain code only if the loop wasn’t terminated by a break
# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")