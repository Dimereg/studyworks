print('введите N')
n=int(input())
A =[0]*n
A[1]=1
A[2]=2
s=0
for i in range (3, n):
    A[i]=int(A[i-1])+int(A[i-2])
    if A[i]%2 == 0:
        print(A[i])
        s = s + int(A[i])
print(s)    

