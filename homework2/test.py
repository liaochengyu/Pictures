# for x in range(1,100):
#     if x%2==0:
#         print(x)
#     else:
#         pass

# x=0
# while True:
#     if x%2==0:
#         print(x)
#         x+=1
#     else:
#         x+=1
#         continue

# def myAbs(x):
#     if x>=0:
#         return x
#     else:
#         return -x

# print(myAbs(-12))

# def myAbs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(myAbs('q'))

# def person(name='liao', age=12, *args, city, job):
#     print(name, age, args, city, job)

# person(,,'cheng','yu',city='chengdu',job='student')

# def function(n):
#     if n==1:
#         return 1
#     else:
#         return n*function(n-1)
# print(function(12))

# d=dict(a=1,b=2)
# for x in d:
#     print (x)
# for y in d.values():
#     print (y)
# for z0,z1 in d.items():
#     print ('d[%s]=%s'%(z0,z1))

# -*- coding: utf-8 -*-
# def triangles():
#     #n,L = 1,[]
#     L=[]
#     while True:
#         #n= n+1
#         L = [1 if (i == len(L) or i == 0) else L[i - 1] + L[i] for i in range(len(L)+1)]
#         yield L
#     return

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 20:
#         break

# def not_empty(s):
#     return s and s.strip()

# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# def is_palindrome(n):
#     #length=len(n)
#     int2str=str(n)

#     if int2str==int2str.reverse():
#         return True

# output = filter(is_palindrome, range(1, 1000))
# print(list(output))
# -*- coding: utf-8 -*-

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
#     return t[0]

# L2 = sorted(L, key=by_name)
# print(L2)
# def lazySum(*args):
#     def sum():
#         s=0
#         for x in args:
#             s+=x
#         return s
#     return sum


# for number in range(2,20):
#     for x in range(2,number):
#         if number%x==0:
#             print(number,'is not prime number')
#             break
#     else:
#         print(number,'is prime number')

# def ask_ok(prompt,retries=4,remainder='please try again!'):
#     while True:
#         ok=input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nop','nope'):
#             return False
#         retries=retries-1
#         if retries<0:
#             raise ValueError('invalid user response')
#         print(remainder)


# ask_ok('OK to overwrite the file?', 4, 'Come on, only yes or no!')

# def f(a,L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

#
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# def make_increment(n):
#     return lambda x:x+n


# with open(r'C:\Users\Administrator\Desktop\test.txt','r') as f:
#     # f.read(size)
#     read_data=f.read(2)
#     print(read_data)
#     newline=f.readline()
#     print('-'*30)
#     print(newline)

# mysql> UPDATE mysql.user SET password=PASSWORD(’liaochenyu10086’) WHERE User=’root’;
# mysqladmin -u test -p 你的密码 password liaochenyu10086

# create user 'liaochenyu'@'localhost' identified by 'liaochenyu10086';
# grant all privileges on *.* to liaochenyu@'localhost';

# SET PASSWORD FOR 'test'@'localhost' = PASSWORD('liaochenyu10086');
# try:
#     pass
# except Exception as e:
#     raise
# else:
#     pass
# finally:
#     pass

# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n

# foo('0')

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError :
#         print("Oops!  That was no valid number.  Try again...")




# ***********************************************************
# 新建了一个类
# class Student(object):
#     """docstring for Student"""
#     def __init__(self, name,score):
#         super(Student, self).__init__()
#         self.__name = name
#         self.__score=score

#     def print_score(self):
#         print('{} : {}'.format(self.__name,self.__score))
#         #或者使用%，上面为推荐用法
#         # print('%s: %s' % (self.name, self.score))

#     def get_grade(self):
#         if self.__score>=90:
#             return 'A'
#         elif self.__score>=60:
#             return 'B'
#         else:
#             return 'C'

#     def get_score(self):
#         print(self.__score)

#     def get_name(self):
#         print(self.__name)

#     def set_score(self, score):
#         """this operation can check arguments is or is not appropriate"""
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')

#     def set_name(self, name):
#         self.__name = name

# 创建实例
# a=Student('liaochengyu',100)

# a.get_name()
# a.get_score()
# print(a.get_grade())
# print("*"*20)
# a.set_name('test')
# a.set_score(0)
# a.get_name()
# a.get_score()
# print(a.get_grade())

# print(Student.__doc__())
# a.print_score()



# *****************************************************
# 了解类的继承等的相关代码
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')

#     def eat(self):
#         print('Eating meat...')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
# # using 'len' method is return object's __len__ funtion
#     def __len__(self):
#         return 10
# *****************************************************
# how to use __slots__ attribute

# class Student(object):
    # name = 'Student'
    # __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

    # def __init__(self, name):
    #     self.name = name
# *****************************************************
# how to use @property resource from 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000'
# class Student(object):

#     def get_score(self):
#          return self.__score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self.__score = value

# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2015 - self._birth
# *********************************************************************************
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen(object):
#     """docstring for Screen"""
#     def __init__(self):
#         super(Screen, self).__init__()
#         pass

#     @property
#     def width(self):
#         """liaochengyu"""
#         return self.__width
#     @width.setter
#     def width(self,value):
#         self.__width=value

#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self,value):
#         self.__height=value

#     @property
#     def resolution(self):
#         return self.__width*self.__height

# ********************************************
# how to use decorator(@)
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print('2015-3-25')
# *************************************
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print(text)
#             print('begin call')
#             func(*args,**kw)
#             print('end call')
#         return wrapper
#     return decorator

# @log
# def now():
#     print('2015-3-25')

# @log('excute')
# def now():
#     print('2015-3-25')
# *************************************
# 使用定制的类
# class Student(object):
#     """stringdoc about student class"""
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return 'student object (name : {})'.format(self.name)
#     __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


create user 'root'@'localhost' identified by 'liaochenyu';
grant all privileges on *.* to 'myroot'@localhost;
CREATE USER 'myroot'@localhost IDENTIFIED BY 'liaochenyu';
update mysql.user set password=PASSWORD('liaochenyu') where User='root';
UPDATE user SET Password = PASSWORD('liaochenyu') WHERE User = 'root';
update mysql.user set authentication_string=password('liaochenyu') where user='root';
mysql(C:\Program Files\mysql-5.7.19-winx64\bin)
