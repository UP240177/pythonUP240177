it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age1 = [22, 19, 24, 25, 26, 24, 25, 24]

#1. Convert the ages to a set and compare the length of the list and the
#set, which one is bigger?
age=set(age1)
print("Length of the list:", len(age1))
print("Length of the set:", len(age))

if len(age1) > len(age):
    print("The list is bigger.")
elif len(age1) < len(age):
    print("The set is bigger.")
else:
    print("Both the list and the set have the same length.")

#2. Explain the difference between the following data types: string, list, tuple and set

#String - Este se encarga de almacenar texto ya sea
#letras, números y simbolos.

#List - Puede contener elementos de diferente tipo como
#números, strings, etc ademas de que se puede modificar
#despues de ser creado.

#Tuple - Almacena una colección de elementos

#Set - Colección de elementos unicos y no admite elementos 
#duplicados.


#3. I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(unique_words)
print("Número de palabras únicas es:", len(unique_words))
