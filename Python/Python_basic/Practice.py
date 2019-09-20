
def Reverse_of_Digit(x):

	rev = 0
	count = 0

	while x>0:
		digit = x%10
		x=x//10
		rev = rev*10+digit
		count +=1
	return rev


def Reverse_of_String(x):
	new_string=" "
	count = 0

	for i in x:
		new_string=i+new_string
		count +=1
	print("Reversed string is",new_string,count)






x= "SJHSHJdshkjdgska"

def case_changing(x):

	new_x=""

	for i in x:
		if i.islower()==True:
			new_x +=i.upper()
		elif i.isupper() == True:
			new_x +=i.lower()

	return new_x



def Decimal_to_Binary(x):
	if x>1:
		Decimal_to_Binary(x//2)
	print(x%2)



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

# Finding HCF Of Two numbers

def HCF(x,y):

    if x>y:
        diff = x-y

    else:
        diff  = y-x

    while True:
        if x%diff ==0 and y%diff==0:
            HCF = diff
            break

        diff -=1

    return HCF




def Bubble_Sort(x):
	for i in range(len(x)-1,0,-1):
		for j in range(i):
			if itm[j]>itm[j+1]:
				itm[j], itm[j+1]= itm[j+1], itm[j]

	return(x)



def Selection_sort(x):

	for i in range(len(x)):
		minpos = i

		for j in range(i+1, len(x)):
			if itm[j]< itm[minpos]:
				minpos = j

		itm[i],itm[minpos] = itm[minpos], itm[i]
		

itm = [235,2332,32,6,32,2,0.0001]



def Insertion_sort(x):

	current = itm[i]

	while i>0 and itm[i-1]>current:
		itm[i] = itm[i-1]
		i -= 1
 
	itm[i] = current


Decimal_to_Binary(10)		














