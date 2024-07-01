 
n=int(input())
val=n
sum=0
rem=0
while val!=0:
    rem= val % 10
    sum+=rem
    val//=10
    
if n % sum ==0:
    print("the number is harsad number")
else:
    print('the number is not harshad number')
