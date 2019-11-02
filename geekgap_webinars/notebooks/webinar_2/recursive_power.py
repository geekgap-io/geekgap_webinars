def power(x, n):
    """Compute x to the power of n (with n>=0)"""

    #1- base case
    if n == 0:
        return 1

    #2- solve sub-problems
    previous_power = power(x, n-1)

    #3- combine sub-solutions
    res = x * previous_power

    return res


if __name__ == '__main__':
    power(2, 0)
    power(2, 4)
    power(2, 5)