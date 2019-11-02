def factorial(n):
    #1- base case
    if n <= 1:
        return 1

    #2- solve sub-problems
    previous_factorial = factorial(n-1)

    #3- combine sub-solutions
    res = n * previous_factorial

    return res

if __name__ == '__main__':
    factorial(0)
    factorial(1)
    factorial(5)
