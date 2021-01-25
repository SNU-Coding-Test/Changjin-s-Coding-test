import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, -1 , -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out

if __name__ == "__main__":
    with open("../input/product_of_array_except_self.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x
            nums = list(map(int, nums.strip("[]").split(",")))
            print(productExceptSelf(nums))