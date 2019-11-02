def very_bad_binary_search(A, k):
    """
    Buggy binary search of k in A, return True if found, False otherwise
    Because of this bug, the following implementation complexity is:
     - Time: linear and not logarithmic
    """
    left, right = 0, len(A)-1
    print(f'so far ==> left={left}, right={right}, k={k}, A={A}')

    # 1- base case
    if len(A) == 0:
        # if empty list there is nothing to search
        return False

    # 2- solve the subproblems
    mid = (right - left)//2 + left
    if A[mid] < k:
        left = mid + 1 # -> search right
        return very_bad_binary_search(A[left:right+1], k) #BUG HERE
    elif A[mid] > k:
        right = mid - 1 # -> search left
        return very_bad_binary_search(A[left:right+1], k) #BUG HERE
    else:
        return True

    # 3- combine the sub-solutions
    # nothing to combine --> tail recursion(stay tunned for more)

if __name__ == '__main__':
    A = [5, 8, 8, 15, 16, 19, 30, 35, 40, 51]
    very_bad_binary_search(A, 15)
    print('')
    very_bad_binary_search(A, 100)
    print('')
    very_bad_binary_search(A, 51)

