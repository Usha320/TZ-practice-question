list=[1,2,3,4]
print(list)
#to remove braces
list=[1,2,3,4]
print(*list)
# ## How to take input in list
user_input=input("enter the input")
number=list(map(int,user_input.split(",")))
print(number)

# ## OOPS

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

# ### single inheritance
class parent:
    def parent_meth():
        return "i am parent"
class child(parent):
    def child_meth():
        return " i am child derived from parent"
obj1=child
print(obj1.parent_meth())
print(obj1.child_meth())


# ### multilevel inheritance
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

# prime number
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

# ## ant on rail
n=int(input())
arr=list(map(int,input().split(",")))
count=0
for i in range (n):
    if (sum(arr[:i+1])==0):
        count+=1
print(count)

# ## chocolate jar
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
def dog_age(n):
    return n*7
n=int(input())
dog_age(n)

n=int(input())
arr=list(map(int,input().split(",")))
for i in range (n):
    print(i)

# ## diwali contest
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

#String spaces
def string_space(string):
    str_count=0
    for char in string:
        if char==' ':
            count+=1
        return count
string=input()
print(count)

# ## paul problem
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

# ## rats problem
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

#BinaryOperations
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

#count difference
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

def findCount(arr, length, num, diff):
    count = 0

    for i in range(length):
        if abs(arr[i] - num) <= diff:
            count += 1
    
    if count == 0:
        return -1
    else:
        return count

# ## vowals count
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

# ## pop
# Boring Arrays
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


# ## Arduino Robocar
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
def party(pizza,people):
    for i in range(people,pizza+1):
        if pizza%i==0:
            return sum(map(int,str(i)))
pizza=int(input())
people=int(input())
print(party(pizza,people))                      

# ## Signature for LCM
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
def reverse(string):
    words=string.split()
    rev=words[::-1]
    return rev
string=input()
print(*reverse(string))


# ## palindrome
input_=input()
lower_ip=input_.lower()
s1=lower_ip
s2=lower_ip[::-1]
if s1==s2:
    print("it is palindrome")
else:
    print("its not a palindrome")


# ## FINDING A PEAK ELEMENT
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

# To find smallest without using built-in min
def min_built_in(arr):
    smallest=arr[0]
    for i in range(len(arr)):
        if (smallest<arr[i]):
            continue
        else:
            smallest=arr[i]
    return smallest
arr=list(map(int,input().split()))
print(min_built_in(arr))
         
