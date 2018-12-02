
# coding: utf-8

# ### Printing statements

# In[ ]:

# Print
print("I love Python")


# In[ ]:

# Print
print("I love Python")#commment


# In[ ]:

# Print

print("I love Python")#commment


# In[ ]:

# Print

print("I love \#should not have comments here
Python")"#commment


# In[ ]:

# Print
'''multiple 
line comments'''
print('''I love 
Python''')#commment
#print "\\"


# In[ ]:

# Print
print("I love Python")


# In[ ]:

x=1
y=2
z=4
print(x, y, z, sep=',')#works in 3.x


# In[ ]:

print(x, end=" ");print(x, y, z)  # Two prints, same output line #works in 3.x


# In[ ]:

print(x, y, z, sep='...', end='!\n')  # Multiple keywords #works in 3.x
print(x, y, z, end='!\n', sep='...')  # Order doesn't matter #works in 3.x


# In[ ]:

#print "hello",#in 2.x
print("world")


# # Variables and types
# 

# In[ ]:

#variable name Syntax: (underscore or letter) + (any number of letters, digits, or underscores)
#Case matters: SPAMis not the same as spam
#Reserved words are off-limits


# In[ ]:

# Variables and assignment
a = 10
print(a)
b = 5
print(b)


# In[ ]:

# Dynamically-inferred types
a = 10
print(type(a))
a = '10'
print(type(a))
a = 10.0
print(type(a))
print(isinstance(a,int))


# In[ ]:

# Type-checking
a = 10
b = '5'
print(a + b)


# In[ ]:

# Manual type-casting (string to int)
a = 10
b = '5'
print(a + int(b))


# In[ ]:

# Automatic type-casting (int to float)
a = 10
print(type(a))
a += 5.0
print(type(a))  


# In[ ]:

# Integer division
a = 10
b = 5                                         
print(a/b)
print(float(b)/a)
print(int('101',2))


# In[ ]:

# Forcing float division
b='3'
a=2.0
print(float(b)/a)
# How to correct?


# # Assignments and Expressions

# In[ ]:

spam = 'Spam'#Basic form
print(spam)
spam, ham = 'yum', 'YUM'#Tuple assignment (positional)
print(spam,ham)
[spam, ham] = ['yum', 'YUM']#List assignment (positional)
print(spam,ham) 
a, b, c, d = 'spam'#Sequence assignment, generalized
print(a,b,c,d)
#a,*b = 'spam'#Extended sequence unpacking (Python 3.0)
#print(a,b)
spam = ham = 'lunch'#Multiple-target assignment
print(spam,ham)
number=9
number += 42#Augmented assignment 
print(number)


# In[ ]:

[a, b, c] = (1, 2, 3)
print(a,c)
(a, b, c) = "ABC"
print(a,b)
((a, b), c) = ('SP', 'AM')
print(a,b,c)


# In[ ]:

red, green, blue = range(3)
print(red,green,blue)


# In[ ]:

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)


# In[ ]:

a, b = seq#error


# In[ ]:

*a, b = seq#only in 3.0
print(a)
print(b)
a, *b, c = seq
print(a)
print(b)
print(c)
a, *b = 'spam'
print(a)
print(b)
a, b, c, *d = seq
print(a,b,c,d)
a, b, c, d, *e = seq
print(a,b,c,d,e)


# In[ ]:

#throws error
#a, *b, c, *d = seq
#a, b = seq
#*a = seq
*a, = seq#correct usage
print(a)


# In[ ]:

a=3
b=5

print(a+b)
print(a-b)


# In[ ]:

c=4.5
a=2
print(c/a)
print(c//a)
print(c*a)
print(c%a)


# In[ ]:

#boolan operators
print (1 or 0)
print (-3 and 0)
print (not 1)


# In[ ]:

#identity test
print(a is b)
print (a is not b)


# In[ ]:

print (1<<2)
print (1>>1)


# In[ ]:

ans=lambda a,b:a**b
print(ans(5,3))


# In[ ]:

#complex number
a=1+0j
b=1+2j
print (a*b)


# In[ ]:

#multiple assgnment
a=b=c=3
print ("value of a, b,c",a,b,c)
l='ab'
d,e=l
print ("d=",d,"e=",e)
b=2 #a=3,b=2
a,b=b,a
print("a=",a,"b=",b)#a=2,b=3


# In[ ]:

#augumented
a+=1#a=2
print (a)
b/=3#b=3
print (b)


# In[ ]:

#del
a=4
print (a)
del a,b#unbinds references
print (a)


# In[ ]:

#expressions
x=4
y=2

print (True & False ,1|1)
print ("4^2",x**y)
print ("0 and 1:",0 and 1)
print ("0 or 1:",0 or 1)
#comparison
a=1;b=4;c=4;d=5
print (a < b <= c < d) #same as a < b and b <= c and c < d
#tenary operator
x = 4 if b > 8 else 9
print ("value of x",x)
print ("2^3",pow(2,3))
p=pow(a,b,c)#same as (a**b)%c
print ("pow(1,4,4)=",p)
print ("(1**4)%4=",(a**b)%c)


# ### User Input

# In[ ]:

a = input('Enter value 1: ')
print(a)


# In[ ]:

a = input('Enter value 1: ')
b = input('Enter value 2: ')
print (a + b)


# ### Conditional (If) Statements

# In[ ]:

# If statements
# Unlike other languages, indentation is significant
a = 5
if a > 10:
    print ('a is greater than 10')
    if a >= 15:
        print ('a is also at least 15')
elif a > 5:
    print ('a is greater than 5 but not greater than 10')
else:
    print ('no condition matched')
    print ('so a is 5 or less')


# In[ ]:

x=int(input("enter a number"))
if x==0 :
    pass#do nothing
elif x>23 or x%2 and x<5:
    print(x)
elif x%2==0:
    print("x is even")
else:
    print(x)


# ### <font color = 'green'>Your Turn</font>

# In[ ]:

# Write a program that asks for a number and computes the
# square of that number.
# If the square is 100 or greater, print the squared value
# and the word 'big'.
# Otherwise if the square is between 50 and 99, print the
# squared value and the word 'medium'.
# Otherwise just print 'too small to bother with'.
#


# # Sequences

# ## Tuples
# 

# In[ ]:

t1=(21,)#singleton
t2=(21,22)#pair
t3=(21,22,'twenty three')
t4=()
print(t1)
print (t2)
print (t3,t4)
x=tuple('python')
print (x)
print (t2[1])
t2[1]=0


# ## list

# In[ ]:

#list
l1=['value1']
l2=['a','b','c']
l3=[]
L = ['abc', ['def', 'ghi']] #Nested sublists
l4=list('python')
print (l1)
print (l2)
print (l3)
print (l4) 
l3.append(1)
l2[1]=3#mutable
print (l3)
print (l2)
#z=[1,2].extend([4,5])
#print z


# In[ ]:

L = list(range(-4, 4))
print (L)


# In[ ]:

l1=[1,2,3,4,5]
l1.insert(2,'next is three')
print (l1)


# In[ ]:

l1.remove(2)
print(l1)


# In[ ]:

print (l1.pop())


# In[ ]:

print (l1.pop(1))
print (l1)


# In[ ]:

#operations in sequences
l=[1,2,3,4]
s="python"
print (len(s))
print (sum(l))
print (min(l))
print (max(l))
l1=[5,6,7,]
print (l+l1)
print ("l*2",l*2)

print (2 in l)
print ('py'in s)
#indexing sequence
print (l1[1],l1[-1],l1[-2])
#silicing
print (s[1:3],l[:2],l[1:],l[:])


# In[ ]:

l=[1,2]
l1=[3,4]
l3=l+l1
l3[2]=6
print(l1)
print(l3)


# In[ ]:

#more operations in list
#l1=[5,6,7,]
l1[3:5]=[9,8,10] 
print (l1)
l1=[1,2,3,4,5,6,7,8,9,10]
del l1[::4]
print ("after delete",l1)
del l1[0]
print ("after del first position in l1",l1)
print ("no of occurances of 3",l1.count(3))
l6=[1,2,3]
print ("number six in position" , l6.index(1))
l1.append(1)
print ("1 is appended", l1)
l1.extend(l)
print ("extending l1 by l",l1)
l1.sort()
#sorted(l1)
print ("sorted l1",l1)

l1.reverse()# or reversed(l1)
print ("reverse ",l1)


# In[ ]:

l1=[1,2,3,4,5,6,7,8,9,10]

del l1[::4]
print ("after delete",l1)


# In[ ]:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])


# In[ ]:

L = ['abc', 'ABC', 'aBe']
L.sort()  # Sort with mixed case
print(L)

L = ['abc', 'ABC', 'aBe']
L.sort(key=str.lower)  # Normalize to lowercase
print(L)

L = ['abc', 'python', 'zee']
L.sort(key=str.lower, reverse=True)  # Change sort order
print (L)


# ## dictionary

# In[ ]:

#dictionary
d1={}
d2={'one':1,'two':2,'three':3,'four':4}
d3={'one':1}
print (d2['one'])
print (d2)
print (d3)
print (dict(one=1))
print (dict([[1,2],[4,3]]))
print (dict.fromkeys('hello', 2)) # same as {'h':2, 'e':2, 'l':2, 'o':2}
print (dict.fromkeys([1, 2, 3])) # same as {1:None, 2:None, 3:None}
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict1))
#seq2=(1,2,3)
dict2 = dict.fromkeys(seq, 10,11,12)
print ("New Dictionary : %s" %  str(dict2))


# In[ ]:

#operations in dictionary
print (d2['two'])
print (d2.get('five','not available'))
print (d2.get('four'))
#print (d2.has_key('six'))#not in 3.x
print('six' in d2)
print (d2.items())
print (d2.keys())
print (d2.values())
print (d2)
#other dict methods practise at home(ref r2 chapter4)


# In[ ]:

D = {'food': {'ham': 1, 'egg': 2}}
print(D['food']['ham'])
keyslist=[1,2,3]
valslist=[4,5,6]
D = dict(zip(keyslist, valslist))
print(D)


# In[ ]:

print(D.copy())
D2={'one':1}
D.update(D2)
print(D) 
D.pop('one')
print(D)


# In[ ]:

#only in 3.0
print (list(zip(['a', 'b', 'c'], [1, 2, 3])))  # Zip together keys and values

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Make a dict from zip result
print(D)


# In[ ]:

D = dict(a=1, b=2, c=3)
print(D)


# In[ ]:

# Iterating through a list of dictionaries
dlist = [{'name':'Mary', 'age':20}, {'name':'John', 'age':30},         {'name':'Bill', 'age':10}, {'name':'Susan', 'age':40}]
for x in dlist:
    if x['age'] >= 30:
        print x['name'], 'is old'
    if x['age'] < 20:
        print x['name'], 'is young'


# In[ ]:

# Duplicate keys not allowed - note overwriting behavior
a = {'name': 'monica', 'name': 'catherine'}
print(a)


# ## string

# In[ ]:

#string
a='python'
b="python"
print(a,b)
a='I\'m a student'
print (a)


# In[3]:


a=('I am ' #logical line continues
  'a teacher')#indendation not needed
print (a)
print (a[0])
print(len(a))
print(a[0:4])
#a[2]='w'#string isimmutable
print(a[::-1])
print(a[9:4:-1])


# In[ ]:

# String "arithmetic" (actually concatenation)
a = 'Monica '
b = 'Catherine'
print(a + b)


# In[ ]:

#plain
a=10
b='string'
print(a,b)


# ###  Loops

# In[22]:


a = [2, 4, 7, 9]
print(a)


# In[23]:

# Iterate through a list
for x in a:
    print (x, 2 * x)


# In[24]:

# List elements can be of different types
a = [1, 'two', 3.0, [4,5,6]]
print(a)
print (type(a))
print (type(a[0]), type(a[1]), type(a[2]), type (a[3]))


# In[25]:

#range and xrange
for x in range(10):
    print (x)
print ("##################")
for x in range(1,10):
    print (x)
print ("##################")
for x in range(1,10,3):
    print (x)
#print range(1,5)
#for i in xrange(1,5):
 #   print i


# In[28]:

list1=[1,'a',2,3]
for x in list1:
    print(x)
for letter in'python':
    print (letter)
st="python"
for i in st:
    print(i)


# In[1]:

while True:
    i=int(input('enter a number'))
    if i>20:
        break
print ("entered number is greater than 20")


# In[3]:

# Echo user input, 0 indicates stop
a = int(input('Enter a number, 0 to stop: '))
while a != 0:
    print (a)
    a = int(input('Enter a number, 0 to stop: '))


# ### <font color = 'green'>practise</font>

# In[7]:

# Below is code that creates a list of four items,
# represented as dictionaries specifying each item's
# color and size.
# Add code to ask for a number, then print the color of all
# items whose size is greater than that number.
items = [{'color':'red', 'size':10}, {'color':'blue', 'size':3},         {'color':'green', 'size':15}, {'color':'yellow', 'size':6}]
s=int(input('enter size'))
for x in items:
    if x['size'] > s:
        print(x['color'])
   

    


# ### <font color = 'green'>practise</font>

# In[ ]:

# Copy-paste your program from above and revise it to repeatedly
# ask for two numbers and print the color of all items whose
# size is between the two numbers, i.e., whose size is higher
# than the first number and lower than the second number.
# If the user's second number is equal to or smaller than
# the first number, the program should print 'Done' and stop.
# Note: for the "and" of two conditions C1 and C2, use "C1 and C2"
#
items = [{'color':'red', 'size':10}, {'color':'blue', 'size':3},         {'color':'green', 'size':15}, {'color':'yellow', 'size':6}]


# ### Functions 

# In[16]:

# Create a function with no arguments or return value
def simple():
    print ('This function has no arguments or return value')


# In[17]:

# Call the function five times
for i in [1,2,3,4,5]:
    simple()


# In[19]:

# Create a function with arguments and a return value
def addthem(a, b):
    return a + b


# In[20]:

# Call the function five times
for i in [1,2,3,4,5]:
    print ('x is', i, '  y is', i+1, '  sum is', addthem(i,i+1))


# In[24]:

def f(x, y=[]):
    #y.append(x)
    print("y valus",y)
    return y
print (f(23)) # prints: [23]
print (f(42,2))


# In[25]:

def f(x, y=None):
    if y is None: 
        y = []
    y.append(x)
    return y
print (f(23)) # prints: [23]
print (f(42)) 


# In[27]:

def sum_args(*numbers):
    '''Accept arbitrary numerical arguments and return their sum.
    The arguments are zero or more numbers. The result is their sum.'''
    return sum(numbers)
print (sum_args(23, 42, 21,25))


# In[31]:

x=8
def counter( ):
    global x
   
    counter.count += 1
    print(cnt)
    return counter.count
counter.count = 5
cnt=1
print(counter())  


# In[32]:

def f(x, y):
    x = 23
    y.append(42)
a = 77
b = [99]
f(a, b)
print (a, b)


# In[33]:

def f(middle, begin='init', end='finis'):
    return begin+middle+end
print (f('tini', end='')) # prints: inittini
print (f('tini'))


# In[35]:

def divide(divisor, dividend):
    return dividend // divisor
print (divide(12, 94)) # prints: 7
print (divide(dividend=94, divisor=12)) # prints: 7


# In[37]:

def sum_args(*numbers):
    return sum(numbers)
d={'a':1,'b':2,'c':3}
print (sum_args(*d.values( )))
#print d.values()


# In[38]:

#nested function
def percent1(a, b, c):
    def pc(x, total=a+b+c): 
        return (x*100.0) / total
    print ("Percentages are:", pc(a), pc(b), pc(c))
percent1(23,123,56)


# In[40]:

def make_adder(augend):
    def add(addend):
        return addend+augend
    return add(augend)
ans=make_adder(2)
print (ans)


# In[41]:

def squares(x):
    for i in range(x): 
        yield i ** 2#yield  sends a result object back to the caller, but remembers where it left off
res=squares(4)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))


# In[ ]:

def f (x): return x**2 
print f(8)
g = lambda x,y: x**y
print g(8,2)


# In[42]:

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: x % 3 == 0, foo)))

print (list(map(lambda x: x * 2 + 10, foo)))

#source
#http://www.secnetix.de/olli/Python/lambda_functions.hawk


# # your turn

# In[ ]:

#Create a function which accepts dictionary keys(as a list) as its only argument.
#The function removes the duplicate keys and returns a sorted list of keys 


# In[44]:

def check(n):
    d={'moni':'A','maria':'B'}
    for i in n:
        if i in d:
            print(d[i])
        else:
            print("new entry",i,"enter gradefor i")
            g=input()
            d[i]=g
            print(d)
print("enter 5 names")
nam=[]
for i in range(3):
    nam.append(input())
check(nam)
    #print(nam)
    


# In[49]:

def simple(a,b,c):
    return a,b,c,c+1
x=simple(2,3,4)


# In[50]:

x


# In[ ]:



