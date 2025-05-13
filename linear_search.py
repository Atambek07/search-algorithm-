"""
Linear Search Algorithm in Python
This script implements the Linear Search algorithm to find an element in a list.
Linear Search checks each element in the list one by one, starting from the first element, until the target element is found or the end of the list is reached.
It is simple but inefficient for large lists, as it requires checking each element sequentially.
Time Complexity: O(n) in the worst, average, and best cases.
Space Complexity: O(1) as it only requires a constant amount of additional space.
"""

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
