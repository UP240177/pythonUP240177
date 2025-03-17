#1.Unpack siblings and parents from family_members
brother = ("Sebastian", "Emanuel")
sister = ("Siberia", "Maria")
sibling = brother + sister
print(f"I have {len(sibling)} siblings")
family_members = sibling + ("Omar","Nancy")

sibling = family_members[:len(sibling)]
parents = family_members[-2:]
print(sibling, parents)

#2.Create fruits, vegetables and animal products tuples. Join the three tup
# les and assign it to a variable called food_stuff_tp.
fruit = ("Mango", "Banana", "Grape")
veggies = ("Carrot", "Onion", "Potato")
animal_product = ("Bacon", "Egg", "Butter")

#3.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = fruit + veggies + animal_product
print(food_stuff_tp)

#4.Slice out the middle item or items from the food_stuff_tp 
# tuple or food_stuff_lt list.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#5.Slice out the first three items and the last three items 
# from food_staff_lt list
mid = int(len(food_stuff_tp)/2)
food_stuff_tp = food_stuff_tp[:mid]
print(food_stuff_tp)

#6.Delete the food_staff_tp tuple completely
del food_stuff_tp

#7.Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

