class PolyCryption:
	a,b,c,d,e = 9,2,4,3,0
	def __init__(self, a = 1,b = 1,c = 0,d = 1,e = 0):
		PolyCryption.a = a
		PolyCryption.b = b
		PolyCryption.c = c
		PolyCryption.d = d
		PolyCryption.e = e
		#Check if decrypted text == original text (Just in case)
		self.checkValid()

	def checkValid(self):
		from string import ascii_letters as s
		x = PolyCryption.Encrypt(s)
		if s == PolyCryption.Decrypt(x):
			return True
		else:
			raise Exception("Invalid Coefficient, please change a,b,c,d values!")

	def __f(x):
		#This is in the form of a(bx + c)^d
		y = PolyCryption.a*(PolyCryption.b*x+PolyCryption.c)**PolyCryption.d + PolyCryption.e
		return str(y)

	def Encrypt(text):
		output = ""
		for i in text:
			#get ascii of letter, then encrypt
			key = ord(i)
			hash = PolyCryption.__f(key)
			output += hash + " "
		return output[:-1]

	def __g(x):
		#f(x) inverse function
		x = int(x)
		y = (((x-PolyCryption.e)/PolyCryption.a)**(1/PolyCryption.d) - PolyCryption.c)/PolyCryption.b
		
		return round(y)

	def Decrypt(text):
		text = text.split(" ")
		output = ""
		for i in text:
			hash = PolyCryption.__g(i)
			output += chr(hash)
		return output

if __name__ == "__main__":	
	text = "This is sample text\nto be encrypted"
	Encrypt = PolyCryption.Encrypt
	Decrypt = PolyCryption.Decrypt
	#x is the encrypted text
	#y is the decrypted/original text
	x = Encrypt(text)
	y = Decrypt(x)
	print(x)
	print(y)
	print()
	#Changing Encryption polynomials
	PolyCryption(10,10,10,10,2)
	x = Encrypt(text)
	y = Decrypt(x)
	print(x)
	print(y)
	print()
	#Changing one coefficent
	PolyCryption.a = 3
	x = Encrypt(text)
	y = Decrypt(x)
	print(x)
	print(y)
