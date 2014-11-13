# Enter your code here. Read input from STDIN. Print output to STDOUT
#n_tests = input()

n_tests = 2
array_tests = [0,1]

#i = 0
#for i in xrange(n_tests):
#    tc = input()
#    array_tests.append(tc)
i = 0
for i in xrange(len(array_tests)):
	height = 1
	#print i
	n_cycles = array_tests[i]
	if n_cycles == 0:
		height = 1
	else:
		for i2 in xrange(n_cycles):
			if (i2 + 1) % 2 != 0: # if we are in cycles 1,3,5,7...
				height = height * 2
			else:				  # if we are in cycles 2,4,6,8...
				height = height + 1
   	
	print height