def removeElement(nums, val):
    index = 0

    for i in nums:

        if i == val:
            continue
        else:
            nums[index] = i
            index += 1

    return index
