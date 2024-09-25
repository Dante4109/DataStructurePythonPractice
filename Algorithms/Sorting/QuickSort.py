# Implementation of QuickSort

# Resources:
# https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/visualize/
# https://www.geeksforgeeks.org/quick-sort/
# https://neetcode.io/courses/dsa-for-beginners/12


def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr


def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()


# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_list(arr)

    quickSort(arr, 0, len(arr) - 1)

    print("\nSorted array is")
    print_list(arr)
