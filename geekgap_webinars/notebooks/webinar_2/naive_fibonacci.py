def fibonacci(n):
    """naive implementation of the fibonacci algorithm"""
    print(f'computing fibonacci({n})')

    #1- base case
    if n <= 1:
        return n

    #2- solve the sub-problems
    previous_fib = fibonacci(n-1)
    previous_previous_fib = fibonacci(n-2)

    #3- combine the sub-solutions
    res = previous_fib + previous_previous_fib

    return res


if __name__ == '__main__':
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(10))
    # print(fibonacci(40))
