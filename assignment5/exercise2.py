def sort_list(numbers):
    nums = numbers.copy()             
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:  
                nums[j], nums[j + 1] = nums[j + 1], nums[j]   
    

my_list = [5, 2, 9, 1, 7]
my_list = [5, 8, 6, 2, 0]
print(sort_list(my_list))  