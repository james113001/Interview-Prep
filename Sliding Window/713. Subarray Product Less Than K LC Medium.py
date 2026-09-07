""" You are given an array of integers nums and an integer k.

Return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106 """
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # n minimum is 1, but k min is 0
        if k <= 1:
            return 0 

        #sliding window
        count=0
        slow = 0
        prod = 1
        for fast, num in enumerate(nums):
            prod*=num
            while prod >= k:
                #guaranteed to evenly divide, but necessitate prod being int and not float
                prod //= nums[slow]
                slow+=1
            
            #by this point the window should have product< k
            #length of window = number of subarrays ending at fast
            count += fast-slow +1
        return count
# O Complexity: O(n) where n is the length of the input array.