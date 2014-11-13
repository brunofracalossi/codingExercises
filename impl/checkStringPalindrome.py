string = "a"
size = len(string)
aux_size = size - 1
is_palindrome = True

for i in xrange(size / 2):
	if string[i] != string[aux_size]:
		is_palindrome = False
		break
	aux_size = aux_size - 1

print is_palindrome
