test_array = [1,50,3,5,66,7,9,2]

def secondLargest(array):
	num_1 = test_array[0]
	num_2 = test_array[1]
	for i in xrange(len(test_array)):
		if test_array[i] > num_1:
			num_2 = num_1
			num_1 = test_array[i]
		else:
			if test_array[i] > num_2:
				num_2 = test_array[i]

	return num_2


print secondLargest(test_array)