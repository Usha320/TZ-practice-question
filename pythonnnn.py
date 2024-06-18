#!/usr/bin/env python
# coding: utf-8

# ## ARGUMENTS

# In[13]:


def sum(a,b):
    return a+b
print(sum(4,5))

#default arg
def sum(a,b=10):
    return a+b
print(sum(2,5))

#keyword arg
def sum(a,b):
    return a+b
print(sum(a=1,b=2))


# ## LIST

# In[16]:


list=[1,2,3,4]
print(list)


# ### to remove braces

# In[17]:


list=[1,2,3,4]
print(*list)


# ## How to take input in list

# In[2]:


user_input=input("enter the input")
number=list(map(int,user_input.split(",")))
print(number)


# ## OOPS

# In[5]:


class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("its a default constructor")
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
obj1=calculator
print(obj1.add(2,5))


# ## inheritance

# ### single inheritance

# In[10]:


class parent:
    def parent_meth():
        return "i am parent"
class child(parent):
    def child_meth():
        return " i am child derived from parent"
obj1=child
print(obj1.parent_meth())
print(obj1.child_meth())


# ### multiple inheritance

# In[ ]:





# ### multilevel inheritance

# In[13]:


class animal():
    def ani_meth():
        return "i am animal"
class dog(animal):
    def dog_meth():
        return " i am dog derived from animal"
class pup(dog):
    def pup_meth():
        return "i am pup derived from dog"
obj2=pup
print(obj2.ani_meth())
print(obj2.dog_meth())
print(obj2.pup_meth())


# ### hybrid inheritance

# In[12]:


class parent:
    def parent_meth():
        return "i am parent"
class child(parent):
    def child_meth():
        return " i am child derived from parent"
class animal(child):
    def ani_meth():
        return "i am animal"
class dog(animal):
    def dog_meth():
        return " i am dog derived from animal"
class pup(dog):
    def pup_meth():
        return "i am pup derived from dog"
obj2=pup
print(obj2.parent_meth())
print(obj2.child_meth())
print(obj2.ani_meth())
print(obj2.dog_meth())
print(obj2.pup_meth())


# ### method overriding"

# In[2]:


class Animal:
    def speak():
        return "animal is apeaking"
class Dog(Animal):
    def speak():
        return "dog is barking"
class Cat(Animal):
    def speak():
        return "meow,meow"
animal=Animal
dog=Dog
cat=Cat
print(animal.speak())
print(dog.speak())
print(cat.speak())


# ## method everloading

# In[3]:


class Calculator:
    def add(self,*args):
        total=0
        for num in args:
            total+=num
        return total
calculator=Calculator()
print(calculator.add(2,3))
print(calculator.add(2,3,4))
print(calculator.add(2,3,4,5))
print(calculator.add(2,3,4,5,6))


# In[4]:


num=int(input("Enter a number"))
if num>1:
    for i in range(2,(num//2)+1):
        if (num%i==0):
            print("not prime")
            break
    else:
            print("prime")
else:
    print("not prime")


# # 

# ## ant on railThere is a ant on your balcony.It wants to leave the rail so sometimes it moves right
# and sometimes it moves left until it gets exhausted.Given an integer array A of size N
# which consists of integer 1 and -1 only representing ant's moves.
# Where 1 means ant moved unit distance towards the right side and -1 means it moved
# unit distance towards the left .Your task is to find and return the integer value
# representing how many times the ant reaches back to original starting position.
# Note:
# * Assume 1-based indexing
# * Assume that the railing extends infinitely on the either sides
# Input Format:
# input1 : An integer value N representing the number of moves made by the ant.
# input2 : An integer array A consisting of the ant's moves towards either side

# In[4]:


n=int(input())
arr=list(map(int,input().split(",")))
count=0
for i in range (n):
    if (sum(arr[:i+1])==0):
        count+=1
print(count)

    


# ### 

# ## chocolate jar

# In[8]:


arr=list(map(int,input().split(",")))
n=int(input())
c=0
for i in arr:
    if i==0:
        continue
    if (i<=3):
        c=c+1
    else:
        if (i%3==0):
            c=c+i//3
        else:
            c=c+(i//3)+1
print(c)


# In[16]:


cho_in_jar=list(map(int,input().split(",")))
no_of_jars=int(input())
student_a=0
for cho in cho_in_jar:
    if cho==0:
        continue
    if (cho<=3):
        student_a=student_a+1
    else:
        if (cho%3==0):
            student_a=student_a+cho//3
        else:
            student_a=student_a+(cho//3)+1
print(student_a)


# ## dog age

# In[15]:


def dog_age(n):
    return n*7
n=int(input())
dog_age(n)


# In[20]:


n=int(input())
arr=list(map(int,input().split(",")))
for i in range (n):
    print(i)


# ## diwali contest

# In[29]:


def dewali(n,p):
    total_time=240-p
    problems=0
    for i in range(0,n):
        time_to_slove=5*i
        if time_to_slove <total_time:
            problems+=1
            total_time-=time_to_slove
    return problems
n=int(input())
p=int(input())
print(dewali(n,p))


# In[27]:


def string_space(string):
    str_count=0
    for char in string:
        if char==' ':
            count+=1
        return count
string=input()
print(count)


# ## paul problem

# In[12]:


n=int(input())
arr=list(map(int,input().split(",")))
arr.sort()
element_1=arr[-1]
element_2=arr[-2]
sum=0
average=(element_1+element_2)/2
for i in range(len(arr)):
    if (arr[i]>=average):
        sum+=arr[i]
        arr[i]=0
print(sum)


# ## rats

# In[1]:


def rats(r,unit,arr):
    if len(arr)==0:
        return -1
    food_requird=r*unit
    total_food=sum(arr)
    if food_requird<total_food:
        return 0
    else:
        return -1
r=int(input("Enter the no of rats:"))
unit=int(input("Enter the amount of food a rat consumes:"))
arr=list(map(int,input("list:").split()))
print(rats(r,unit,arr))


# In[14]:


def operationBinary(s):
    if not s:
        return -1
    result=int(s[0])
    i=1
    while i<len(s):
        operation=s[i]
        next_digit=int(s[i+1])
        if operation=='A':
            result=result & next_digit
        elif operation=='B':
            result=result | next_digit 
        elif operation=='c':
            result=result ^ next_digit
        i+=2
    return result
s=input()
print(operationBinary(s))


# ## checkpassword

# In[34]:


def checkPass(password):
    if(len(password)<4):
        return 0
    has_digit=False
    has_upper=False
    if password[0].isdigit():
        return 0
    for char in password:
        if char==' ' or char=='/':
            return 0
        if char.isdigit():
            has_digit=True
        if char.isupper():
            has_upper=True
    if has_digit and has_upper:
        return 1
    else:
        return 0
        
password=input()
print(checkPass(password))


# In[8]:


def count(arr,num,diff):
    count=0
    for i in range(len(arr)):
        if (abs(arr[i]-num)<=diff):
            count+=1
    return count
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(count(arr,num,diff))


# In[5]:


def findCount(arr, length, num, diff):
    count = 0

    for i in range(length):
        if abs(arr[i] - num) <= diff:
            count += 1
    
    if count == 0:
        return -1
    else:
        return count

# Example usage:
arr = [12,3,14,56,77,13]
length = len(arr)
num = 13
diff = 2
print(findCount(arr, length, num, diff))  # Output: 3


# ## vowals count

# In[14]:


def vowals_count(string):
    count=0
    vowals='aeiouAEIOU'
    for i in string:
        if i in vowals:
            count+=1
    return count
string=input()
print(vowals_count(string))


# ## head tail
# Toss and score
# You are playing a game of Toss and Score in the Hillwood City Mall with your friends.
# The game consists of the following rules:
# Toss an unbiased coin multiple times.
# For each heads you get 2 points and for each tails you lose 1 point.
# The game ends as soon as you get 3 heads in a row, or you toss the coin throughout
# the length of string S.
# You have been given a string 5 consisting of letters H (for heads) and T (for tails)
# denoting the sequence results you get on the tass of coin N times. Your task is to find
# and return an integer value representing the final score you get once the game ends.
# Note: The final score can be negative too.
# Input Specification:
# Input1: A string s. representing the sequence of results you get on the toss of coin N times
# Sample Input:
# HHHTT
# Output:
# 6

# In[4]:


def toss_and_play(string):
    score=0
    count=0
    for s in string:
        if s=='H':
            score+=2
            count+=1
            if count==3:
                break
        elif s=='T':
            score-=1
            count=0
    return score
string='HTTHTHHHTHTH'
print(toss_and_play(string))           


# ## desk
# Nearest Corner
# Bruce is a newly hired employee at a company. The Office Management Department
# has given him a desk number, which is stored in string S. He has also been handed a
# string array A. containing all the N office desk numbers.
# Array A also includes the symbol"-", which stands for the gap in the sitting
# arrangement. Comer seats are those that are on either side of the gap. Your task is to
# help Bruce find and retum an integer value. representing how far he is from the
# nearest corner seat. Return 0, if he is in the corner seat.
# Note:
# There will always be at least one gap in the string array A
# Desk number is always in a format of a number first followed by an English letter in
# uppercase
# Assume 0 - based indexing
# Input Specification:
# A string S. representing Bruce's newly assigned desk number.
# Second line containing space seperated strings showing the seat positions and gaps
# Sample input:
# 3C
# 1A 2B - 3C 4D
# Sample Output:
# 0

# In[3]:


def seat(desk, arr):
    pos = arr.index(desk)  
    min_distance = float('inf') 


    for i in range(len(arr)):
        if arr[i] == '-':
            corner_left=arr[i-1]
            corner_right=arr[i+1]
            if arr[i]==corner_left or corner_right:
                return 0
            elif i < pos:
                min_distance = min(min_distance,corner_left)
           
            elif i > pos:
                min_distance = min(min_distance, i - corner_right)
    
    return min_distance


desk = input().strip()  
arr = input().strip().split()  
print(seat(desk, arr))


# In[10]:


def distance_to_corner_seat(S, A):
    pos = A.index(S) 
    min_distance = float('inf')
    corner_indices = []
    for i in range(len(A)):
        if A[i] == '-':
            corner_indices.append(i)
    for corner_index in corner_indices:
        distance = abs(pos - corner_index)
        min_distance = min(min_distance, distance)
    
    return min_distance
S = '3C'
A = ['1A', '2B', '-', '3C', '4D']

print(distance_to_corner_seat(S, A))


# In[13]:


def distance_to_corner_seat(S, A):
    pos = A.index(S)  # Find index of Bruce's desk number S in list A
    
    # Initialize variables
    min_distance = float('inf')
    corner_indices = []
    
    # Find indices of corner seats '-'
    for i in range(len(A)):
        if A[i] == '-':
            corner_indices.append(i)
    
    # Calculate distances to the nearest left and right corner seats
    for corner_index in corner_indices:
        distance = abs(pos - corner_index)
        if distance == 0:  # If Bruce's desk is at a corner seat
            return 0
        min_distance = min(min_distance, distance)
    
    return min_distance

# Example usage:
S = '3C'
A = ['1A', '2B', '-', '3C', '4D']

print(distance_to_corner_seat(S, A))  # Output: 0


# ## pop
# Boring Arrays
# You are given an array A of size N. In one operation you can select any two elements
# from it, add their absolute difference in your score.
# Your task is to find and return an integer value, representing the maximum score.
# Note:
# Assume 1 based indexing
# The elements on which operation has been performed cannot be selected again.
# Input Specification:
# Input1: An integer value N, representing the size of array A
# input2: An integer array A
# Output Specification:
# Return an integer value, representing the maximum score
# Sample Input:
# 4
# 1 2 3 4
# Sample Output:
# 4

# In[27]:


def arr(a,n):
    score=0
    while len(n)>1:
        sorted_arr=n.sort()
        diff=abs(n[0]-n[-1])
        score+=diff
        n.pop(0)
        n.pop(-1)
    return score
a=int(input())
n=list(map(int,input().split()))
print(arr(a,n))


# ## salt peper
# '''
# Problem Statement:
# In a quaint village nestled between rolling hills, there were N different salt containers
# and N different pepper containers in two separate groups. Each container had a
# specific level of bitterness, represented by arrays A and B respectively. The task at
# hand was to form N combinations, each consisting of one salt container and one
# pepper container
# However, there was a twist to the challenge. The objective was to arrange the
# combinations in such a way that the maximum bitterness level, which is the sum of
# salt and pepper quantities in each combination, was minimized.
# Print the lowest possible maximum bitterness level.
# Input Format:
# The first line contains a single integer N, the number of salt and pepper containers in
# each group.
# The second line contains N space-separated integers, denoting the bitterness level of
# N salt containers.
# The third line contains N space-separated integers, denoting the bitterness level of N 
# Sample Innput:
# 3
# 1 3 5
# 2 8 6
# Sample Output:
# 11
# 
# '''

# In[34]:


def salt_pepper(n,s,p):
    add=[]
    for i in range(len(s)):
        for j in range(len(p)):
            add.append(s[i]+p[j])
    return max(add)
n=int(input())
s=list(map(int,input().split()))
p=list(map(int,input().split()))
print(salt_pepper(n,s,p))


# ## Arduino
# Tom is an Arduino Programmer. He has designed a program to run his robocar on a
# horizontal number line. Initially, the car is parked at: 0.
# Given an array A of N integers which can be A. B. C... the robocar runs as follows as
# per the designed program
# First the robocar moves A units in specified direction(right in case the integer is
# positive and left if the integer is negative).
# Then robocar first moves A units and then B units in a specified direction.
# In the next step, the robocar moves A units. B units, and then C units in a specified
# direction.
# This process keeps on repeating as per the number of integers in the sequence..
# Your task is to find and retum an integer value, representing the farthest coordinate
# reached by the robocar from the beginning to the end of the process.
# Sample Input:
# 1 -2 3 4
# Sample Output:
# 6

# In[37]:


def robocar(n,arr):
    sum=0
    for i in range(len(arr)):
        if i>0:
            sum+=i
        elif i<=0:
            sum-+i
    return sum
n=int(input())
arr=list(map(int,input().split()))
print(robocar(n,arr))


# ## Pizza Party
# Angela has decided to throw a pizza party. she has ordered N number of pizzas to be
# served to her N number of friends. In this way, she will be serving only one pizza to
# each friend.
# She now wants to invite fewer people to her party in order to provide more pizzas per
# person. But at the same time, she wants to ensure that there are at least Y friends at
# her party.
# Your task is to help Angela find and return an integer value, representing the sum of
# digits of the minimum number of friends that she can invite to the party, ensuring
# that each person gets an equal number of pizzas
# Sample Input:
# 100 17
# Sample Output:2

# In[5]:


def party(pizza,people):
    for i in range(people,pizza+1):
        if pizza%i==0:
            return sum(map(int,str(i)))
pizza=int(input())
people=int(input())
print(party(pizza,people))                      


# ## Signature for LCM
# Given two numbers a and b. Find the GCD and LCM of and d.
# Input:
# * Two positive integers a and b (1 <=a, b <=1000)
# Output:
# For GCD function, an integer representing the GCD of a 'and b
# For LCM function, an integer representing the LCM of a and b
# Sample Input:
# 12 18
# Output:
# 6
# 36

# In[14]:


def gcd(a,b):
    while(b>0):
        a,b=b,a%b
    return a
def lcm(a,b):
    return(a*b)//gcd(a,b)
a=int(input())
b=int(input())
print(lcm(a,b))
print(gcd(a,b))


# ## Pangram is a sentence containing every letter in the English alphabet. Given a string, 
# find all characters that are missing from the string, Le., the characters that can make 
# the string a Pangram We need to print output in alphabetic order.
# For example,
# Input: welcome to geeksforgeeks
# Output: abdhijnpquvxyz

# In[33]:


def pangram(string):
    alp='abcdefghijklmnopqrstuvwxyz'
    string=string.lower()
    miss=[]
    for i in alp:
        if i not in string:
            miss.append(i)
    sorted_op=sorted(miss)
    return miss
string='abcdefgh'
print(''.join(pangram(string)))


# ## You are given a string containing words separated by spaces. Your task is to write a
# function or program that reverses the order of words in the string.
# Sample Input:
# Hello World
# Sample Output:
# World Hello

# In[40]:


def reverse(string):
    words=string.split()
    rev=words[::-1]
    return rev
string=input()
print(*reverse(string))


# ## palindrome

# In[53]:


input_=input()
lower_ip=input_.lower()
s1=lower_ip
s2=lower_ip[::-1]
if s1==s2:
    print("it is palindrome")
else:
    print("its not a palindrome")


# ## FINDING A PEAK ELEMENT

# ## Peak Element Finder
# Description: You are given an N- dimensional array arr[]. A peak element in the array 
# is defined as an element whose value is greater than or equal to its neighboring 
# elements (if they exist). Your task is to find the index of any peak element in the given 
# array
# Note: use 0-based indexing
# Input:
# An integer representing the number of elements in the array. N space-separated 
# integers, denoting the elements of the array.
# N space-separated integers ,denoting the elements of the array arr[]
# Sample Input:
# 5  ,
# 
# 1 3 20 4 1
# Sample Output:
# 2

# In[ ]:


def slove(n,arr):
    c=0
    for i in range(1,n+1):
        if(arr[i]<arr[i-1] and arr[i]>arr[i+1]):
            c=i
            break
    if (arr[-2]>arr[-1] and arr[-1]>ans):
        c=len(arr)-1
    return c
n=int(input())
arr=list(map(int,input().split()))
print(slove(n,arr))


# 
