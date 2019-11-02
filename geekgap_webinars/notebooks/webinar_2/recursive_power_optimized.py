def power_optimized(x, n):
    """Compute x to the power_optimized of n (with n>=0)"""

    #1- base case
    if n == 0:
        return 1

    #2- solve sub-problems
    squared_power = power_optimized(x, n//2)

    #3- combine sub-solutions
    if n %2 == 0:
        res = squared_power * squared_power
    else:
        res = x * squared_power * squared_power

    return res


if __name__ == '__main__':
    power_optimized(2, 0)
    power_optimized(2, 4)
    power_optimized(2, 5)