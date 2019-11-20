
# Without crating function
#x=int(input("Enter yout number: "))



#By creating Function
def Get_pair(array, x):
	count=0
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[i]+array[j]==x:
				count +=1
	return count


array= [8,34,34,5, 5,10,24,150,2,0]
x= 10

print("Number of pair is ", Get_pair(array,x))


