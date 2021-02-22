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
    rev = None
    slow = fast = head # fast, slow runner initialization

    # make a reversed linked list
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    # palindrome check
    while rev and slow.val == rev.val:
        slow, rev = slow.next, rev.next

    return not rev

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