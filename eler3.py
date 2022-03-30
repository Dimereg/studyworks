print('введите N')
n=int(input())
def is_simple(i):
    flag=0
    for k in range( 2, n//2):
        if n%k == 0:
            flag+=1
    if flag == 0:
        return True
        else:
            return False
            
for i in range (n,2,-1):
    is_simple(i)
    if is_simple(i):
        print(i)

        
    
    

