def numSubarraysBoundedMaximumDP(A, L, R):
    """
    Given an array of A with pos integer and two positive integer
    L and R (L<=R), 
    return number of (contiguous, non-empty) subarray st value of 
    maximum array element in the subarray is between L and R inclusive

    e.g.
    A = [2, 1, 4, 3], L = 2, R = 3
    output: 3 since three subarray meets requirement: [2], [2, 1], [3]
    """
    # think as dp problem
    # property conserved: max of subarray is always bounded
    # if dp[i] > R: no subarray ends with A[i] meets requirement
    # if dp[i] < L: only valid subarrays are the ones that valid in dp[i-1]
    #   since we can only extend to A[i] when subarrays in dp[i-1] is also valid
    # if L <= dp[i] <= R: i - start_index of current window

    start = 0
    prev_count = 0
    result = 0

    for end in range(len(A)):
        if A[end] > R:
            start = end + 1
            prev_count = 0
        elif A[end] < L:
            result += prev_count
        else:
            prev_count = end - start + 1
            result += prev_count
    return result


def numSubarraysBoundedMaximum(A, L, R):
    # simply above code bit further
    # note we can combine dp[i] < L and dp[i] in range
    # when dp[i] < L, number of valid subarray is number of elements between start and end before update,
    # excluding element from end to i
    # then as soon as we encounter dp[i] in range, all elements from start to i are valid
    ans = 0
    start = end = -1
    for i in range(len(A)):
        if A[i] > R:
            start = end = i
        elif A[i] >= L:
            end = i
        ans += end - start
    return ans
