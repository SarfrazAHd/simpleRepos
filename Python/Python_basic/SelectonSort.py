

#Programme 1: WAP to Implement SelectionSort

print("********************************************************")
print("****************** Selection Sort **********************")
print("\n")
def SelSort(a):
    for i in range(len(A)):
        minpos=i
        for j in range(i+1,len(A)):
            if  A[j]< A[minpos]:
                minpos = j

        A[i],A[minpos]= A[minpos],A[i]
        print(A)

A=[77,4375,2,32,5654,3223,-1,0,43643]
SelSort(A)
print(A)
print("\n")

print("*****************************************************")
print("*****************************************************")


