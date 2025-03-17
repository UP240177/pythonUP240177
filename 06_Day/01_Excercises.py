#1.Create an empty tuple.
lista = tuple()

#2.Create a tuple containing names of your sisters
#  and your brothers (imaginary siblings are fine).
brother = ("Sebastian", "Emanuel")
sister = ("Siberia", "Maria")

#3.Join brothers and sisters tuples and assign 
# it to siblings.
sibling = brother + sister
print(sibling)

#4.How many siblings do you have?
print(f"I have {len(sibling)} siblings")

#5.Modify the siblings tuple and add the name of your
# father and mother and assign it to family_members.
family_members = sibling + ("Omar","Nancy")
print(family_members)