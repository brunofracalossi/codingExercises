import sys

number = float(sys.argv[1])

square_root = number
find_sq_root = False
no_square_root = False

while not find_sq_root:
	if number >= 1:
		sq = round(square_root * square_root,1)
	else:
		sq = round(square_root * square_root,3)
	print sq
	if sq == number:
		find_sq_root = True
	else:
		if square_root < 1:
			square_root = square_root + 0.001
		else:
			square_root = square_root - 0.001

	if square_root <= 0:
		find_sq_root = True
		no_square_root = True

	if sq < number and number > 1:
		find_sq_root = True
		no_square_root = True

if no_square_root:
	print "There is no square root for num " + str(number)
else:
	print "Square root of " + str(number) + " is " + str(round(square_root,3))
