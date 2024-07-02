def tower(n,frm,to,aux,ctr):
    if n==0:
        return
    tower(n-1,frm,aux,to,ctr)
    print(f"move {n} from {frm} to {to}")
    ctr[0]+=1
    tower(n-1,aux,to,frm,ctr)
n=3
ctr=[0]
tower(n,'a','c','b',ctr)
print(ctr)
output:
move 1 from a to c
move 2 from a to b
move 1 from c to b
move 3 from a to c
move 1 from b to a
move 2 from b to c
move 1 from a to c
[7]
