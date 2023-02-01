def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return l

def find_num_pos(arr, x):
    arr = sorted(arr)
    pos = binary_search(arr, x)
    if pos >= len(arr) or arr[pos] != x:
        if pos == 0:
            return None, None, None
        else:
            return pos - 1, pos, None
    else:
        i = pos
        while i >= 0 and arr[i] == x:
            i -= 1
        j = pos
        while j < len(arr) and arr[j] == x:
            j += 1
        return i, pos, j

input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]
target = int(input("Enter a number to find its position in the list: "))

a, b, c = find_num_pos(numbers, target)
if a is None:
    print("The number is not in the list and it would be the first element if it were added to the list")
else:
    if c is None:
        print(f"The number is in the list and its position is {b}")
    else:
        print(f"The number is not in the list and it would be the element at position {b} if it were added to the list")
