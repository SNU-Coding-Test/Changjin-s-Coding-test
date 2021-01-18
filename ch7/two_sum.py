import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]



if __name__ == "__main__":
    with open("../input/two_sum.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums, target = x.split()
            nums = list(map(int, nums.strip("[]").split(",")))
            target = int(target)
            print(twoSum(nums, target))