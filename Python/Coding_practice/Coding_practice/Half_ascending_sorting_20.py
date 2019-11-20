
#print("Hello ")



itm=[4,6,2,3,1,0,-7,-100, 100, 90]

def half_sorting(x):

	for i in range(len(itm)//2):
		minpos =i
		for j in range(i+1,len(itm)//2):
			if itm[j] < itm [minpos]:
				minpos = j

		itm[i],itm[minpos] = itm[minpos], itm[i]

	print(itm)
		
	


	for m in range(len(itm)//2, len(itm)):
		minpos_2 =m
		for n in range(m+1,len(itm)):
			if itm[n] > itm [minpos_2]:
				minpos_2 = n

		itm[m],itm[minpos_2] = itm[minpos_2], itm[m]

	print(itm)

		

half_sorting(itm)
