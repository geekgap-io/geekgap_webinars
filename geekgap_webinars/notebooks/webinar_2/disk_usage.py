import os

"""
The os functions that we are given are:
os.path.getsize(path)
os.path.isfile(path)
os.listdir(path)
os.path.join(path, filename)
"""


def disk_usage(path):
    """
    Input: a path
    Output: Total Disk Space being utilized by a folder/file
    """

    path_size = os.path.getsize(path)

    # 1- base case
    if os.path.isfile(path):
        print('{0:<7}'.format(path_size), path)
        return path_size

        # 2- solve sub-problems step
    children_size = 0
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        children_size += disk_usage(child_path)

    # 3- combine sub-solutions
    total_size = path_size + children_size

    print('{0:<7}'.format(total_size), path)
    return total_size


if __name__ == '__main__':
    disk_usage('/Users/junior/geekgap/Repos/geekgap_webinars')