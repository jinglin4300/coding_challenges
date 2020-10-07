"""
Question:
https://app.codility.com/programmers/challenges/
There are N rectangular buildings standing along the road next to each other. 
The K-th building is of size H[K] × 1.

Because a renovation of all of the buildings is planned, we want to cover 
them with rectangular banners until the renovations are finished. 
Of course, to cover a building, the banner has to be at least as high as 
the building. We can cover more than one building with a banner if it is wider than 1.

We can order at most two banners and we want to cover all of the buildings. 
Also, we want to minimize the amount of material needed to produce the banners.

What is the minimum total area of at most two banners which cover all of the buildings?
that, given an array H consisting of N integers, returns the minimum total area of at most two banners that we will have to order.
"""


def solution(H):
    # write your code in Python 3.6
    if len(H) == 0:
        return 0
    if len(H) <= 2:
        return sum(H)

    left_max = []
    curr_max = 0
    for i in range(len(H)):
        curr_max = max(curr_max, H[i])
        left_max.append(curr_max)
    right_max = []
    curr_max = 0
    for i in range(len(H) - 1, -1, -1):
        curr_max = max(curr_max, H[i])
        right_max.append(curr_max)
    right_max.reverse()

    smallest = float("inf")
    for i in range(1, len(H)):
        # partition on i: left includes num up to i, right includes rest of nums
        area = i * left_max[i - 1] + (len(H) - i) * right_max[i]
        if area < smallest:
            smallest = area
    return smallest
