n=list(map(int,input().split()))
c=0
for i in range(1,len(n)):
    j=i-1
    while j!=-1:
        if n[j] > n[i]:
            n[j],n[i]=n[i],n[j]
            i=j
            print(n)
        j-=1
        c+=1
print(len(n),c)
output:
58 38 29 17 47 28 36
[38, 58, 29, 17, 47, 28, 36]
[38, 29, 58, 17, 47, 28, 36]
[29, 38, 58, 17, 47, 28, 36]
[29, 38, 17, 58, 47, 28, 36]
[29, 17, 38, 58, 47, 28, 36]
[17, 29, 38, 58, 47, 28, 36]
[17, 29, 38, 47, 58, 28, 36]
[17, 29, 38, 47, 28, 58, 36]
[17, 29, 38, 28, 47, 58, 36]
[17, 29, 28, 38, 47, 58, 36]
[17, 28, 29, 38, 47, 58, 36]
[17, 28, 29, 38, 47, 36, 58]
[17, 28, 29, 38, 36, 47, 58]
[17, 28, 29, 36, 38, 47, 58]
7 21
