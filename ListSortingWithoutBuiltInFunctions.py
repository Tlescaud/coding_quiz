def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
input_list = [4, 2, 9, 1]
sorted_list = bubble_sort(input_list)
print(sorted_list)  


'''In this program:

The bubble_sort function takes a list arr as input.

The outer for loop runs n times, where n is the length of the list.

The inner for loop iterates through the list, comparing adjacent elements.

If an element is greater than the next element, they are swapped.

This process is repeated until the entire list is sorted.

Finally, the sorted list is returned.'''
