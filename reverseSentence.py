sentence = "Hello what is your name"
count_words = 0
words = {}
reverse_sentence = ""
new_word = ""

for i in xrange(len(sentence)):
	if sentence[i] == " ":
		count_words = count_words + 1
		words[count_words] = new_word
		new_word = ""
	else:
		new_word = new_word + sentence[i]

count_words = count_words + 1 #count last word
words[count_words] = new_word #add last word

while count_words > 0:
	reverse_sentence = reverse_sentence + words[count_words] + " "
	count_words = count_words - 1

print reverse_sentence

