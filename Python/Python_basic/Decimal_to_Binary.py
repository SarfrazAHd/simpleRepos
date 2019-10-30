

def DecimalConversion(x):

	def decimaltoBinary(x):

		decimal = int(x)
		print('In Binary: ', bin(x))

	
	def DecimaltoOct(x):

		decimal = int(x)
		print('In Octal :', oct(x))


	def DecimaltoHexa(x):

		decimal = int(x)
		print('in Hexadecimal : ', hex(x))

	
	decimaltoBinary(x)
	DecimaltoOct(x)
	DecimaltoHexa(x)




print(int('1010010',2))



def BinarytoDecimal(x):
	binary = x
	decimal = int(binary, 2);
	print(binary,"in Decimal =",decimal);
	
#BinarytoDecimal('10100')



def OctaltoDecimal(x):
	binary = x
	decimal = int(binary, 8)
	print(binary,"Octal in Decimal = ",decimal)

#OctaltoDecimal('522')



def HexatoDecimal(x):
	binary = x
	decimal = int(binary, 16);
	print(binary,"Hexa in Decimal = ",decimal);

#HexatoDecimal('ABCDEf')

print('\n')

#DecimalConversion(100)



def binaryToOctal(x):
	binary = x
	if binary == 'x':
	    exit();
	else:
	    temp = int(binary, 2);
	    print(binary,"in Octal =",oct(temp))

#binaryToOctal('101010')

def octalToHexa(x):
	binary = x
	if binary == 'x':
	    exit();
	else:
	    temp = int(binary, 8);
	    print(binary,"in Hexa =",hex(temp))


#octalToHexa('522')



