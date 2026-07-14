collection = {1,2,3,4}
print(collection)
print(len(collection))
collection2 = set()

print(type(collection2))
collection2.add(4)
collection2.add("rohan")
collection2.add((5,6,7,8))

print(collection) 
print(collection2)
print(collection.union(collection2))
print(collection.intersection(collection2))
print(collection.difference(collection2))