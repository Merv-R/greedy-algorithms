"""
N kids stand in a line, each having an integer rating. We distribute candies where:
    Each kid gets at least 1 candy
    Kids with higher ratings than their neighbors get more candies.
Find the minimum candies required.

Constraints:
1 <= N <= 1e5

Example:
Input: [1,3,7,1]
Output: 7

Explanation:
Candies: [1,2,3,1]
"""

# Hypothesis: Start from the lowest ranking kids. Then work your way up, looking at the ratings on both sides.

def distribute_candy(ratings: list[int]) -> int:
    num_kids = len(ratings)
    candies = [1] * num_kids
    val_ind_pair = sorted([(val, ind) for ind, val in enumerate(ratings)])
    for _, ind in val_ind_pair:
        if ind > 0 and ratings[ind] > ratings[ind - 1]:
            candies[ind] = max(candies[ind], candies[ind - 1] + 1)
        if ind < num_kids - 1 and ratings[ind] > ratings[ind + 1]:
            candies[ind] = max(candies[ind], candies[ind + 1] + 1)
    print(candies)
    return sum(candies)

print(distribute_candy([1,3,7,1]))
print(distribute_candy([1,2,7,4,3,3,1]))