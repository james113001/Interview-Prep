"""  """
from typing import List

def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    
    lo, hi = 0, len(nums)-1
    while lo <=hi:
        mid = (lo+hi)//2
        
        if nums[mid]==target:
            return mid
        if nums[lo] <= nums[mid]:
            #left side is sorted
            if nums[lo]<=target<nums[mid]:
                hi = mid-1
            #if not, target must be on right side
            else:
                lo= mid + 1
        else:
            #right side sorted
            if nums[hi]>=target>nums[mid]:
                lo = mid + 1
            #if not, target must be on left side
            else:
                hi= mid - 1
    return -1