"""
Given an array of N integers. Find the highest product by multiplying 3 elements.

Constraints:
3 <= N <= 5e5

Example:

Input: [1,2,3,4]
Output: 24 (2*3*4)

Input: [0,-1,10,7,5]
Output: 350 (5*7*10)
"""

# A naive approach where we sort the array in descending order, and take the product of the three largest numbers
def highest_product_naive(nums: list[int]) -> int:
    nums = sorted(nums, reverse=True)
    return nums[0] * nums[1] * nums[2]
# Note that this logic fails for the third test case

# We need to consider the case where the product of 2 negative numbers along with the positive number is also considered.
# Therefore, our updated logic will consider the 2 lowest negative number and the highest positive number
def highest_product(nums: list[int]) -> int:
    nums = sorted(nums, reverse=True)
    return max((nums[0]*nums[1]*nums[2]),(nums[0]*nums[-1]*nums[-2]))

nums = [1,2,3,4]
nums2 = [0,-1,10,7,5]
nums3 = [-5,-2,-1,0,0,1,1,5]

print(highest_product_naive(nums))
print(highest_product_naive(nums2))
print(highest_product_naive(nums3))     # Incorrect answer because of the nature of this logic

print(highest_product(nums))
print(highest_product(nums2))
print(highest_product(nums3))