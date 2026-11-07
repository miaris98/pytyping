import os

PROBLEMS = {
    "01_Arrays_and_Hashing": {
        "01_Two_Sum.py": '''"""
LeetCode 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
''',
        "02_Contains_Duplicate.py": '''"""
LeetCode 217: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
''',
        "03_Valid_Anagram.py": '''"""
LeetCode 242: Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
            if count[char] < 0:
                return False
        return True
''',
        "04_Group_Anagrams.py": '''"""
LeetCode 49: Group Anagrams
Given an array of strings strs, group the anagrams together.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            groups[tuple(key)].append(word)
        return list(groups.values())
''',
        "05_Top_K_Frequent_Elements.py": '''"""
LeetCode 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
'''
    },
    "02_Two_Pointers": {
        "01_Valid_Palindrome.py": '''"""
LeetCode 125: Valid Palindrome
A phrase is a palindrome if it reads the same forward and backward after converting all uppercase letters into lowercase and removing all non-alphanumeric characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
''',
        "02_Two_Sum_II.py": '''"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
''',
        "03_3Sum.py": '''"""
LeetCode 15: 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
''',
        "04_Container_With_Most_Water.py": '''"""
LeetCode 11: Container With Most Water
Find two lines that together with the x-axis form a container, such that the container contains the most water.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
'''
    },
    "03_Sliding_Window": {
        "01_Best_Time_to_Buy_and_Sell_Stock.py": '''"""
LeetCode 121: Best Time to Buy and Sell Stock
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
''',
        "02_Longest_Substring_Without_Repeating_Characters.py": '''"""
LeetCode 3: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
'''
    },
    "04_Stack": {
        "01_Valid_Parentheses.py": '''"""
LeetCode 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
''',
        "02_Min_Stack.py": '''"""
LeetCode 155: Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
'''
    },
    "05_Binary_Search": {
        "01_Binary_Search.py": '''"""
LeetCode 704: Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
''',
        "02_Search_2D_Matrix.py": '''"""
LeetCode 74: Search a 2D Matrix
You are given an m x n integer matrix matrix with the properties that integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
'''
    },
    "06_Linked_List": {
        "01_Reverse_Linked_List.py": '''"""
LeetCode 206: Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
''',
        "02_Merge_Two_Sorted_Lists.py": '''"""
LeetCode 21: Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
'''
    },
    "07_Trees": {
        "01_Invert_Binary_Tree.py": '''"""
LeetCode 226: Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
''',
        "02_Maximum_Depth_of_Binary_Tree.py": '''"""
LeetCode 104: Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
'''
    },
    "08_Dynamic_Programming": {
        "01_Climbing_Stairs.py": '''"""
LeetCode 70: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one_step_before = 2
        two_steps_before = 1
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        return one_step_before
''',
        "02_Coin_Change.py": '''"""
LeetCode 322: Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount.
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
'''
    },
    "09_Graphs": {
        "01_Number_of_Islands.py": '''"""
LeetCode 200: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
        return island_count
'''
    }
}

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leetcode_problems")
os.makedirs(base_dir, exist_ok=True)

for folder, files in PROBLEMS.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for filename, content in files.items():
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\\n")

print(f"Created sample problems in {base_dir}")

