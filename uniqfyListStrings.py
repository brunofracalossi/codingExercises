values = ['test', 'd','a','b','a','c','c','a','b','d']

def uniqfy(list):
   	# Not order preserving
   	keys_array = {}
   	for e in list:
   		#print e
		keys_array[e] = 1
	print keys_array
   	return keys_array.keys()

seq = uniqfy(values)
print seq