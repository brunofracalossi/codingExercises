array_1 = [1,5,7,15,66,67,68,1001,1002]
array_2 = [2,3,4,6,8,68,70,999,1000,1003]

new = []

pos_1 = 0
pos_2 = 0

print "Len 1: " + str(len(array_1))
print "Len 2: " + str(len(array_2))
keep = True

last_append = 312313113

#while we didn't go trough all positions from both arrays
while keep:
	if pos_1 == len(array_1) - 1 and pos_2 == len(array_2) - 1:
		keep = False

	print pos_1, pos_2

	if array_1[pos_1] < array_2[pos_2]:
		if last_append != array_1[pos_1]:
			new.append(array_1[pos_1])
			last_append = array_1[pos_1]
			pos_1 = pos_1 + 1
		else:
			new.append(array_2[pos_2])
			pos_2 = pos_2 + 1
	elif array_2[pos_2] < array_1[pos_1]:
		if last_append != array_2[pos_2]:
			new.append(array_2[pos_2])
			last_append = array_2[pos_2]
			pos_2 = pos_2 + 1
		else:
			new.append(array_1[pos_1])
			pos_1 = pos_1 + 1
	else: # if elements are equal
		if last_append != array_1[pos_1]:
			new.append(array_1[pos_1])
			last_append = array_1[pos_1]
		
		if pos_2 < len(array_2):
			pos_2 = pos_2 + 1
		if pos_1 < len(array_1):
			pos_1 = pos_1 + 1

	# to avoid index out of bounds
	if pos_1 == len(array_1):
		pos_1 = len(array_1) - 1
	if pos_2 == len(array_2):
		pos_2 = len(array_2) - 1

	print new

print new

