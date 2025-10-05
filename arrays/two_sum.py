def two_sum(nums, target):
    know_numbers = {}

    for idx, num in enumerate(nums):
        desire = target - num
        if desire in know_numbers:
            return [know_numbers[desire]]



nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))