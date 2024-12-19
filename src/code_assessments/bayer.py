# Use urllib.request to send network request if needed.

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line

def code_here():
    # We'll make this nicer later
    splitData = inputData.split("\n")
    Arr, Sum = list(map(int, splitData[0].split(" "))), int(splitData[1])
    # Arr = [int(x) for x in Arr]
    print(Arr)
    print(Sum)
    
    # Brute Force
    list_pairs = []
    for i in range(len(Arr)):
        for j in range((i + 1), len(Arr)):
            print(f"Testing {type(Arr[i])} + {type(Arr[j])}")
            if Arr[i] + Arr[j] == Sum:
                print("found a sum")
                list_pairs.append([Arr[i], Arr[j]])
    if list_pairs == []:
        return "No Pairs Found"
    else:
        return list_pairs

    # I still need to convert the list of pairs to different lines to be read as input.

    # Use the function to return the solution.
print(code_here())
