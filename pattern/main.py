n = int(input('enter a numbers of row : '))

for i in range(n):
    for j in range(i+1):
        print(j,end=' ')
    print()