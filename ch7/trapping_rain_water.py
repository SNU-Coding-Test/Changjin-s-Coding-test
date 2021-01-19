import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def trap(height: List[int]) -> int:
    # 예외 처리
    # LeetCode test case 중 empty input이 있음.
    if not height:
        return 0

    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]

    volume = 0
    # max height를 찾을 때까지 반복해서 투 포인터를 이동
    while left != right:
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
            left_max = max(height[left], left_max)
        else:
            volume += right_max - height[right]
            right -= 1
            right_max = max(height[right], right_max)

    return volume

if __name__ == "__main__":
    with open("../input/trapping_rain_water.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            height = x.strip("[]").split(",")
            try:
                height = list(map(int, height))
            except ValueError as e:
                height = None
            print(trap(height))