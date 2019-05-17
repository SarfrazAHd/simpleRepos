

# Merge sort
def merge_sort(array):
	if len(array)<= 1:
		return array

	mid = int(len(array)/2)
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	return merge(left , right)


def merge(left, right):
	result =[]
	left_ptr=right_ptr= 0
	while left_ptr<len(left) and right_ptr<len(right):

		if left[left_ptr] < right[right_ptr]:
			result.append(left[left_ptr])
			left_ptr +=1
		else:
			result.append(right[right_ptr])
			right_ptr +=1

	result.extend(right[right_ptr:])
	result.extend(left[left_ptr:])
	return result
itm=[1,231,43,4,543,62,32,532, -100,0]
print(merge_sort(itm))


