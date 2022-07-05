"""
There are N mice and N holes. A mice takes 1 minute to travel 1 unit left or right.
Find the minimum time after which all mice are in holes.

Constraints:
1 <= N <= 1e5
-1e9 <= A[i] <= B[i] <= 1e9

Example:
Input: [3,2,-4], [0,-2,4]
Output: 2

Explanation:
-4 -> -2    : 2
2  -> 0     : 2
3  -> 4     : 1
"""

def mice_to_holes(mice_pos: list[int], hole_pos: list[int]) -> int:
    mice_pos.sort()
    hole_pos.sort()
    min_time = 0
    for mice, hole in zip(mice_pos, hole_pos):
        min_time = max(min_time, abs(mice - hole))
    return min_time

print(mice_to_holes([3,2,-4],[0,-2,4]))