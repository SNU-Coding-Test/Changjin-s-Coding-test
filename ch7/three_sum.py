import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def threeSum(nums: List[int]) -> List[List[int]]:
    sol = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i>0 and nums[i] == nums[i-1]:
            continue

        # 투 포인터 풀이
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum >0:
                right -= 1
            else:
                sol.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return sol


if __name__ == "__main__":
    with open("../input/three_sum.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x.strip("[]").split(",")
            try:
                nums = list(map(int, nums))
            except ValueError as e:
                nums = []
            print(threeSum(nums))