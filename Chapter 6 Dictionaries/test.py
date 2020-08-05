a = [1, 2, 3]
b = [1, 2, 3]
c = a
 
a[0] = 5
 
print(a)  # [5, 2, 3] - changed
print(b)  # [1, 2, 3] - didn't change
print(c)  # [5, 2, 3] - also changed

a = int(input())  # 10
b = int(input())  # 10
print(a is b)     # True
print(id(a))      # 4462719392
print(id(b))      # 4462719392
 
a = int(input())  # 10000
b = int(input())  # 10000
print(a is b)     # False
print(id(a))      # 4466218032
print(id(b))      # 4466218160

#NOTE: Python favors small integers and will use the same small number as reference
# Therefore having the same ID #
# For large numbers it creates new objects --> new ID
a = [1, 2, 3]
b = a
a = [1, 2, 3]
 
print(a is b)