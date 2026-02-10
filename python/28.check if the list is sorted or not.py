def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage
numbers = [1, 2, 3, 4, 5]

if is_sorted(numbers):
    print("List is sorted")
else:
    print("List is not sorted")
