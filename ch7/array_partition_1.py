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
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i%2 == 0:
            sum += n

    return sum

if __name__ == "__main__":
    with open("../input/array_partition_1.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x
            nums = list(map(int, nums.strip("[]").split(",")))
            print(arrayPairSum(nums))