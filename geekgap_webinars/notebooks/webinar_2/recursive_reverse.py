def helper(L, left, right):
    """helper function to reverse the element of a
    list(L) between left and right"""
    print(f'so far ==> left={left}, right={right}, L={L}')

    # 1- base case
    if left >= right:
        # if list has 0 or 1 element there is nothing to do
        return

    # 2- solve the sub-problems
    # 2.1 swap elements at position left and right
    L[left], L[right] = L[right], L[left]

    # 2.2 reverse elements between left+1 and right-1
    helper(L, left+1, right-1)

    #3- combine the sub-solutions
    # nothing to combine --> tail recursion(stay tunned for more)


def reverse(L):
    """Reverse a list (L) in-place recursively"""
    helper(L, 0, len(L)-1)

if __name__ == '__main__':
    L = list(range(10))
    reverse(L)

    L = list(range(30))
    reverse(L)
