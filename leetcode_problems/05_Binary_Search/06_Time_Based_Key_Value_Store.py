"""
LeetCode 981: Time Based Key-Value Store
Companies: Google, Amazon, Netflix, Apple, Uber, Lyft, Roblox
Time Complexity: O(1) for `set`, O(log N) for `get` via binary search.
Space Complexity: O(N) - Stores `(timestamp, value)` pairs per key.
Intuition: Because timestamps in `set` are strictly increasing, each key's list of `(timestamp, value)` pairs is naturally sorted—allowing O(log N) binary search on `get`.
Why Efficient: Avoids O(log N) balanced-tree insertion overhead on `set` by appending in O(1) and binary searching the naturally sorted list on `get`.
"""
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ""
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return res
