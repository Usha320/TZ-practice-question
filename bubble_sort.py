n=[10,15,7,23,5]
print(n)
c=0
for i in range(0,len(n)):
    for j in range(0,len(n)-1-i):
        if n[j]>n[j+1]:
            n[j],n[j+1] = n[j+1],n[j]
            print(n)
            c+=1
print(c)
output:
[10, 15, 7, 23, 5]
[10, 7, 15, 23, 5]
[10, 7, 15, 5, 23]
[7, 10, 15, 5, 23]
[7, 10, 5, 15, 23]
[7, 5, 10, 15, 23]
[5, 7, 10, 15, 23]
6
