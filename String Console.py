Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "Python Programmijg"
>>> x[0:5]
'Pytho'
>>> x[0:6]
'Python'
>>> x
'Python Programmijg'
>>> x[7:]
'Programmijg'
>>> x[:9]
'Python Pr'
>>> x[:]
'Python Programmijg'
>>> x[0:6:1]
'Python'
x[0:6:2]
'Pto'
x[::]
'Python Programmijg'
x[::-1]
'gjimmargorP nohtyP'
#String METHODS
x
'Python Programmijg'
len(x)
18
x.upper()
'PYTHON PROGRAMMIJG'
x.lower()
'python programmijg'
x.capitalize()
'Python programmijg'
x.title()
'Python Programmijg'
x
'Python Programmijg'
x.swapcase()
'pYTHON pROGRAMMIJG'
x
'Python Programmijg'
x =
SyntaxError: invalid syntax

x = "python is a general purpose programming"
x.find("o")#it will return index of first occurence
4
x.rfind("o")
30
x.find("o",0)
4
x.find("o",5)
24
x.index("o",5)
24
x.find("X")
-1
#-1 means substring not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'python is a general purpose programming'
x.count("o")
3
x.count("X")
0
x
'python is a general purpose programming'
x.split()
['python', 'is', 'a', 'general', 'purpose', 'programming']
x.split()[0]
'python'
x
'python is a general purpose programming'
x.split("a")
['python is ', ' gener', 'l purpose progr', 'mming']
x = ['python', 'is', 'a', 'general', 'purpose', 'programming']
type(x)
<class 'list'>
" ".join(x)
'python is a general purpose programming'
"#".join(x)
'python#is#a#general#purpose#programming'
#String - immutable
x = "hey Python"
x.lower()
'hey python'
x
'hey Python'
x[0]="H"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x[0]="H"
TypeError: 'str' object does not support item assignment
del x[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    del x[0]
TypeError: 'str' object doesn't support item deletion
del x
x
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = "python is a general purpose programming"
x.replace()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x.replace()
TypeError: replace expected at least 2 arguments, got 0
"
x.replace("python","Java")
'Java is a general purpose programming'
x = "Python"
x.zfill(10)
'0000Python'
x.center("*",10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x.center("*",10)
TypeError: 'str' object cannot be interpreted as an integer
x.center(10,"*")
'**Python**'
x.center(7)
' Python'
len(x)
6
x
'Python'
id(x)
4357100920


x = [1,2,3,4,5]
y = x
x.pop()
5
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]

x = "python"
"a" in x
False
"y" in x
True
#membership operator
x = 1
y = 1
x is y
True
