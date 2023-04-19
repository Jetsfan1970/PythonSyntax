def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    num_list = nums.count(7)
    msg = True if (num_list >= 1) else False
    print(msg)
    
        

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

