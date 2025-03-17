#Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
len(it_companies)
print(it_companies)

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update({"whatsApp","Instagram","Youtube"})
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)

#What is the difference between remove and discard
#Remove te indica error cuando quieres eliminar algo inexistente 
#y discard no te marca error.