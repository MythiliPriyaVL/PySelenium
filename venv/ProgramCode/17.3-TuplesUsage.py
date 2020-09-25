# A python program to demonstrate the use of tuples
# Built-in Functions: all(), any(), enumerate(), max(), min(), sorted(), len(), tuple()
#divmod( x , y ) → ( div , mod )
#Return the tuple ((x-x%y)/y, x%y). Invariant: div*y + mod == x. This is the quotient and the remainder in division.

tuple1 = ('python', 'program')
tuple2 = ('coder', 1)

if (tuple1 != tuple2):
    # cmp() returns 0 if matched, 1 when not tuple1
    # is longer and -1 when tuple1 is shoter
    print('Not the same')
else:
    print('Same')


tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

#Packing and Unpacking
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)

#Comparing tuples
#case 1
a=(5,6)
b=(1,4)
if (a>b):
    print("a is bigger")
else:
    print("b is bigger")

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items() #Loop through both keys and values, by using the items() function
print(b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])

#print('Maximum element in tuples 1,2: ', max(tuple1), ',', max(tuple2)) :TypeError: '>' not supported between instances of 'int' and 'str'
#print('Minimum element in tuples 1,2: ', min(tuple1), ',', min(tuple2)) :TypeError: '<' not supported between instances of 'int' and 'str'
