A=list(map(int,input().split()))
counter=0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]>A[j]:
            counter=A[i]
            A[i]=A[j]
            A[j]=counter
            
for i in range(len(A)):
    print(A[i],end=" ")

    