"""
Given a list of intervals: [start, end]. Find the length of the maximal set of mutually disjoint intervals.

Constraints:
1 <= N <= 1e5
1 <= A[i][0] <= A[i][1] <= 1e9

Input: [[1,2], [2,10], [4,6]]
Output: 2
"""

# Test Case: [[1,4], [2,3], [4,6], [8,9]]
# We can see a pattern and it seems like for maximal disjoint sets, we need a set that ends early (hypothesis: starts early?)

def disjoint_intervals(intervals: list[int]) -> int:
    intervals.sort(key = lambda x: x[1])
    prev_end = intervals[0][1]
    count = 1
    for start, end in intervals:
        if start <= prev_end:
            pass
        else:
            prev_end = end
            count += 1
    return count

intervals = [[1,2], [2,10], [4,6]]
intervals2 = [[1,4], [2,3], [4,6], [8,9]]

print(disjoint_intervals(intervals))
print(disjoint_intervals(intervals2))