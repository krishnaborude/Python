# ===============================================
# Exam Answers – Python
# ===============================================

# -----------------------------------------------
# Section A – MCQs (10 × 1 = 10 Marks)
# -----------------------------------------------
# 1. The operator "+=" mutates the same list.
#    Answer: b
#
# 2. Default list is shared across calls.
#    Answer: a
#
# 3. "is" checks identity, "==" checks value.
#    Answer: b
#
# 4. (1,2,3) is (1,2,3) → False (different objects).
#    Answer: b
#
# 5. list + tuple → TypeError, others are valid.
#    Answer: a
#
# 6. Slicing past the end returns [].
#    Answer: a
#
# 7. __x (name-mangling) is Python encapsulation trick.
#    Answer: b
#
# 8. len((1,2,3)) is valid.
#    Answer: b
#
# 9. a = [1,2,3] → print(a*2 + [5] + a) → [1,2,3,1,2,3,5,1,2,3]
#
# 10. Output of: print(0.1 + 0.2 == 0.3) → False
#     Answer: b (False)


# -----------------------------------------------
# Section B – Theory Questions (5 × 2 = 10 Marks)
# -----------------------------------------------

# Q1. Method Resolution Order (MRO)
class A:
    def show(self): print("Class A")

class B(A):
    def show(self): print("Class B")

class C(A):
    def show(self): print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()        # Output: Class B
print(D.mro())    # [D, B, C, A, object]

# Q2. Private Attributes
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private attribute

    def get_marks(self):
        return self.__marks

s = Student("Krishna", 85)
print(s.name)          # Krishna
print(s.get_marks())   # 85

# Q3. Shallow vs Deep Copy
import copy
a = [[1, 2], [3, 4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]

# Q4. Constructor Overloading with Default Args
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

p1 = Person("Ravi", 21)
p2 = Person("Amit")
p3 = Person()

# Q5. Positional vs Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student("Krishna", 20)        # positional
student(age=22, name="Ravi")  # keyword


# -----------------------------------------------
# Section C – Programs / Practical
# -----------------------------------------------

# 1) 4-digit Armstrong (Narcissistic) numbers
res = []
for n in range(1000, 10000):
    s = str(n)
    if sum(int(d)**4 for d in s) == n:
        res.append(n)
print("Armstrong numbers:", res)

# 2) Merge two dicts without update(); sum common keys
def merge_sum(a, b):
    out = {}
    for k in set(a) | set(b):
        out[k] = a.get(k, 0) + b.get(k, 0)
    return out

print(merge_sum({'x':2,'y':1}, {'y':3,'z':5}))

# 3) 2×2 Matrix Class
class Matrix2x2:
    def __init__(self, a11,a12,a21,a22):
        self.m = [[a11,a12],[a21,a22]]

    def display(self):
        for r in self.m:
            print(r)

    def __add__(self, other):
        r = Matrix2x2(0,0,0,0)
        r.m = [[self.m[i][j] + other.m[i][j] for j in range(2)] for i in range(2)]
        return r

    def __matmul__(self, other):  # A @ B
        r = Matrix2x2(0,0,0,0)
        r.m = [[sum(self.m[i][k]*other.m[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        return r

# 4) Recursive digital root
def digital_root(n):
    n = abs(n)
    if n < 10: 
        return n
    return digital_root(sum(int(d) for d in str(n)))

print(digital_root(9875))  # 2

# 5) Inheritance: Person → Student
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
    def is_passed(self):
        return self.marks >= 35

# 6) Queue using two stacks
class TwoStackQueue:
    def __init__(self):
        self._in, self._out = [], []
    def enqueue(self, x):
        self._in.append(x)
    def dequeue(self):
        if not self._out:
            while self._in: self._out.append(self._in.pop())
        if not self._out: 
            raise IndexError("empty queue")
        return self._out.pop()

# 7) Library with encapsulated book list
class Library:
    def __init__(self):
        self.__books = []
    def add(self, title):
        if title not in self.__books: self.__books.append(title)
    def remove(self, title):
        if title in self.__books: self.__books.remove(title)
    def search(self, keyword):
        return [b for b in self.__books if keyword.lower() in b.lower()]
    def list_all(self):
        return tuple(self.__books)

# 8) Flatten nested list
def flatten(x):
    for item in x:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(flatten([1,[2,[3,4]],5])))

# 9) Multi-level Inheritance: Device → Laptop → GamingLaptop
class Device:
    def __init__(self, brand):
        self.brand = brand
    def specs(self):
        return f"Brand: {self.brand}"

class Laptop(Device):
    def __init__(self, brand, cpu, ram, price):
        super().__init__(brand); self.cpu, self.ram, self.price = cpu, ram, price
    def specs(self):
        return f"{super().specs()}, CPU: {self.cpu}, RAM: {self.ram}GB, Price: {self.price}"

class GamingLaptop(Laptop):
    def __init__(self, brand, cpu, ram, gpu, price):
        super().__init__(brand, cpu, ram, price); self.gpu = gpu
    def specs(self):
        return f"{super().specs()}, GPU: {self.gpu}"

# 10) Calculator with overloaded add
class Calculator:
    def add(self, a, b, c=None):
        return a + b if c is None else a + b + c

calc = Calculator()
print(calc.add(2,3))    # 5
print(calc.add(2,3,4))  # 9

# ===============================================
# End of Answers
# ===============================================
