p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
p_w={}
for i in range(len(p)):
    p_w[i]=p[i]/w[i]
print(p_w)
l=list(p_w.items())
n=len(l)
for i in range(n-1):
    max=i
    for j in range(i+1,n):
        if l[j][1]>l[max][1]:
            max=j
        l[i],l[max]=l[max],l[i]
print(l)
output:
{0: 5.0, 1: 3.3333333333333335, 2: 3.0, 3: 1.75, 4: 8.0, 5: 3.0, 6: 2.0}
[(4, 8.0), (0, 5.0), (1, 3.3333333333333335), (2, 3.0), (6, 2.0), (5, 3.0), (3, 1.75)]

#using lambda
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
p_w={}
for i in range(len(p)):
    p_w[i]=p[i]/w[i]
print(p_w)
l=list(p_w.items())
n=len(l)
sorted_list=sorted(l,key=lambda x:x[1],reverse=True)
print("sorting using lambda",sorted_list)
output:
{0: 5.0, 1: 3.3333333333333335, 2: 3.0, 3: 1.75, 4: 8.0, 5: 3.0, 6: 2.0}
sorting using lambda [(4, 8.0), (0, 5.0), (1, 3.3333333333333335), (2, 3.0), (5, 3.0), (6, 2.0), (3, 1.75)]
