# They store multiple items in a single variable. Set items are separated by commas
# and enclosed within curly brackets {} and seprated by commas

# info = {"Carla", 19, False, 5.9, 19}
# print(info)


# # Methods of joining two sets in Python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # # cities3 = cities.union(cities2)
# # # print(cities3)
cities.update(cities2)
print(cities)

# # # cities3 = cities.intersection(cities2)
# # # print(cities3)
cities.intersection_update(cities2)
print(cities)

# # cities3 = cities.symmetric_difference(cities2) #returns a new set 
# # # whereas the symmetric_difference_update updates into the existing set
# # print(cities3)
# # cities.symmetric_difference_update(cities2)
# # print(cities)



# # cities3 = cities.difference(cities2)
# # print(cities3)
# # # diff_update

# # Set Method in python

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = { "Seoul", "Kabul"}
print(cities.isdisjoint(cities2))


# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Seoul", "Kabul"}
# # print(cities.issuperset(cities2))
# # cities3 = {"Madrid","Tokyo"}
# # print(cities.issuperset(cities3))

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Delhi", "Madrid"}
# # print(cities2.issubset(cities))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Helsinki", "Warsaw", "Seoul"}
# # cities.update(cities2)
# # print(cities)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities.remove("Tokyo")
# # print(cities)
# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # item = cities.pop()
# # print(cities)
# # print(item)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # del cities
# # print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
# Empty set is represented as set()
print(type({}))