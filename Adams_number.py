square =lambda n: n*n
rev = lambda n: int(str(n)[::-1])
i = int(input()) 
print("the number is Adam's number") if rev(square(rev(i))) == square(i) else print("the number is not Adnan' number")   
