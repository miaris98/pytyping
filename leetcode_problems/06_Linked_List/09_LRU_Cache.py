"""
LeetCode 146: LRU Cache
Companies: Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber, TikTok, Stripe
Time Complexity: O(1) - Both `get` and `put` run in strict O(1) time.
Space Complexity: O(capacity) - Hash map and doubly linked list store at most `capacity` nodes.
Intuition: Combine a Hash Map `{key: Node}` for O(1) lookup with a Doubly Linked List (`left` = LRU, `right` = MRU) for O(1) removal and re-insertion at the most-recently-used end.
Why Efficient: Singly linked lists or arrays require O(N) shifts on access. A Doubly Linked List with sentinel `left`/`right` nodes detaches and promotes any node in O(1) pointer updates.
"""
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
