"""
Given an array of integers of length N. Majority element occurs with a frequency > N/2. Find the majority element.

Constraints:
1 <= N <= 1e6

Example:
Input: [3,2,2,4,2,2]
Output: 2

Explanation:
2 occurs with the frequency of 2 > (6/2 = 3)
"""

from collections import Counter

# This takes O(N) Time and O(N) Space Complexity.
def majority_element_v1(elements: list[int]) -> int:
    return Counter(elements).most_common(1)[0][0]

# This has O(N) Time (O(log(w).N) to be exact) and O(1) Spacce Complexity. We do this by thinking in terms of bits.
# The majority in each bit space is taken and the result will be the answer (majority elememnt) that we are looking for.
def majority_element_v2(elements: list[int]) -> int:
    n = len(elements)
    result = 0
    for bit in range(32):   #iterating over the columns of bits
        num_of_ones = 0
        for num in elements:
            if (1 << bit) & num:
                num_of_ones += 1
        if num_of_ones > n // 2:
            result |= (1 << bit)
    return result

elements = [3,2,2,4,2,2]
print(majority_element_v1(elements))
print(majority_element_v2(elements))