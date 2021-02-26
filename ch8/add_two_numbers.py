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

def reverseList(node: ListNode) -> ListNode:
    prev = None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

def toList(node: ListNode) -> List:
    list = []
    while node:
        list.append(node.val)
        node = node.next
    return list

def toReverseLinkedList(result: str) -> ListNode:
    prev = None
    for r in result:
        node = ListNode(r)
        node.next, prev = prev, node
    return node

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    x = int(''.join(str(c) for c in toList(reverseList(l1))))
    y = int(''.join(str(c) for c in toList(reverseList(l2))))
    sum = x+y

    return toReverseLinkedList(str(sum))

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
