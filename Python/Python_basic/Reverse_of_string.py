
#reverse of any string 

def reverse(string):
    reversed_string = ''    
    for i in string:
        reversed_string=i+reversed_string
    print(reversed_string)


x=input("Enter any string: ")
reverse(x)   

#seceond method for reverse:

y=input("Enter any strings:")

print(y[::-1])       #so simple ):

