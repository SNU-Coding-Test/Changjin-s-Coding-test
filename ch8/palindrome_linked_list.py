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

def isPalindrome(head: ListNode) -> bool:
    pal = []

    if not head:
        return True

    node = head
    # list transformation
    while node is not None:
        pal.append(node.val)
        node = node.next

    # palindrome discrimination
    while len(pal)>1:
        if pal.pop(0) != pal.pop():
            return False

    return True

if __name__ == "__main__":
    with open("../input/palindrome_linked_list.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            nums = x
            nums = list(map(int, nums.split("->")))
            print(nums)
            list_head = None
            # reversed input to make linked list
            for i in nums[::-1]:
                list_node = ListNode(i)
                list_node.next = list_head
                list_head = list_node
            print(isPalindrome(list_head))