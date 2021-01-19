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
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * water

        stack.append(i)

    return volume

if __name__ == "__main__":
    with open("../input/trapping_rain_water.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            height = x.strip("[]").split(",")
            try:
                height = list(map(int, height))
            except ValueError as e:
                height = []
            print(trap(height))