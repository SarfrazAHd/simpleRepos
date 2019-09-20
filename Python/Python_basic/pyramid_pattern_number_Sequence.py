
def pyramid_number_pattern(x,y):
	for i in range(y):
		for j in range(i+1):
			print(i+x,end=" ")
		print()


	for m in range(1,y+1):
		for j in range(y-m):
			print((x+y-1)-m, end=" ")
		print()
		
pyramid_number_pattern(1,5)


