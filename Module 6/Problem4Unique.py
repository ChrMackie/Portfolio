#Christian Mackie 11/12/2023
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

# Example usage
nums = [1, 3, 3, 3, 6, 2, 3, 5]
unique_nums = remove_duplicates(nums)
print("Original list:", nums)
print("Unique list:", unique_nums)