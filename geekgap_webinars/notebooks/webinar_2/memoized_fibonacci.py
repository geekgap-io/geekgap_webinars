memo = dict()
def memoized_fibonacci(n):
    """memorized implementation of the fibonacci algorithm"""
    # check first if in memo
    if n in memo: return memo[n]

    print(f'computing memoized_fibonacci({n})')
    #1- base case
    if n <= 1:
        # save the result in memo
        memo[n] = n
        return n

    #2- solve the sub-problems
    previous_fib = memoized_fibonacci(n-1)
    previous_previous_fib = memoized_fibonacci(n-2)

    #3- combine the sub-solutions
    res = previous_fib + previous_previous_fib

    # save the result in memo
    memo[n] = res

    return res


if __name__ == '__main__':
    print(memoized_fibonacci(4))
    print(memoized_fibonacci(5))
    print(memoized_fibonacci(10))
    print(memoized_fibonacci(40))
