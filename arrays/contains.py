def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


nums = [3, 5, 1, 7, 3]
print(contains_duplicate(nums))
