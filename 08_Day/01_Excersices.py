#1.Create an empty dictionary called dog
dog = {}

#2.Add name, color, breed, legs, age to the dog dictionary
dog = {'Name':'',
       'Color': '',
       'Breed': '',
       'Legs': '',
       'Age_of_the_dog': ''}

#3.Create a student dictionary and add first_name, 
# last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student_dictionary =  {
    'first_name':'Miguel Enrique',
    'last_name':'Castañeda Trinidad',
    'gender':'Masculino',
    'age':'18',
    'marital_status':'Single',
    'skills':['Drawing','Creating',
              'Python'],
    'country':'Mexico',
    'city':'Aguascalientes',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

#4.Get the length of the student dictionary
print(len(student_dictionary))

#5.Get the value of skills and check the data type,
#  it should be a list
skills = student_dictionary['skills']
print(type(skills))

#6.Modify the skills values by adding one or two skills
student_dictionary["skills"].extend(["Node.js", "MongoDB"])
print(student_dictionary['skills'])

#7.Get the dictionary keys as a list
keyList = list(student_dictionary.values())
print(keyList)

#8.Get the dictionary values as a list
valuesList = list(student_dictionary.items())
print(valuesList)

#9.Change the dictionary to a list of tuples using 
# items() method
studentTuple = student_dictionary.items()
print(studentTuple)

#10.Delete one of the items in the dictionary
student_dictionary.pop('gender')
print(student_dictionary)

#11.Delete one of the dictionaries
del student_dictionary