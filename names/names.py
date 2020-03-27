import time
from binary_search_tree import BinarySearchTree
# original runtime is n ** 2
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

head = 0

for i,name_1 in enumerate(names_1):
    if i == 0:
        head = BinarySearchTree(name_1)
    else:
        y = head.insert(name_1)

for i,name_2 in enumerate(names_2):
        x = head.insert(name_2)
        if x:
          if x in names_1:
            if x not in duplicates:
              duplicates.append(x)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

