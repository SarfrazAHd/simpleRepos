
def quick_sort(array):
	if len(array)<=1:
		return array

	pivot=array[len(array)//2]
	
	left=[x for x in array if x< pivot]
	right=[x for x in array if x> pivot]
	middle=[x for x in array if x==pivot]
	return quick_sort(left)+ middle + quick_sort(right)


array=[2,3,23,5,6,2,234,5,2,5,6,4,23,2]
print("Soreted elements are ",quick_sort(array))
