def add_binary(a,b):
	maxlen = max(len(a), len(b))

	#Normalize lengths
   	a = a.zfill(maxlen)
	b = b.zfill(maxlen)
	print a, b
	
	result = ''
	carry  = 0

	i = maxlen - 1

	while (i >= 0):
		r = carry
		print a[i], b[i]

		if a[i] == '1':
			r = r + 1 + carry
		if b[i] == '1':
			r = r + 1 + carry

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
		result = result + "1"

	return result

a = "1010"
b = "101"
print add_binary(a,b)