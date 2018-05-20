#program for linear search in python
def linearSearch(array, key):

    #searching key from starting in array until end of the array

    for index in range(len(array)):
        
        if array[index] == key:
            return index

    return -1

array = [2,3,5,23,6,7,2,12,4]

key = 7

result = linearSearch(array,key)

if(result != -1):
    print "Key is found at index :",result
else:
    print "Key is not found in array"