# Enter your code here. Read input from STDIN. Print output to STDOUT
array_tests = ["aaab", "aa", "cabba"]
n_tests = len(array_tests)

#for i in xrange(n_tests):
#    tc = raw_input()
#    array_tests.append(tc)

def isPalindrome(word):
    is_palindrome = True
    size = len(word) - 1
    for i in xrange(size / 2):
        if word[i] != word[size]:
            is_palindrome = False
        size = size -1
    
    return is_palindrome

def removeAndCheckIfIsPalindrome(string, pos):
    new_string = ""
    for i in xrange(len(string)):
        if i != pos:
            new_string = new_string + string[i]

    return isPalindrome(new_string)
        
for i in xrange(len(array_tests)):
    size   = len(array_tests[i]) - 1
    length = len(array_tests[i])
    for i2 in xrange(len(array_tests[i]) / 2):
        if array_tests[i][i2] != array_tests[i][size]:
            if removeAndCheckIfIsPalindrome(array_tests[i], i2):
                pos_remove = i2
            else:
                pos_remove = size
            is_palindrome = False
            break
        else:
            is_palindrome = True
        size = size - 1
    
    if is_palindrome == True:
        print -1
    else:
        print pos_remove
    
            
        
