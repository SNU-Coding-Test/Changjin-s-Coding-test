import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(price-min_price, profit)
    return profit


if __name__ == "__main__":
    with open("../input/best_time_to_buy_and_sell_stock.txt", "r") as f:
        data = f.read().splitlines()
        for x in data:
            prices = x
            prices = list(map(int, prices.strip("[]").split(",")))
            print(maxProfit(prices))