import os

"""
The os functions that we are given are:
os.path.getsize(path)
os.path.isfile(path)
os.listdir(path)
os.path.join(path, filename)
"""


def disk_usage_tail_recursion(path, size_so_far=0):
    """
    Tail recursion implementation of the disk usage function.
    """

    size_so_far += os.path.getsize(path)

    # 1- base case
    if os.path.isfile(path):
        print('{0:<7}'.format(size_so_far), path)
        return size_so_far

        # 2- solve sub-problems step
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        size_so_far = disk_usage_tail_recursion(child_path, size_so_far)

    # 3- combine sub-solutions
    # no need

    print('{0:<7}'.format(size_so_far), path)
    return size_so_far


if __name__ == '__main__':
    disk_usage_tail_recursion('/Users/junior/geekgap/Repos/geekgap_webinars')