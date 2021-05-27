arr1 = [5,7,3,9,4,9,8,3,1] #original array.
arr1.sort() 
length = len(arr1)
arr2 = [] #blank array for non duplicate elements.
greatest = -1 #set to -1 in case theres no unique elements.
while True:
        if length >= 1 and length <= 2000: #Checks to see that the array length is between 1 and 2000.
            for i in arr1: #loop to get the count for each element.
                count = arr1.count(i)
                if count == 1:  #if statements that checks if count of each element is 1 they get added to another array.
                    arr2.append(arr1[i]) #adds element thats not repeated to another array.
                    greatest = i 
            print (greatest) #prints the greatest element thats not repeated.
            break
        else:
            print ("Error, try again.")