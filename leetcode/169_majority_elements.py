def majority_elements_1(nums):
    counts = {}
    measure = len(nums) // 2
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > measure:
            return num


def majority_elements_2(nums):
    nums.sort()
    return nums[len(nums)//2]


def majority_elements(nums):
    major = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            count += 1
            major = nums[i]
        elif major == nums[i]:
            count += 1
        else:
            count -= 1
    return


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_elements(nums))

