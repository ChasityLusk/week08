def isSorted(nums):
    """Returns true if the list is sorted in ascending order, False otherwise."""

    if len(nums) <= 1:
        return True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True
    
