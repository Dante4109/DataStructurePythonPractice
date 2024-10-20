# O( c^n )


# c branches, where c is sometimes n.
def recursion(i, nums, c):
    if i == len(nums):
        return 0

    for j in range(i, i + c):
        branch = recursion(j + 1, nums)
