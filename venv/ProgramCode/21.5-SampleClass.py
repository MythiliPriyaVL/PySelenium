class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()

print([x * y for x, y in zip([3, 4], [5, 6])])

print([(i.upper(), len(i)) for i in 'kiwi' ])