# O( nlogn )

# HeapSort
import heapq

nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)  # O(n)
while nums:
    heapq.heappop(nums)  # O(logn)

# MergeSort (and most built-in sorting functions)
