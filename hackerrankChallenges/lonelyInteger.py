#!/usr/bin/py
def lonelyinteger(array):
    keys_array = {}
    
    for i in xrange(len(array)):
        integer = array[i]
        if integer in keys_array:
            keys_array[integer] = keys_array[integer] + 1
        else:
            keys_array[integer] = 1

    for i in xrange(len(array)):
        if keys_array[array[i]] == 1:
            return array[i]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
