#!https://www.hackerrank.com/challenges/insertionsort2

def printArray(array):
    for i in xrange(len(array)):
        print array[i],
    print ""
    
def insertionSort(array):
    for i in xrange(1, len(array)):
        compare = True
        ind = 0
        while (compare == True) and (ind < i):
            if array[i] < array[ind]:
                compare = False
                aux   = array[i]
                aux_i = i - 1
                while aux_i >= ind:
                    array[aux_i + 1] = array[aux_i]
                    aux_i = aux_i - 1
                array[ind] = aux
            ind = ind + 1
        printArray(array)
        
size = input()
array = [int(i) for i in raw_input().strip().split()]
insertionSort(array)
