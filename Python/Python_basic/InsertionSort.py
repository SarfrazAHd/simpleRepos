

##  Insertion Sort

def insSort(z):
    

    for i  in range(1,len(itm)):

        current=itm[i]

        while i>0 and itm[i-1] > current:

            itm[i]=itm[i-1]

            i = i-1
        itm[i]= current


itm=[4,6,2,3,54,0,-7,-100,210]

insSort(itm)

print(itm)























































