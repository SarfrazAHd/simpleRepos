



original = open(filename)
for line in original:
	S.push(line.rstrip('\n')) 
original.close( )
output = open(filename,'w') 

while not S.is_empty( ):
	output.write(S.pop( ) +'\n') 
	output.close( )
print("File closed")