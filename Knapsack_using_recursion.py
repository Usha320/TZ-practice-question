def max_val(weight,value,capacity,n):
    if n==0 or capacity==0:
        return 0
    if (weight[n-1]>capacity):
        return max_val(weight,value,capacity,n-1)
    else:
        return max((value[n-1]+max_val(weight,value,capacity-weight[n-1],n-1))
                   ,max_val(weight,value,capacity,n-1))
weight=[1,3,5,4,1,3,2]
value=[5,10,15,7,8,9,4]
capacity=15
n=len(weight)
print(max_val(weight,value,capacity,n))
output:
51
