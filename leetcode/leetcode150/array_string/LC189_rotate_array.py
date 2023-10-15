"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        raise NotImplementedError()
    
class Solution1(Solution):
    def reverse(self, nums: List[int], s: int, e: int):
        while s < e:
            temp = nums[s]
            nums[s] = nums[e - 1]
            nums[e - 1] = temp
            s += 1
            e -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        '''
            input = part1(pivot)part2
            result = part2part1
            
            dive into par1, part2
            1,2,3,4,5,6,7 k=3
            1,2,3,4 | 5,6,7
              part1    part2
            4,3,2,1 | 7,6,5
            revert part1, and part2
            5,6,7 | 1,2,3,4
            revert whole list in the end
        '''
        # no need to the rotation exceed length of nums
        k = k % len(nums)    
        self.reverse(nums, 0, len(nums) - k)
        self.reverse(nums, len(nums) - k, len(nums))
        self.reverse(nums, 0, len(nums))

class Solution2(Solution):
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        use built-in method
        '''
        n=len(nums)
        k=k%n
        nums[:] =nums[n-k:] + nums[:n-k]