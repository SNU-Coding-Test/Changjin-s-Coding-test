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
    root = head = ListNode()

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next

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
