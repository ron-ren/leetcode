'''

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):
            return(0)
    
        new_nums=sorted(nums)
        
        p=0
        for i in range(len(nums)):
            if(nums[i]!=new_nums[i]):
                p=i
                break
        q=0
        
        for i in range(len(nums)):
            if(nums[len(nums)-1-i]!=new_nums[len(nums)-1-i]):
                q=len(nums)-1-i
                break
        if(q>p):
            return(q-p+1)
        else:
            return(0)
            