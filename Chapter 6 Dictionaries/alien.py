alien_o = {'color':'green','points':5}
print(alien_o['color'])
print(alien_o['points'])

new_points = alien_o['points']
print('You just earned ' + str(new_points) + ' points!')

alien_o['x_position'] = 0
alien_o['y_position'] = 25

print(alien_o) # Python doesn't care about the order you added these key-value pairs only cares about the content

print('Your color is ' + alien_o['color'] + '!')
alien_o['color'] = 'blue'
print('Your color is ' + alien_o['color'] + '!')

alien_1 = {'x_position': 0, 'y_position': 25, 'speed':'fast'}

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(alien_1['x_position'])

del alien_1['y_position']
print(alien_1)

favorite_languages = {
    'jen':'python',
    'sarah':'c',
}
print("Jen's favorite coding language is " +
    favorite_languages['jen'].title() + 
    '!')