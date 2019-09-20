## Bubble Sort


print("input element for sorting are: 5,-1,6,7,89,0,25,10,9,45")
print("")

def srt(a):

    for i in range(len(item)-1,0,-1):
        for j in range(i):
            if item[j]> item[j+1]:
                temp = item[j]
                item[j] =item[j+1]
                item[j+1] = temp





item= [5,-1,6,7,89,0,25,10,9,45]
srt(item)
print("sorted elements are:",item)


