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

def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

if __name__ == "__main__":
    with open("../input/reverse_linked_list.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x.split("->")
            nums = [int(num) if num!='NULL' else None for num in nums]
            list_head = None
            for num in nums[::-1]:
                list_node = ListNode(num)
                list_node.next, list_head = list_head, list_node
            print(nums)
            print(reverseList(list_head))