"""
Given N bulbs, either On (1) or Off (0). Turning on the ith bulb causes all remaining bulbs on the right to flip.

Find the minimum number of switches to turn all the bulbs on.

Constraints:
1 <= N <= 1e5
A[i] = {0,1}
"""

# For the test case of [1,0,1], we'll have a running cost (starting from 0) everytime we wish to flip a switch from 0 to 1 
# (and subsequently all the remaing switches to the right) at ith index. If the value is 1 already, move to the next index
# For the algorithm above, the Time complexity is O(N*N) and space is O(1) (Naive approach)

# For the optimized solution, we also take into account of the cost value and see if it is odd or even when we reach an
# arbitrary value in the array. If the cost is even, don't flip the value. If it is odd, flip the value.

def bulbs(bulb_array: list[int]) -> int:
    cost = 0
    for bulb in bulb_array:
        if cost % 2 == 1:   #
            bulb = not bulb
        if bulb % 2 == 0:
            cost += 1
    return cost

# Same logic as above, but a little easier to follow:

def bulbs_v2(bulb_array: list[int]) -> int:
    cost = 0
    for bulb in bulb_array:
        if cost % 2 == 0:
            pass                # bulb = bulb   leaving it, as is   
        else:
            bulb = not bulb
        if bulb % 2 == 1:
            pass                # if the value is already 1, do nothing
        else:
            cost += 1
    return cost

bulbs1 = [1,0,1]
bulbs2 = [1,0,1,1,1,0,0,1,0,1]

print(bulbs(bulbs1))
print(bulbs_v2(bulbs1))
print(bulbs(bulbs2))
print(bulbs_v2(bulbs2))