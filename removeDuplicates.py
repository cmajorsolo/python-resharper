def solution(num):
    i = 0
    for j in range(1, len(num)):
        if num[i] != num[j]:
            i += 1
            num[i] = num[j]
    return i

def anotherSolutionn(num):
    i = 0
    for j in range(1, len(num)):
        if num[i] != num[j]:
            i += 1
            num[i] = num[j]
    return num[0:i]

def binary_search(inputList, toSearch):
    import math
    median = math.floor(len(inputList) / 2)
    if toSearch < inputList[median]:
        return binary_search(inputList[:median], toSearch)
    elif toSearch > inputList[median]:
        return binary_search(inputList[median:], toSearch)
    else:
        return median


def medianOfTwoSortedArrays(nums1, nums2):
    resultArr = []
    if len(nums1) is 0 and len(nums2) is not 0:
        return getMedianOfAnArray(nums2)
    elif len(nums1) is not 0 and len(nums2) is 0:
        return getMedianOfAnArray(nums1)
    else:
        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                resultArr.append(nums1[l])
                l += 1
            else:
                resultArr.append(nums2[r])
                r += 1
        if l < len(nums1):
            resultArr.extend(nums1[l:])
        elif r < len(nums2):
            resultArr.extend(nums2[r:])
        return getMedianOfAnArray(resultArr)

def getMedianOfAnArray(nums):
    quotient, remainder = divmod(len(nums), 2)
    if remainder is 1:
        median = float(nums[quotient])
    elif remainder is 0:
        median = float((nums[quotient] + nums[quotient - 1]) / 2)
    return median

if __name__ == '__main__':
    # print(solution([0,0,1,1,2,2,3]))
    # print(anotherSolutionn([0,0,1,1,2,2,3]))
    # print(binary_search([1, 2, 3, 4, 6, 7], 1))
    print(medianOfTwoSortedArrays([1,3], [2]))