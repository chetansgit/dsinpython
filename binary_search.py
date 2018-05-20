#program for binary search
def binarySearch(array, left, right, key) :
    
    if right >= left :
        mid = (left + right  + 1)/ 2
       
        #if element is present at the middle itself
        if array[mid] == key:
            return mid
        
        #if element is smaller than mid then it can be present in left subarray
        elif array[mid] > key:
            return binarySearch(array, left, mid - 1, key)
        
        #else element can only be present in right subarray
        else:
            return binarySearch(array, mid + 1, right, key)
    else:
        return -1

#test array
array = [2,3,6,7,9,12,45,77]
key = 7

#calling search function
result = binarySearch(array, 0, len(array) - 1, key)

if result != -1:
    print "Element is present at index %d"%result
else:
    print "Element is not found in array"


