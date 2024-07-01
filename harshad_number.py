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

n=i nput()
dig_sum = lambda x : eval('+'.join([i for i in x]))   
print("the number is harsad number") if int(dig_sum(n)) % int(n) ==0 else print('the number is not harshad number')
