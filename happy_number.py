square = lambda x: x*x
def s(val):
    sum=0
    rem=0
    while val!=0:
        rem= val % 10
        sum+=square(rem)
        val//=10
    return sum
N= int(input())
while True:
    N=s(N)
    if N == 1:
        print('the number is happy number')
        break
    if N != 1 and 1<N<10:
        print('the number is not happy number')
        break
