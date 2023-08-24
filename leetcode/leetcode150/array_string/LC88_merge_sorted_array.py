"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        raise NotImplementedError
    
class Solution1(Solution):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # solution 1: sort
        # time: O((m+n)log(m+n))
        # space: O(1)
        nums1[:] = sorted(nums1[:m] + nums2)

class Solution2(Solution):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # solution 2: two pointers
        # time: O(m+n)

        # two pointers to go thourgh nums1, nums2 from tail
        p1, p2 = m -1, n -1
        # pointer track the posistion to insert value to nums1
        insert = m + n -1

        # break loop when p1 or p2 equals to 0
        while p1 >= 0 and p2 >= 0:
            # insert greater value
            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 = p1 -1
            else:
                nums1[insert] = nums2[p2]
                p2 = p2 -1
            # every loop need move insert posistion left
            insert = insert -1
        
        #  if there are still elements in nums2
        # copy them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]
