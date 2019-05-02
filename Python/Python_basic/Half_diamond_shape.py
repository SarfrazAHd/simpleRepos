x=int(input("Enter number of rows:"))

for i in range(x):
    for j in range(i+1):
        print("*",end=" ")

    print()


for k in range(x):
    for l in range(x-k-1):
        
        print("*",end=" ")

    print()
