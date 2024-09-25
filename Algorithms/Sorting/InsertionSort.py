# Time Complexity:
# Space Complexity:

# Resources:
# https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/
# https://www.geeksforgeeks.org/insertion-sort/
# https://neetcode.io/courses/dsa-for-beginners/10


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp
            j -= 1
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

    insertionSort(arr)

    print("\nSorted array is")
    print_list(arr)
