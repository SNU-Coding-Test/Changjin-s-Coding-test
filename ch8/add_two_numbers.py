import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    x1, x2 = [], []
    while l1:
        x1.append(l1.val)
        l1 = l1.next
    while l2:
        x2.append(l2.val)
        l2 = l2.next
    sum = 0
    for i, num in enumerate(x1):
        sum += num * (10 ** i)
    for i, num in enumerate(x2):
        sum += num * (10 ** i)
    prev = None
    for c in str(sum):
        result = ListNode(c)
        result.next, prev = prev, result
    return result

if __name__ == "__main__":
    with open("../input/add_two_numbers.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums1, nums2 = x.split(" + ")
            nums1, nums2 = list(map(int, nums1.strip("()").split("->"))), list(map(int, nums2.strip("()").split("->")))
            list_head = [None, None]
            # reversed input to make linked list
            for i, nums in enumerate([nums1, nums2]):
                for num in nums[::-1]:
                    list_node = ListNode(num)
                    list_node.next = list_head[i]
                    list_head[i] = list_node
            addTwoNumbers(list_head[0], list_head[1])
