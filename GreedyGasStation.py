"""
There are N gas stations along a circular route.
Each has A[i] amounty of gas. To travel from station i -> i+1, there is a cost B[i].
Find the earliest station from where you can travel around the entire circuit. Return -1 if not possible.

Constraints:
1 <= N <= 1e6
"""

def circular_gas_station(gas: list[int], cost: list[int]) -> int:
    start = 0
    curr = 0
    n = len(gas)
    for ind, (gas_val, cost_val) in enumerate(zip(gas * 2, cost * 2)):
        if ind == start + n:
            return start
        curr += gas_val - cost_val
        if curr < 0:
            start = ind + 1 # Optimizing since all the middle values would've contributed to the negative current value so far
            curr = 0
    return -1

gas_list = [3,5,2,1,7]
cost_list = [4,2,1,9,1]

print(circular_gas_station(gas_list, cost_list))