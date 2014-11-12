a = "1111111111"
b = "1010101010"

def add_binary(a,b):
	maxlen = max(len(a), len(b))

	#Normalize lengths
   	a = a.zfill(maxlen)
	b = b.zfill(maxlen)
	print " " + a + "\n+" + b
	
	result = ''
	carry  = 0

	i = maxlen - 1

	while (i >= 0):
		r = carry

		if a[i] == '1':
			r = r + 1
		if b[i] == '1':
			r = r + 1

		i = i - 1

		if r == 1 or r == 3:
			result = "1" + result
		else:
			result = "0" + result

		if r >= 2:
			carry = 1
		else:
			carry = 0
     
	if carry == 1:
		result = "1" + result

	return result

print "------------\n" + add_binary(a,b)