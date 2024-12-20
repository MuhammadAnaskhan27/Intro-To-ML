# Create two sets:
# set1 containing 5 random numbers.
# set2 containing 5 other random numbers.
# Perform the following operations:
# Find and print the union of the two sets.
# Find and print the intersection of the two sets.
# Find and print the difference (items in set1 but not in set2).
# Find and print the symmetric difference (items that are in either of the sets but not both).
set1 = {1,3,5,7,9}
set2 = {2,4,6,8,10}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference =  set1.difference(set2)
symmetric_diff = set1.symmetric_difference(set2)
print(union)
print(intersection)
print(difference)
print(symmetric_diff)


