#List
# fruit1 = "apple"
# fruit2 = "mango"
# fruit3 = "orange"
# fruit4 = "persimmon"
#index  - the location of the item inside that starts with 0

fruits = ["apple", "mango", "orange", "melon"]
print(fruits)

#access item individually
print(f"My favorite fruit growing up is {fruits[0]}.")

#add more item
fruits.append("strawberry")
print(fruits)
fruits.insert(3, "watermelon")
print(fruits)
