arr1 = [1,2,3,4,5] #sets arrays.
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
a_set = set(arr1) #makes arrays sets.
b_set = set(arr2)
c_set = set(arr3)
l1 = len(arr1) #gets length of arrays.
l2 = len(arr2)
l3 = len(arr3)
while True:
        if l1 >= 1 and l1 <= 1000 and l2 >= 1 and l2 <= 1000 and l3 >= 1 and l3 <= 1000: #Checks to see that the array length is between 1 and 2000.
            print ("the elements in all arrays are ")
            result = list(a_set.intersection(b_set, c_set)) # puts common elements in a list.
            print(result)
            if result == []: #if no common elements lets users know.
                print("No common elements")
            break
        else:
            print ("Error, try again.")