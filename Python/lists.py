# Create a list of 5 of your favorite foods.
# Print the second item in the list.
# Add two more foods to the list.
# Change the third food in the list to another one.
# Remove the first food from the list.
# Print the modified list.

fav_foods =  ["BBQ","Pizza","Biryani","Burger","Chinese"]
print(fav_foods[1])
fav_foods.append("Soup")
fav_foods.append("Shawarma")
fav_foods[2]="Haleem"
fav_foods.remove("BBQ")
fav_foods.pop(0)
print(fav_foods)


