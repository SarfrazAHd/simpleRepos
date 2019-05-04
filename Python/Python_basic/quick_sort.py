
def quick_sort(arr):
	if len(arr)<=1:
		return arr


	pivot =arr[len(arr)//2]

	right=[x for x in arr if x>pivot]
	left=[x for x in arr if x<pivot]
	middle=[x for x in arr if x==pivot]
	return quick_sort(left) + middle + quick_sort(right)

itm=[3,54,1,-1,0,-100]
print(quick_sort(itm))



