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
    nums_map = {}
    for i, num in enumerate(nums):
        # 키와 값을 바꿔 딕셔너리에 저장하고, 타겟에서 첫번째 수를 뺀 결과를 key로 조회
        if target-num in nums_map:
            # 키가 존재하면 바로 return
            return [nums_map[target-num], i]
        nums_map[num] = i



if __name__ == "__main__":
    with open("../input/two_sum.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums, target = x.split()
            nums = list(map(int, nums.strip("[]").split(",")))
            target = int(target)
            print(twoSum(nums, target))