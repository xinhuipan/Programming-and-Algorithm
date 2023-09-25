#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=5
print( x )


# In[2]:


x = 60*60*24*7
print ("the number of seconds in a week is " + str(x))
print ("the number of seconds in a week is",x)


# In[3]:


x = 5
print( x )


# In[4]:


print ( x + 1 )


# In[5]:


x = 7 * 9 + 13
print( x )
x = "I just had a peach at 3 o'clock in the morning"
print( x )
x = int( 15/4 )-27
print( x )


# In[6]:


x = 2
y = 3
print( "x=",x ) 
print( "x= "+str(x) ) 
print( "y=",y )
print( "x * y =",x*y )
print( "x + y =",x+y )


# In[7]:


x = 2
y = 3
print( "x=" , x , "y=" , y )
z = x
x = y
y = z
print( "x=" , x , " and y=" , y )


# In[8]:


x = 2
print( x )
x = x + 3
print( x )


# In[9]:


days_in_a_year = 365
print ( days_in_a_year )


# In[12]:


Apple = 2
print( Apple )

#apple和Apple都行，大小写无所谓，但是这两个不一样


# In[14]:


a = 3.14159265
b = 7.5
c = 8.25
d = a * b * b * c / 3
print( d )


# In[16]:


#variable names的好用之处

pi = 3.14159265
radius = 7.5
height = 8.25
volume_of_cone = pi * radius * radius * height / 3
print( volume_of_cone )


# In[1]:


#constant是把value定义给variable，一旦设定就不能改变了。看起来更清晰

total = 24.95
final_total = int ( 100 * total * 1.15 ) / 100
print ( final_total )


# In[2]:


#也可以这样写,CONSTANT NAME都大写

SERVICE_CHARGE = 1.15
CENTS = 100

total = 24.95
final_total = int ( CENTS * total * SERVICE_CHARGE ) / CENTS
print( final_total )

#不仅更清晰，易读，也能更容易更改数值！


# In[14]:


nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1

#加这两行，找到错误
print( nr1, nr2, nr3 )
print( nr1 % nr2 )

print( nr3 / (nr1 % nr2) )


# In[15]:


#soft typing 给variable一个新的value，type会变
#通过print( type () ) 可以看到这个value的type

a = 3
print( type( a ) )
a = 3.0
print( type( a ) )
a = "3.0"
print( type( a ) )


# In[23]:


a = 1
b = 4
c = "1"
d = "4"
print( a + b )
print( c + d )
#print( a + c )是不行的，因为int不可以加str进行运算，instead，变成两个str，或者直接逗号链接
print(str(a) + c)
print( a, c )


# In[25]:


name = "John Cleese"
print( name )


# In[26]:


a: int = 1
b: str = "4"
print( type(a), type(b) )


# In[27]:


#就算你强行把string写成int，系统还是会识别那是str

a: int = "1"
b: str = 4
print( type(a), type(b) )


# In[28]:


#shorthand operator

number_of_bananas = 100
number_of_bananas = number_of_bananas + 1
print( number_of_bananas )


# In[29]:


#和上面一样的

number_of_bananas = 100
number_of_bananas += 1
print( number_of_bananas )


# In[32]:


number_of_bananas = 100
number_of_bananas += 12
number_of_bananas -= 13
number_of_bananas *= 19
number_of_bananas /= number_of_bananas
print( number_of_bananas )
print( int( number_of_bananas ))


# In[33]:


# comment: insert your code here.
# BTW: Have you noticed that everything behind the hashtag 
print( "Something..." ) # on a line is ignored by your python interpreter?
print( "and something else.." ) # this is really helpful to comment on your code!
"""Another way
of commenting on your code is via 
triple quotes -- these can be distributed over multiple """ # lines
'''which can also be done
with single quotes''' # but be careful with there being quotes IN your comments
# when you use this multi-line method
print( "Done." )


# In[44]:


#如果是在最后用三个单引号或者三个双引号的形式，那么虽然不会被print，但会作为一个notation在最下面出现,但井号就不会显示

'''no''' 
'''no way'''
print( "没有哦" )

"""nope"""
#what


# In[51]:


radius = 2
pi = 3.14159
surface_of_circle = 2 * pi * radius
print( "the surface area of a circle with the radius", radius, "is", surface_of_circle )


# In[52]:


#或者直接

radius = 2
pi = 3.14159
print( "the surface area of a circle with the radius", radius, "is", 2* pi * radius )


# In[56]:


CENT_IN_DOLLARS = 100
CENT_IN_QUARTERS = 25
CENT_IN_DIMES = 10
CENT_IN_NICKELS = 5
CENT_IN_PENNIES = 1

amount = 12345
cents = amount #因为这个amount后面要用于计算和output，所以需要定义cents=amount

dollars = int( cents / CENT_IN_DOLLARS ) #数量是int
cents -= dollars * CENT_IN_DOLLARS #剩下的钱=总数-多少张dollars*dollars里面的cent数量

quarters = int( cents / CENT_IN_QUARTERS )
cents -= quarters * CENT_IN_QUARTERS

dimes = int( cents / CENT_IN_DIMES )
cents -= dimes * CENT_IN_DIMES

nickels = int( cents / CENT_IN_NICKELS )
cents -= nickels * CENT_IN_NICKELS

pennies = int( cents ) #因为penny就是cent

print(  amount, "consist of" )
print( "dollars:", dollars )
print( "quarters:", quarters )
print( "dimes:", dimes )
print( "nickels:", nickels )
print( "pennies:", pennies )

print( "for", amount, "the minimum number of the coins needed is", dollars + quarters + dimes + nickels + pennies )


# In[60]:


#先定义variable

var1 = 1
var2 = 2
var3 = 3

average = (var1 + var2 + var3 ) / 3 
'''给average定义'''

print( average ) #最后输出


# In[ ]:


a = 17
b = 23
print( "a =", a, "and b =", b )
a += b #表示新的a=a+b
# add two more lines of code here to ensure the swapping of a and b


print( "a =", a, "and b =", b )

