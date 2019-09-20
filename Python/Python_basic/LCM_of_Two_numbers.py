



# Finding LCM of Two Numbers
def get_LCM(x,y):
	if x>y:
		greater = x

	else:
		greater = y

	while True:

		if greater%x==0  and greater%y==0:
			get_LCM = greater
			break

		greater +=1

	return get_LCM













