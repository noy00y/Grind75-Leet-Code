def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = False
        counts = 0
        returnType = []

        while not found and counts < len(nums):
            
            for i in range(len(nums)):

                # if not same index:
                if counts != i and nums[counts] + nums[i] == target:
                    found = True
                    returnType.append(counts)
                    returnType.append(i)
                    
                    return returnType

            counts += 1

        return returnType

# Driver Code:
nums = [1, 2, 3, 4]

answer = twoSum(nums, 7)
for i in answer:
    print(i)