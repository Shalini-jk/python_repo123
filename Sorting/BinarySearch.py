num=[2,5,9,12,17,37,86]

print('List: ',end='')
for n in num:
    print(n,end=' ')
print('\n')

x=int(input('Enter number to search '))
f=0
S=0
E=len(num)-1

while S<=E:

    M=(S+E)//2

    if x==num[M]:
        print('Number found at index',M)
        f=1
        break

    elif x>num[M]: 
        S=M+1

    elif x<num[M]:  
        E=M-1

if f==0:
    print('Number not found')