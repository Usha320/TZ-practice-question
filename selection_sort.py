n=[10,15,7,23,5]
c=0
print(n)
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if n[j] < n[i]:
            n[i],n[j]=n[j],n[i]
            print(n)
        c+=1
print(c)
output:
[10, 15, 7, 23, 5]
[7, 15, 10, 23, 5]
[5, 15, 10, 23, 7]
[5, 10, 15, 23, 7]
[5, 7, 15, 23, 10]
[5, 7, 10, 23, 15]
[5, 7, 10, 15, 23]
10        
