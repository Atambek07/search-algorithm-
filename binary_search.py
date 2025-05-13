"""
Binary Search Algorithm in Python
This script implements the Binary Search algorithm to find an element in a sorted list.
Binary Search works by repeatedly dividing the search interval in half. If the value of the target element is less than the value of the middle element, the search continues in the left half; otherwise, it continues in the right half. The process is repeated until the target element is found or the interval is empty.
This algorithm is efficient and works only on sorted lists.
Time Complexity: O(log n) in the worst, average, and best cases.
Space Complexity: O(1) for iterative implementation or O(log n) for recursive implementation due to recursion stack.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1
    
    return -1

arr = [11, 12, 22, 25, 34, 64, 90]
target = 22
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
