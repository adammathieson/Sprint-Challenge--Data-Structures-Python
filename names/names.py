import time
from binary_search_tree import BinarySearchTree
from merge_sort import merge_sort

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# names_1_tree = BinarySearchTree("")

# for name in names_1:
#     names_1_tree.insert(name)

# for name in names_2:
#     if names_1_tree.contains(name):
#         duplicates.append(name)

# Stretch
names_1_hash = {}
for i, e in enumerate(names_1):
    names_1_hash[e] = i

for name in names_2:
    if name in names_1_hash:
        duplicates.append(name)
# print(names_1_hash)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

