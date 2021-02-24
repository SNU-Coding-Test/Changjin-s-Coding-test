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

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1

if __name__ == "__main__":
    with open("../input/merge_two_sorted_lists.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums1, nums2 = x.split(", ")
            nums1, nums2 = list(map(int, nums1.split("->"))), list(map(int, nums2.split("->")))
            print(nums1, nums2)
            list_head = [None, None]
            # reversed input to make linked list
            for i, nums in enumerate([nums1, nums2]):
                for num in nums[::-1]:
                    list_node = ListNode(num)
                    list_node.next = list_head[i]
                    list_head[i] = list_node
            print(mergeTwoLists(list_head[0], list_head[1]))