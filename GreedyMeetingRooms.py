"""
Given a list of intervals: [start, end] for meetings. Find the least number of meeting rooms required.

Constraints:
1 <= N <= 1e5
1<= A[i][0] <= A[i][1] <= 1e9

Example:
Input: [[5,10], [15,20], [0,30]]
Output: 2

Explanation:
[0,30] and [5,10] take place simultaneously. Same for [0,30] and [15,20]
"""
# Thought: We only care about the places where the change happens.
# From the example above we can deduce that at time (5, 15, 0) we increase the current meeting room requirement by 1 (+1)
# And when we hit time (10, 20, 30) we decrease the room requirement by 1 (-1)
# Therefore, we create tuples to solve this problem such as (0, +1), (5, +1), (10, -1)...

def meeting_room(meeting_times: list[list[int, int]]) -> int:
    curr_req = 0
    max_req = 0
    meeting_req = []
    for start, end in meeting_times:
        meeting_req.append((start, 1))
        meeting_req.append((end, -1))
    meeting_req.sort()
    for _, need in meeting_req:
        curr_req += need
        max_req = max(curr_req, max_req)
    return max_req

print(meeting_room([[5,10], [15,20], [0,30]]))