A = [5, 2, 4, 6, 1, 3, 2, 6]
p = 1
q = len(A)


def Partition(A,p,q):
    i=p
    x=A[i]
    for j in range(p+1,q+1):
        if A[j]<=x:
            i=i+1
            tmp=A[j]
            A[j]=A[i]
            A[i]=tmp
    l=A[p]
    A[p]=A[i]
    A[i]=l
    return i


def quicksort(A,p,r):
    if p<r:
        q = (p + r) // 2
        quicksort(A, p, q)
        quicksort(A, q + 1, r)
    return A


res = quicksort(A, p, q)
print(res)
