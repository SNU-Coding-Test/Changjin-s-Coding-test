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
    return sum(sorted(nums)[::2]) # 한 줄로 pythonic 하게 풀이

if __name__ == "__main__":
    with open("../input/array_partition_1.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x
            nums = list(map(int, nums.strip("[]").split(",")))
            print(arrayPairSum(nums))