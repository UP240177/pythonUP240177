#1.Declare an empty list
b = list()

#2.Declare a list with more than 5 items
b = ["a","e","i","o","u"]

#3.Find the length of your list
bmid = int(len(b)/2)
print(len(b))

#4.Get the first item, the middle item and
# the last item of the list
print(b[0]," ",b[bmid]," ",b[-1])

#5.Declare a list called mixed_data_types,
#  put your(name, age, height, marital status, address)
mixed_data_types = ["Miguel",18,1.67,False,"addres"]

#6.Declare a list variable named it_companies and assign initial values Facebook,
#  Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#7.Print the list using print()
print(it_companies)

#8.Print the number of companies in the list
print(len(it_companies))

#9.Print the first, middle and last company
comMid = int(len(it_companies)/2)
print(it_companies[0]," ",it_companies[comMid]," ",it_companies[-1])

#10.Print the list after modifying one of the companies
it_companies[6] = "Asus"
print(it_companies)

#11.Add an IT company to it_companies
it_companies.append("Ubisoft")
print(it_companies)

#12.Insert an IT company in the middle of the companies list
it_companies.insert(4,"Sony")
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

#14.Join the it_companies with a string '#;  '
result = '#;  '.join(it_companies)
print(result)

#15.Check if a certain company exists in the 
# it_companies list.
print(it_companies.index("IBM"))

#16.Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17.Reverse the list in descending order 
# using reverse() method
it_companies.reverse()
print(it_companies)

#18.Slice out the first 3 companies from the list
print(it_companies[:3])

#19.Slice out the last 3 companies from the list
print(it_companies[-3:])

#20.Slice out the middle IT company or companies
#  from the list
print(it_companies[3:6])

#21.Remove the first IT company from the list
comMid = int(len(it_companies)/2)
comEnd = len(it_companies)

#22.Remove the middle IT company or companies 
# from the list
it_companies.pop(0)
print(it_companies)

#23.Remove the last IT company from the list
it_companies.pop(comMid)
print(it_companies)

#24.Remove all IT companies from the list
it_companies.pop(-1)
print(it_companies)

#25.Destroy the IT companies list
del it_companies

#26.Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#27.After joining the lists in question 26. Copy the
#  joined list and assign it to a variable full_stack,
#  then insert Python and SQL after Redux.
full_stack = list()
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index("Redux") + 1,"Python")
full_stack.insert(full_stack.index("Redux") + 1,"SQL")
print(full_stack)



