# O( n )

nums = [1, 2, 3]
sum(nums)  # sum of array
for n in nums:  # looping
    print(n)

nums.insert(1, 100)  # insert middle
nums.remove(100)  # remove middle
print(100 in nums)  # search

import heapq

heapq.heapify(nums)  # build heap

# sometimes even nested loops can be O(n)
# (e.g. monotonic stack or sliding window)
