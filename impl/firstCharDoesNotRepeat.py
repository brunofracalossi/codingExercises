word = "echaae"
keys_array = {}

for i in xrange(len(word)):
	print word[i]
	if word[i] in keys_array:
		keys_array[word[i]] = keys_array[word[i]] + 1
	else:
		keys_array[word[i]] = 1

for i in xrange(len(word)):
	if keys_array[word[i]] == 1:
		first_char_not_repeat = word[i]
		break

print keys_array

print first_char_not_repeat
