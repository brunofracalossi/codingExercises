word = raw_input()

def canBePalindrome(string):
    # (all_chars - 1) from string needs to have count_char % 2 resulting in 0
    chars = {}

    for i in xrange(len(string)):
        if string[i] in chars:
            chars[string[i]] = chars[string[i]] + 1
        else:
            chars[string[i]] = 1

    count = 0
    for i in chars:       
        if chars[i] % 2 != 0:
            count = count + 1
    if count > 1:
        return False
    else:
        return True

if canBePalindrome(word) == True:
    print "YES"
else:
    print "NO"