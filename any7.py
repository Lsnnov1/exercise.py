def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE

    # LOOP THROUGH 
    for number in nums:
        # IF NUMBER EQUALS 7 RETURN TRUE OTHERWISE FALSE
        if number == 7:
            return True
    return False
    

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

