# Example function with tricky edge cases: Finding median of a list

def find_median(numbers):
    """
    Returns the median value of a list of numbers.
    Handles edge cases: empty list, single element, even/odd length.
    """
    if not numbers:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        # Bug 2: Incorrect median calculation for even length
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        # Bug 3: Off-by-one error for odd length
        return sorted_nums[mid + 1]

# Example usages
print(find_median([]))            # None (empty list)
print(find_median([7]))           # 7 (single element)
print(find_median([1, 2, 3]))     # 2 (odd length)
print(find_median([1, 2, 3, 4]))  # 2.5 (even length)
