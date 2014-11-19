#https://www.hackerrank.com/challenges/insertionsort1

def printArray(array):
    for i in xrange(len(array)):
        print array[i],
    print ""
    
def insertionSort(array):
    value = array[len(array) - 1]
    
    for i in xrange(len(array) - 2):
        if value < array[i]:
            position = i
            break

    size = len(array) - 2
    while size >= position:
        array[size + 1] = array[size]
        size = size - 1
        printArray(array)
    
    array[position] = value
    printArray(array)

m = input()
array = [int(i) for i in raw_input().strip().split()]
insertionSort(array)
