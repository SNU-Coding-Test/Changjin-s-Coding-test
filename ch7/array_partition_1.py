import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum

if __name__ == "__main__":
    with open("../input/array_partition_1.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x
            nums = list(map(int, nums.strip("[]").split(",")))
            print(arrayPairSum(nums))