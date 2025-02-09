def merge_sort(arr):
    """
    Sorts a list using the merge sort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        A new sorted list.  (Or sorts the list in place if you prefer that approach)
    """

    if len(arr) <= 1:
        return arr  # Base case: Already sorted

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)  # Recursively sort the left half
    right = merge_sort(right) # Recursively sort the right half

    return merge(left, right)  # Merge the sorted halves


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left: The first sorted list.
        right: The second sorted list.

    Returns:
        A new sorted list containing all elements from left and right.
    """

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from left or right
    merged.extend(left[left_index:])  # Efficiently extend using slices
    merged.extend(right[right_index:])

    return merged


# Example usage:
my_list = [5, 2, 8, 1, 9, 4]
sorted_list = merge_sort(my_list)
print("Sorted list:", sorted_list)  # Output: Sorted list: [1, 2, 4, 5, 8, 9]

# Example of sorting in-place (modifying original list) if you prefer:
def merge_sort_in_place(arr):
    def _merge_sort(arr, start, end):
        if end - start <= 1:  # Base case: sublist of size 0 or 1
            return

        mid = (start + end) // 2
        _merge_sort(arr, start, mid)  # Sort left half
        _merge_sort(arr, mid, end)  # Sort right half
        _merge(arr, start, mid, end)  # Merge the sorted halves

    def _merge(arr, start, mid, end):
        left = arr[start:mid]
        right = arr[mid:end]

        left_index = 0
        right_index = 0
        merged_index = start

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                arr[merged_index] = left[left_index]
                left_index += 1
            else:
                arr[merged_index] = right[right_index]
                right_index += 1
            merged_index += 1

        arr[merged_index:end] = left[left_index:] or right[right_index:]  # Efficiently copy remaining elements

    _merge_sort(arr, 0, len(arr))


my_list_in_place = [5, 2, 8, 1, 9, 4]
merge_sort_in_place(my_list_in_place)
print("Sorted list in-place:", my_list_in_place) # Output: Sorted list in-place: [1, 2, 4, 5, 8, 9]