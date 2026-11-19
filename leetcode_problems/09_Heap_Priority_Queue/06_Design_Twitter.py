"""
LeetCode 355: Design Twitter
Companies: Uber, Amazon, Google, Microsoft, Twitter, Coupang
Time Complexity: O(1) for `postTweet`/`follow`/`unfollow`; O(F + 10 log F) for `getNewsFeed` across F followed users.
Space Complexity: O(U + T) - Stores user follow sets and tweet lists.
Intuition: Store each user's tweets with a global timestamp counter, and use a Max-Heap to merge only the latest tweet from each followed user (just like Merge K Sorted Lists, stopping after 10 pops).
Why Efficient: Instead of merging and sorting all historical tweets of all followed users, lazy K-way heap merging inspects at most 10 tweets total!
"""
from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            tweets = self.tweet_map[followeeId]
            if tweets:
                idx = len(tweets) - 1
                cnt, tweetId = tweets[idx]
                heapq.heappush(heap, (cnt, tweetId, followeeId, idx - 1))
        while heap and len(res) < 10:
            cnt, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                nxt_cnt, nxt_id = self.tweet_map[followeeId][idx]
                heapq.heappush(heap, (nxt_cnt, nxt_id, followeeId, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
