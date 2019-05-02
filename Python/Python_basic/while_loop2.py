#print no from 1-100 but don't print  no.divisble by 3.

#using while loop
i=1
while i<=100:
    if i%3 == 0 and i%5==0:
        print(i)
    i=i+1   





    #using for loop

for i in range(1,101,1):
    if i%3!=0:
       print(i)
    

print("Good bye:")    

        
