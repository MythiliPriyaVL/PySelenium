a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
print(a.symmetric_difference(b))
print(a.union(b)- a.intersection(b))

print(a.difference(b))
print(a-b)

print(bool(0))
print(bool(21))

info1 = 'Infinity'
print(info1.find('a'))

count = 0
while count < 2:
   print (count, " is  less than 2")
   count = count + 2
else:
   print (count, " is not less than 2")

x=float('inf')
print(x)

list_pt = list('Welcome')
print(list_pt)

y=10.0
z=int(y)
print(type(z))
x=float.fromhex('A')
print(type(x))

a = -10
if a:
  print("a's value")
else:
  print("Sorry nothing will get printed")