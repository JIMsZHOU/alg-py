"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        raise NotImplementedError
    
class Solution1(Solution):
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        # two pointers, head and tail
        p1, p2 = 0, len(nums) - 1
        # move two pointer towards middle, break loop when 2 pointers meet
        while p1 <= p2:
            # find val in arr equals to input
            if nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
        return p1

def test():
    """
    Test function for the removeElement method of Solution1 class.
    """
    solution = Solution1()
    nums1 = [3,2,2,3]
    val1 = 3
    expected_output1 = 2
    expected_nums1 = [2,2]
    output1 = solution.removeElement(nums1, val1)
    assert output1 == expected_output1, f"Error: expected {expected_output1}, but got {output1}"
    assert nums1[:expected_output1] == expected_nums1, f"Error: expected {expected_nums1}, but got {nums1[:expected_output1]}"

    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    expected_output2 = 5
    expected_nums2 = [0,1,4,0,3]
    output2 = solution.removeElement(nums2, val2)
    assert output2 == expected_output2, f"Error: expected {expected_output2}, but got {output2}"
    assert nums2[:expected_output2] == expected_nums2, f"Error: expected {expected_nums2}, but got {nums2[:expected_output2]}"

    nums3 = [1]
    val3 = 1
    expected_output3 = 0
    expected_nums3 = []
    output3 = solution.removeElement(nums3, val3)
    assert output3 == expected_output3, f"Error: expected {expected_output3}, but got {output3}"
    assert nums3[:expected_output3] == expected_nums3, f"Error: expected {expected_nums3}, but got {nums3[:expected_output3]}"

    nums4 = [1, 2, 3, 4, 5]
    val4 = 6
    expected_output4 = 5
    expected_nums4 = [1, 2, 3, 4, 5]
    output4 = solution.removeElement(nums4, val4)
    assert output4 == expected_output4, f"Error: expected {expected_output4}, but got {output4}"
    assert nums4[:expected_output4] == expected_nums4, f"Error: expected {expected_nums4}, but got {nums4[:expected_output4]}"

    nums5 = [1, 1, 1, 1, 1]
    val5 = 1
    expected_output5 = 0
    expected_nums5 = []
    output5 = solution.removeElement(nums5, val5)
    assert output5 == expected_output5, f"Error: expected {expected_output5}, but got {output5}"
    assert nums5[:expected_output5] == expected_nums5, f"Error: expected {expected_nums5}, but got {nums5[:expected_output5]}"

    nums6 = []
    val6 = 0
    expected_output6 = 0
    expected_nums6 = []
    output6 = solution.removeElement(nums6, val6)
    assert output6 == expected_output6, f"Error: expected {expected_output6}, but got {output6}"
    assert nums6[:expected_output6] == expected_nums6, f"Error: expected {expected_nums6}, but got {nums6[:expected_output6]}"

test()