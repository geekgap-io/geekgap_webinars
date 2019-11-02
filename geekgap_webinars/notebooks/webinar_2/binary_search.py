def helper(A, k, left, right):
    """binary search of k in A[left:right], return True if found, False otherwise"""
    print(f'so far ==> left={left}, right={right}, k={k}, A={A}')

    #1- base case
    if left > right:
        # if empty list there is nothing to search
        return False

    #2- solve the subproblems
    mid = (right - left)//2 + left
    if A[mid] < k:
        left = mid + 1 # -> search right
        return helper(A, k, left, right)
    elif A[mid] > k:
        right = mid - 1 # -> search left
        return helper(A, k, left, right)
    else:
        return True


    #3- combine the sub-solutions
    # nothing to combine --> tail recursion(stay tunned for more)


def binary_search(A, k):
    """binary search of k in A, return index if found, -1 otherwise"""
    return helper(A, k, 0, len(A)-1)


if __name__ == '__main__':
    A = [5, 8, 8, 15, 16, 19, 30, 35, 40, 51]
    binary_search(A, 15)
    print('')
    binary_search(A, 100)
    print('')
    binary_search(A, 51)

