# Implementation of BucketSort

# Resources:
# https://www.hackerearth.com/practice/algorithms/sorting/bucket-sort/visualize/
# https://www.geeksforgeeks.org/bucket-sort/
# https://neetcode.io/courses/dsa-for-beginners/13


def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()


# Driver code
if __name__ == "__main__":
    arr = [2, 1, 2, 0, 0, 2]
    print("Given array is")
    print_list(arr)

    bucketSort(arr)

    print("\nSorted array is")
    print_list(arr)
