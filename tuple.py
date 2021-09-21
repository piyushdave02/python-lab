Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mytuple=("ram","shyam","mohan")
>>> print(mytuple)
('ram', 'shyam', 'mohan')
>>> mytuple=("ram","shyam","mohan","ram","mohan")
>>> print(mytuple)
('ram', 'shyam', 'mohan', 'ram', 'mohan')
>>> mytuple=("ram","shyam","mohan")
>>> print(len(mytuple))
3
>>> mytuple = ("ram",)
>>> print(type(mytuple))
<class 'tuple'>
>>> #NOT a tuple
>>> mytuple = ("ram")
>>> print(type(mytuple))
<class 'str'>
>>> tuple1 = ("a", "b", "c")
>>> tuple2 = (1, 2, 3, 4, 5)
>>> tuple3 = (True, False, False)
>>> print(tuple1)
('a', 'b', 'c')
>>> print(tuple2)
(1, 2, 3, 4, 5)
>>> print(tuple3)
(True, False, False)
>>>  mytuple = ("abc", 20, True, 11, "male")
 
SyntaxError: unexpected indent
>>> mytuple = ("abc", 20, True, 11, "male")
>>> print(mytuple)
('abc', 20, True, 11, 'male')
>>> mytuple=("ram","shyam","mohan")
>>> print(mytuple[1])
>>> print(mytuple[1])
shyam
>>> mytuple=("ram","shyam","mohan")
>>> print(mytuple[-1])
mohan
>>> mytuple=("ram","shyam","mohan","sohan","rohan")
>>> print(mytuple[1:3])
('shyam', 'mohan')
>>> mytuple=("ram","shyam","mohan","sohan","rohan")
>>> print(mytuple[:1])
('ram',)
>>> mytuple=("ram","shyam","mohan","sohan","rohan")
>>> print(mytuple[1:])
('shyam', 'mohan', 'sohan', 'rohan')
>>> 