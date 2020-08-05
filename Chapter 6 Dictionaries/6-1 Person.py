'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary
'''

girlfriend = {'first_name':'Gaby', 'last_name':'Garcia', 
    'age': 22, 'city':"Panorama City"}

print("My girlfriend's name is " + girlfriend['first_name'] + 
' '+ girlfriend['last_name'])

print('She is ' + str(girlfriend['age']))

print('She lives in ' + girlfriend['city'])