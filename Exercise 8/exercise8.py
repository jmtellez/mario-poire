class Solution(object):
    def returnar(self, nums, n): #method to get the new array.
        Solution=[] #empty array for answer.
        for i in range(n): #loop to traverse array.
            Solution.append(nums[i]) #adds elements in the x spots of the array into the empty array.  
            Solution.append(nums[i+n]) #adds elements in the y spots of the array into the empty array.  
        return Solution
               
arr = [2,5,1,3,4,7]
n = 3
l = len(arr)
ob1 = Solution() 
while True:
        if n >= 1 and n <= 500 and l == 2*n: #Checks to see that the array length is between 1 and 2000.
            print ("Your updated array is" , ob1.returnar(arr, n)) #prints out the solution of our method.
            break
        else:
            print ("Error, try again.")