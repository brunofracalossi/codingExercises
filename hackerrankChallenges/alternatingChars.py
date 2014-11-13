# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = []
n_tests = input()

for i in xrange(n_tests):
    tc = raw_input()
    tests.append(tc)
    
for i in xrange(len(tests)):
    word = tests[i]
    deletes = 0
    for i2 in xrange(len(word) - 1):
        if word[i2] == word[i2 + 1]:
            deletes = deletes + 1
    print deletes
            