'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''

favorite_numbers = {'Eric': 22, 'Gaby': 27, 'Brito': 69, 'Joeji': 88}
peoples = ['Eric','Gaby','Brito','Joeji']

for key in favorite_numbers:
    print(key, "'s favorite number is" , favorite_numbers[key])
# This is called iterating a Dictionary!!