# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
    number = raw_input()
    count = 0
    for i in xrange(len(number)):
        if int(number[i]) != 0:
            if int(number) % int(number[i]) == 0:
                count = count + 1
    print count