# Tuples are immutable 

# country = ("Spain", "Italy", "India",)
# #            [0]      [1]      [2]     
# print(country[0])
# print(country[1])
# print(country[2])

# country = ("Spain", "Italy", "India", "England", "Germany")
# #            [0]      [1]      [2]       [3]        [4]
# print(country[-1]) # Similar to print(country[len(country) - 1])
# print(country[-3])
# print(country[-4])

# We can check if a given item is present in the tuple. This is done using the in keyword.
# country = ("Spain", "Italy", "India", "England", "Germany")
# print(country.index("Germany"))
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")
my_list = [1, 2, 3, 4, 5]

# Check if 3 is in the list
if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

# print(animals[3:7])     #using positive indexes
# print(animals[-7:-2])   #using negative indexes

# print(animals[4:])      #using positive indexes
# print(animals[-4:])     #using negative indexes
# print(animals[:-3]) 

# print(animals[::2])     #using positive indexes
# print(animals[-8:-1:2])

# Operations on Tuple

# Tuples are immutable, hence if you want to add, remove or change tuple
# items, then first you must convert the tuple to a list
# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item 
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = len(tuple1)

# l = ()
# print(dir(l))