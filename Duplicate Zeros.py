"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

 

Note:

    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
"""
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr2 = [i for i in arr]
        print(arr2)
        i=0
        j = 0
        while i < len(arr):
            print("J" + str(j))
            print("I" + str(i))
            print("arr2[j]" + str(arr2[j]))
            if not arr2[j]:
                #arr[i] = 0
                print("inside loop")
                print("I: " + str(i) + "J: " + str(j))
                i+=1
                if i<len(arr):
                    arr[i] = 0
            else:
                arr[i] = arr2[j]
            j+=1
            i+=1        
                
        return arr
