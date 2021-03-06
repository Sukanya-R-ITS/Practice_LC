"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

"""


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
    
        # for i in range(len(arr)):
        #     if i+1<=len(arr)-1:   
        #         arr[i]=max(arr[i+1:]) 
            
        arr=[max(arr[i+1:])  if i<len(arr)-1 else -1 for i in range(len(arr))]    
            
        return arr
       
       
       
---------------------
""" 
Efficent solution
sample 14900 KB submission

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(arr)):
            arr[i-1] = max(arr[i:]) 
        arr[-1]=-1
        
        return arr

"""
