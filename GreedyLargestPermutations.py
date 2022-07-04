"""
Given an array A of a random permutation of numbers from 1 to N. Given B, the number of swaps in A that we can make.
Find the largest permutation possible.

Constraints:
1 <= N <= 1e6
1 <= B <= 1e9

Example:
Input: A = [1,3,2], B = 1
Output = [3,1,2]

Explanation:
N = 3
Since we can make B = 1 swaps, we swap 1 and 3
"""

# Hypothesis: We can greedily replace the higher elements in N -> N-1 -> N-2 ...

def largest_permutation(num_list: list[int], swaps: int) -> list[int]:
    ind = 0
    max_size_val = len(num_list)
    num_dict = {val: index for index, val in enumerate(num_list)}
    while swaps > 0 and ind < len(num_list):
        curr_ind = num_dict[max_size_val]
        if ind != curr_ind:
            swaps -= 1
            num_list[ind], num_list[curr_ind] = num_list[curr_ind], num_list[ind]
            num_dict[num_list[ind]], num_dict[num_list[curr_ind]] = num_dict[num_list[curr_ind]], num_dict[num_list[ind]]
        ind += 1
        max_size_val -= 1
    return num_list

print(largest_permutation([1,3,2], 1))
print(largest_permutation([3,2,4,1,5], 3))