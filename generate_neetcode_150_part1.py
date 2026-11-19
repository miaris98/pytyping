"""
NeetCode 150 Solutions Generator - Part 1 (Categories 01 to 09: 70 problems)
Includes Company tags, Time/Space Big O, Core Intuition, Why Efficient, and Optimal Python 3 Code.
"""

PART1_PROBLEMS = {
    "01_Arrays_and_Hashing": [
        (
            "01_Contains_Duplicate.py",
            "LeetCode 217: Contains Duplicate",
            "Amazon, Google, Apple, Microsoft, Meta, Bloomberg",
            "O(N) - Single pass over N elements with O(1) average hash set lookups.",
            "O(N) - Hash set stores up to N unique elements in the worst case.",
            "Use a Hash Set to remember seen numbers and answer membership queries in O(1) time.",
            "Brute-force takes O(N²) and sorting takes O(N log N). A hash set runs in O(N) time and terminates early on the first duplicate.",
            """from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False"""
        ),
        (
            "02_Valid_Anagram.py",
            "LeetCode 242: Valid Anagram",
            "Amazon, Bloomberg, Meta, Google, Spotify, Microsoft",
            "O(N) - Two linear passes over strings of length N.",
            "O(1) - At most 26 lowercase English character keys in the frequency map.",
            "Two strings are anagrams iff they have the exact same length and identical character frequency counts.",
            "Sorting both strings costs O(N log N). Counting frequencies in a hash map achieves optimal O(N) time and O(1) bounded alphabet space.",
            """from collections import defaultdict

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
        return True"""
        ),
        (
            "03_Two_Sum.py",
            "LeetCode 1: Two Sum",
            "Google, Amazon, Meta, Microsoft, Apple, Bloomberg, Uber, Adobe",
            "O(N) - Single pass through the array with O(1) hash table lookups.",
            "O(N) - Stores at most N - 1 elements and their indices in the hash map.",
            "For each number `num`, the exact partner needed is `complement = target - num`. Store seen numbers in a dict mapping `{value: index}`.",
            "Replaces the O(N) inner search loop of an O(N²) brute-force approach with an O(1) hash map lookup, solving the problem in one O(N) pass.",
            """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []"""
        ),
        (
            "04_Group_Anagrams.py",
            "LeetCode 49: Group Anagrams",
            "Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber",
            "O(N * K) - N words of max length K counted into 26-slot frequency tuples.",
            "O(N * K) - Hash map stores all N strings grouped by their 26-integer signature.",
            "All anagrams share the same 26-letter frequency count. Use the 26-count tuple as a dictionary key to bucket anagrams together.",
            "Sorting each word of length K takes O(N * K log K). Counting characters into a 26-element array drops the log K factor for optimal O(N * K) time.",
            """from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            groups[tuple(key)].append(word)
        return list(groups.values())"""
        ),
        (
            "05_Top_K_Frequent_Elements.py",
            "LeetCode 347: Top K Frequent Elements",
            "Meta, Amazon, Google, Microsoft, Apple, Uber, Bloomberg",
            "O(N) - Frequency counting plus linear bucket scan across N buckets.",
            "O(N) - Counter map and frequency buckets of size N + 1.",
            "Since any element's frequency is between 1 and N, create an array of N + 1 buckets where `bucket[freq]` holds numbers appearing `freq` times.",
            "Sorting takes O(N log N) and a heap takes O(N log K). Bucket sort exploits the bounded frequency range [1..N] to achieve strict O(N) linear time.",
            """from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res"""
        ),
        (
            "06_Encode_and_Decode_Strings.py",
            "LeetCode 271: Encode and Decode Strings",
            "Google, Meta, Amazon, Uber, LinkedIn, Square",
            "O(N) - Single pass over total character count N for both encode and decode.",
            "O(1) - Auxiliary space beyond the output string/list.",
            "Prefix each string with its character length followed by a delimiter `#` (e.g., `4#code`). During decoding, read the length up to `#` and slice that exact number of characters.",
            "Delimiter-escaping fails or scans twice when strings contain `#` or digits. Length-prefixing jumps directly over any inner characters in O(1) index slices.",
            """from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1 : i])
        return res"""
        ),
        (
            "07_Product_of_Array_Except_Self.py",
            "LeetCode 238: Product of Array Except Self",
            "Amazon, Meta, Apple, Microsoft, Google, Bloomberg, Uber, Asana",
            "O(N) - One forward pass for prefixes and one backward pass for suffixes.",
            "O(1) - Uses the output array directly with only two scalar accumulators.",
            "Every element's answer is the product of all numbers to its left multiplied by the product of all numbers to its right.",
            "Avoids O(N²) nested loops and avoids division (which breaks when zeros exist) while using O(1) auxiliary space beyond the output list.",
            """from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res"""
        ),
        (
            "08_Valid_Sudoku.py",
            "LeetCode 36: Valid Sudoku",
            "Amazon, Apple, Microsoft, Google, Uber, Nvidia, Karat",
            "O(1) - Fixed 9x9 board (81 cells) scanned once.",
            "O(1) - Hash sets hold at most 81 entries across 9 rows, 9 cols, and 9 boxes.",
            "Track seen digits for each row `r`, column `c`, and 3x3 sub-box `(r // 3, c // 3)` using hash sets.",
            "Instead of 27 separate passes over the board, integer-dividing `(r // 3, c // 3)` maps any cell to its 3x3 box in O(1) time during a single pass.",
            """from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        return True"""
        ),
        (
            "09_Longest_Consecutive_Sequence.py",
            "LeetCode 128: Longest Consecutive Sequence",
            "Google, Amazon, Meta, Bloomberg, Microsoft, Apple, Spotify",
            "O(N) - Each number is visited at most twice (once in outer loop, once in inner streak).",
            "O(N) - Hash set stores all unique numbers for O(1) lookups.",
            "Put all numbers in a Set. Only start counting a consecutive streak `x, x+1, x+2...` if `x - 1` is NOT in the set (meaning `x` is the true start of a sequence).",
            "Sorting costs O(N log N). Checking `if (num - 1) not in num_set` ensures we never redundantly count from the middle of a sequence, guaranteeing O(N) runtime.",
            """from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest"""
        ),
    ],
    "02_Two_Pointers": [
        (
            "01_Valid_Palindrome.py",
            "LeetCode 125: Valid Palindrome",
            "Meta, Amazon, Microsoft, Apple, Google, Bloomberg",
            "O(N) - Left and right pointers cross after visiting each character once.",
            "O(1) - Compares characters in-place without allocating a filtered copy.",
            "Walk two pointers inward from both ends of the string, skipping non-alphanumeric characters and comparing lowercase characters.",
            "Building a new filtered string and reversing it allocates O(N) extra memory. Two pointers validate the string in-place in O(1) space.",
            """class Solution:
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
        return True"""
        ),
        (
            "02_Two_Sum_II.py",
            "LeetCode 167: Two Sum II - Input Array Is Sorted",
            "Amazon, Google, Meta, Apple, Microsoft, Bloomberg",
            "O(N) - Each step moves either `left` forward or `right` backward at most N times.",
            "O(1) - Zero auxiliary data structures used.",
            "Start pointers at the smallest (`left = 0`) and largest (`right = n - 1`) values. If their sum is too small, increment `left`; if too large, decrement `right`.",
            "Exploits the sorted property to achieve O(N) runtime with O(1) constant memory instead of an O(N) hash table.",
            """from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left + 1, right + 1]
            elif cur < target:
                left += 1
            else:
                right -= 1
        return []"""
        ),
        (
            "03_3Sum.py",
            "LeetCode 15: 3Sum",
            "Meta, Amazon, Google, Microsoft, Apple, Bloomberg, Uber, Adobe",
            "O(N²) - O(N log N) sort plus N iterations of an O(N) two-pointer sweep.",
            "O(1) - In-place duplicate skipping without a hash set (excluding output list).",
            "Sort the array, fix the first number `nums[i]`, and run a Two-Pointer search on `i+1..n-1` for `-nums[i]`, skipping adjacent duplicates.",
            "Reduces O(N³) triple-loop brute force to O(N²) and avoids high-memory hash sets by skipping duplicate adjacent sorted elements.",
            """from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res"""
        ),
        (
            "04_Container_With_Most_Water.py",
            "LeetCode 11: Container With Most Water",
            "Amazon, Google, Meta, Microsoft, Apple, Bloomberg, Adobe",
            "O(N) - Single pass moving the shorter boundary pointer inward N - 1 times.",
            "O(1) - Only scalar pointer and maximum tracking variables.",
            "Start with maximum width (`left = 0, right = n - 1`). Since water height is capped by the shorter wall, always move the shorter pointer inward in hopes of finding a taller wall.",
            "Eliminates N - 1 suboptimal pairs on every single step, turning an O(N²) all-pairs check into an optimal O(N) greedy two-pointer scan.",
            """from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            max_water = max(max_water, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water"""
        ),
        (
            "05_Trapping_Rain_Water.py",
            "LeetCode 42: Trapping Rain Water",
            "Goldman Sachs, Amazon, Google, Meta, Microsoft, Apple, Bloomberg",
            "O(N) - Single two-pointer traversal visiting each bar once.",
            "O(1) - Tracks `left_max` and `right_max` scalars instead of O(N) prefix/suffix arrays.",
            "Water trapped above any bar depends on `min(max_left, max_right) - height[i]`. By always advancing the side with the smaller running maximum, we know the exact bottleneck height immediately.",
            "Dynamic programming prefix/suffix tables require O(N) extra memory. Two pointers achieve the same O(N) speed in O(1) constant space.",
            """from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water"""
        ),
    ],
    "03_Sliding_Window": [
        (
            "01_Best_Time_to_Buy_and_Sell_Stock.py",
            "LeetCode 121: Best Time to Buy and Sell Stock",
            "Amazon, Meta, Google, Microsoft, Bloomberg, Apple, Goldman Sachs",
            "O(N) - Single chronological pass through prices.",
            "O(1) - Tracks only `min_price` and `max_profit`.",
            "Track the lowest buying price seen so far (`min_price`) and test selling at each current price (`price - min_price`).",
            "Replaces O(N²) nested buy/sell loops with a single O(N) running-minimum pass using O(1) space.",
            """from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit"""
        ),
        (
            "02_Longest_Substring_Without_Repeating_Characters.py",
            "LeetCode 3: Longest Substring Without Repeating Characters",
            "Amazon, Meta, Google, Microsoft, Bloomberg, Apple, Uber, Spotify",
            "O(N) - Single pass with O(1) hash map index jumps.",
            "O(min(N, M)) - Dictionary stores at most one index per unique character in the charset.",
            "Maintain a sliding window `[left, right]` of unique characters. Store each character's latest index so `left` can jump straight past any duplicate.",
            "Jumping `left = char_index[char] + 1` via a hash map avoids incrementing `left` one by one, completing in strictly N iterations.",
            """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len"""
        ),
        (
            "03_Longest_Repeating_Character_Replacement.py",
            "LeetCode 424: Longest Repeating Character Replacement",
            "Google, Amazon, Meta, Uber, Microsoft, Bloomberg",
            "O(N) - Both `left` and `right` pointers advance at most N times.",
            "O(1) - Frequency dictionary stores at most 26 uppercase English letters.",
            "A window is valid if `(window_length - max_frequency_char_count) <= k`. Expand `right` and only shift `left` by 1 when replacements needed exceed `k`.",
            "We never need to decrement `max_freq` when shrinking because only a strictly larger `max_freq` can ever produce a longer valid window—keeping the check O(1).",
            """from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0
        for right, char in enumerate(s):
            count[char] += 1
            max_freq = max(max_freq, count[char])
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len"""
        ),
        (
            "04_Permutation_in_String.py",
            "LeetCode 567: Permutation in String",
            "Microsoft, Amazon, Meta, Google, Oracle, Uber",
            "O(N) - Fixed-size sliding window updates in O(1) per character.",
            "O(1) - Two fixed-size frequency arrays of length 26.",
            "Slide a window of length `len(s1)` across `s2`, maintaining character counts for `'a'..'z'` and checking when both frequency profiles match.",
            "Generating permutations takes O(N!) and sorting each window takes O(N * M log M). Fixed 26-slot frequency arrays run in O(N) time and O(1) space.",
            """class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        if c1 == c2:
            return True
        for i in range(len(s1), len(s2)):
            c2[ord(s2[i]) - ord('a')] += 1
            c2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if c1 == c2:
                return True
        return False"""
        ),
        (
            "05_Minimum_Window_Substring.py",
            "LeetCode 76: Minimum Window Substring",
            "Meta, Airbnb, Amazon, Google, LinkedIn, Uber, Microsoft, Lyft",
            "O(N + M) - Each character in `s` is visited at most twice (`right` and `left`).",
            "O(1) - Frequency maps bounded by the ASCII character set.",
            "Expand `right` until all required character counts (`have == need`) are satisfied, then greedily contract `left` to find the smallest valid window.",
            "Tracking `have` vs `need` integer counters lets us verify window validity in O(1) time instead of comparing entire hash maps on every step.",
            """from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need_map = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(need_map)
        res, res_len = [-1, -1], float("inf")
        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need_map and window[ch] == need_map[ch]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in need_map and window[s[left]] < need_map[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else "" """
        ),
        (
            "06_Sliding_Window_Maximum.py",
            "LeetCode 239: Sliding Window Maximum",
            "Amazon, Google, Meta, Citadel, Uber, Microsoft, DoorDash",
            "O(N) - Every index is pushed and popped from the monotonic deque at most once.",
            "O(K) - Deque stores at most K indices from the current window.",
            "Maintain a Monotonic Decreasing Deque of indices: pop smaller elements from the back before pushing `right`, and pop out-of-window indices from the front.",
            "Scanning each window takes O(N * K) and a heap takes O(N log K). A monotonic deque keeps the window maximum at `dq[0]` in amortized O(1) time per step.",
            """from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for right, val in enumerate(nums):
            while dq and nums[dq[-1]] < val:
                dq.pop()
            dq.append(right)
            if dq[0] <= right - k:
                dq.popleft()
            if right >= k - 1:
                res.append(nums[dq[0]])
        return res"""
        ),
    ],
    "04_Stack": [
        (
            "01_Valid_Parentheses.py",
            "LeetCode 20: Valid Parentheses",
            "Amazon, Meta, Google, Bloomberg, Microsoft, Apple, Spotify",
            "O(N) - Single pass pushing and popping each character at most once.",
            "O(N) - Stack holds up to N opening brackets in the worst case.",
            "Use a LIFO Stack for open brackets. When encountering a closing bracket, verify the top of the stack matches its required opening partner.",
            "Processes nested brackets in one O(N) pass with O(1) per-character stack operations.",
            """class Solution:
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
        return not stack"""
        ),
        (
            "02_Min_Stack.py",
            "LeetCode 155: Min Stack",
            "Amazon, Bloomberg, Microsoft, Google, Apple, Meta",
            "O(1) - Constant time for `push`, `pop`, `top`, and `getMin`.",
            "O(N) - Parallel `min_stack` stores the running minimum at each stack depth.",
            "Maintain two synchronized stacks: `stack` for values and `min_stack` where each slot stores the minimum value at or below that depth.",
            "Avoids O(N) scans when the minimum element is popped, guaranteeing strict O(1) worst-case time for all four operations.",
            """class MinStack:
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
        return self.min_stack[-1]"""
        ),
        (
            "03_Evaluate_Reverse_Polish_Notation.py",
            "LeetCode 150: Evaluate Reverse Polish Notation",
            "Amazon, Google, LinkedIn, Microsoft, Uber",
            "O(N) - Each token is processed once in O(1) time.",
            "O(N) - Stack holds operand integers during evaluation.",
            "Push numbers onto a stack; when an operator (`+`, `-`, `*`, `/`) appears, pop the top two operands, apply the operator, and push the result back.",
            "Postfix notation eliminates parentheses and operator precedence rules, allowing single-pass evaluation with a stack in O(N) time.",
            """from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]"""
        ),
        (
            "04_Generate_Parentheses.py",
            "LeetCode 22: Generate Parentheses",
            "Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber",
            "O(4^N / sqrt(N)) - Generates only valid Catalan-number sequences.",
            "O(N) - Recursion stack depth and current path list of length 2N.",
            "Backtrack by tracking `open_n` and `close_n` counts: add `'('` if `open_n < n`, and add `')'` only if `close_n < open_n`.",
            "Prunes invalid bracket prefixes immediately instead of generating all 2^(2N) strings and filtering them afterward.",
            """from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtrack(open_n: int, close_n: int):
            if open_n == close_n == n:
                res.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()
            if close_n < open_n:
                stack.append(")")
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res"""
        ),
        (
            "05_Daily_Temperatures.py",
            "LeetCode 739: Daily Temperatures",
            "Meta, Amazon, Google, Microsoft, Apple, TikTok, Bloomberg",
            "O(N) - Each index is pushed and popped from the monotonic stack at most once.",
            "O(N) - Monotonic stack stores unresolved day indices.",
            "Maintain a Monotonic Decreasing Stack of indices. When today's temperature is warmer than the day at the top of the stack, pop that day and record `today - prev_day`.",
            "Replaces O(N²) forward scans with a single O(N) monotonic stack pass that resolves multiple waiting days as soon as a warmer day arrives.",
            """from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res"""
        ),
        (
            "06_Car_Fleet.py",
            "LeetCode 853: Car Fleet",
            "Google, Amazon, Uber, Stripe, Microsoft",
            "O(N log N) - Dominated by sorting cars by starting position.",
            "O(N) - Stack/list stores arrival times of distinct car fleets.",
            "Sort cars from closest-to-target to farthest. Compute each car's arrival time `(target - pos) / speed`; if a car behind arrives sooner or equal to the fleet ahead, it merges into that fleet.",
            "Processing from front to back turns collision simulation into a simple arrival-time comparison on a stack.",
            """from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)"""
        ),
        (
            "07_Largest_Rectangle_in_Histogram.py",
            "LeetCode 84: Largest Rectangle in Histogram",
            "Amazon, Google, Meta, Microsoft, Adobe, Citadel",
            "O(N) - Each bar is pushed and popped from the stack once.",
            "O(N) - Monotonic increasing stack of `(start_index, height)` pairs.",
            "Keep a Monotonic Increasing Stack. When a shorter bar arrives, taller bars on the stack can no longer extend right—pop them, compute their max area, and carry their `start` index backward.",
            "Brute-force expanding around each bar takes O(N²). The monotonic stack finds both the left and right boundaries for every bar in a single O(N) pass.",
            """from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area"""
        ),
    ],
    "05_Binary_Search": [
        (
            "01_Binary_Search.py",
            "LeetCode 704: Binary Search",
            "Google, Amazon, Microsoft, Apple, Meta, Bloomberg",
            "O(log N) - Halves the search interval on every comparison.",
            "O(1) - Iterative pointers `low`, `high`, and `mid`.",
            "Compare `target` with the middle element `nums[mid]`. Discard the left half if `nums[mid] < target` or the right half if `nums[mid] > target`.",
            "Reduces O(N) linear search to O(log N) logarithmic time with O(1) memory.",
            """from typing import List

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
        return -1"""
        ),
        (
            "02_Search_2D_Matrix.py",
            "LeetCode 74: Search a 2D Matrix",
            "Amazon, Microsoft, Meta, Google, Apple, Bloomberg",
            "O(log(M * N)) - Binary search across M * N virtual 1D indices.",
            "O(1) - Maps 1D index to 2D `(row, col)` using `divmod(mid, n)` in-place.",
            "Treat the M × N sorted matrix as a virtual 1D sorted array of length `M * N`, converting any 1D midpoint `mid` to `(mid // n, mid % n)`.",
            "Achieves logarithmic O(log M + log N) time without flattening or copying the matrix.",
            """from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
        return False"""
        ),
        (
            "03_Koko_Eating_Bananas.py",
            "LeetCode 875: Koko Eating Bananas",
            "Google, Amazon, Meta, DoorDash, Airbnb, Salesforce",
            "O(N log M) - Binary search over speed range `[1..max(piles)]`, spending O(N) per check.",
            "O(1) - Only scalar boundary variables used.",
            "Binary search on the eating speed `k` in `[1, max(piles)]`. Since feasibility is monotonic (faster speed never takes more hours), find the minimum `k` where total hours `<= h`.",
            "Testing every speed linearly takes O(N * M) where M can be 10^9. Binary search on the answer space reduces M to log₂(M) ≈ 30 checks!",
            """from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            k = (low + high) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res"""
        ),
        (
            "04_Find_Minimum_in_Rotated_Sorted_Array.py",
            "LeetCode 153: Find Minimum in Rotated Sorted Array",
            "Amazon, Microsoft, Meta, Google, Bloomberg, Uber",
            "O(log N) - Halves the search range in each step.",
            "O(1) - Constant pointer variables.",
            "Compare `nums[mid]` with `nums[high]`. If `nums[mid] > nums[high]`, the minimum pivot must lie in the right half (`low = mid + 1`); otherwise it lies at `mid` or to the left (`high = mid`).",
            "Finds the rotation pivot in O(log N) time instead of an O(N) linear scan.",
            """from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]"""
        ),
        (
            "05_Search_in_Rotated_Sorted_Array.py",
            "LeetCode 33: Search in Rotated Sorted Array",
            "Meta, Amazon, Google, Microsoft, LinkedIn, Apple, Bloomberg, Uber",
            "O(log N) - Single-pass binary search eliminating half the array each step.",
            "O(1) - Constant space pointers.",
            "At any midpoint `mid`, at least one half (`low..mid` or `mid..high`) is guaranteed to be strictly sorted. Check which half is sorted, then check if `target` falls within that sorted half's bounds.",
            "Solves rotated search in one O(log N) binary search without needing a separate pass to find the pivot first.",
            """from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1"""
        ),
        (
            "06_Time_Based_Key_Value_Store.py",
            "LeetCode 981: Time Based Key-Value Store",
            "Google, Amazon, Netflix, Apple, Uber, Lyft, Roblox",
            "O(1) for `set`, O(log N) for `get` via binary search.",
            "O(N) - Stores `(timestamp, value)` pairs per key.",
            "Because timestamps in `set` are strictly increasing, each key's list of `(timestamp, value)` pairs is naturally sorted—allowing O(log N) binary search on `get`.",
            "Avoids O(log N) balanced-tree insertion overhead on `set` by appending in O(1) and binary searching the naturally sorted list on `get`.",
            """from collections import defaultdict

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
        return res"""
        ),
        (
            "07_Median_of_Two_Sorted_Arrays.py",
            "LeetCode 4: Median of Two Sorted Arrays",
            "Google, Amazon, Meta, Goldman Sachs, Microsoft, Apple, Bloomberg",
            "O(log(min(M, N))) - Binary searches the partition point on the smaller array.",
            "O(1) - Only index and boundary variables used.",
            "Binary search the partition cut `i` in the smaller array `A` (which automatically fixes cut `j = half - i` in `B`) until `A_left <= B_right` and `B_left <= A_right`.",
            "Merging both arrays takes O(M + N) time. Binary searching the partition on the shorter array achieves the theoretical optimal O(log(min(M, N))) time and O(1) space.",
            """from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        low, high = 0, len(A) - 1
        while True:
            i = (low + high) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return float(min(Aright, Bright))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1"""
        ),
    ],
    "06_Linked_List": [
        (
            "01_Reverse_Linked_List.py",
            "LeetCode 206: Reverse Linked List",
            "Amazon, Microsoft, Meta, Apple, Google, Bloomberg",
            "O(N) - Single pass visiting each node once.",
            "O(1) - Reverses `.next` pointers in-place using `prev`, `curr`, and `next_temp`.",
            "Walk through the list iteratively, saving `curr.next` before flipping `curr.next = prev`.",
            "Iterative pointer reversal uses O(1) memory compared to O(N) recursion stack space.",
            """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev"""
        ),
        (
            "02_Merge_Two_Sorted_Lists.py",
            "LeetCode 21: Merge Two Sorted Lists",
            "Amazon, Microsoft, Meta, Apple, Google, Adobe",
            "O(N + M) - Advances through one node of `list1` or `list2` on each comparison.",
            "O(1) - Splices existing nodes in-place using a single `dummy` anchor node.",
            "Use a `dummy` node and `tail` pointer, repeatedly attaching the smaller front node of `list1` or `list2`.",
            "In-place pointer splicing uses O(1) memory and attaches any leftover tail in O(1).",
            """from typing import Optional

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
        tail.next = list1 or list2
        return dummy.next"""
        ),
        (
            "03_Reorder_List.py",
            "LeetCode 143: Reorder List",
            "Meta, Amazon, Microsoft, Bloomberg, Google",
            "O(N) - Fast/slow midpoint, second-half reversal, and alternating merge are each O(N).",
            "O(1) - Mutates pointers in-place without copying nodes into an array.",
            "1) Find the middle with slow/fast pointers, 2) Reverse the second half in-place, 3) Zipper-merge the first and reversed second halves.",
            "Storing nodes in a list costs O(N) memory. Reversing the second half in-place achieves O(1) extra space.",
            """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2"""
        ),
        (
            "04_Remove_Nth_Node_From_End_of_List.py",
            "LeetCode 19: Remove Nth Node From End of List",
            "Meta, Amazon, Microsoft, Google, Apple, Bloomberg",
            "O(N) - Single pass using two pointers separated by a gap of `n` nodes.",
            "O(1) - Uses a `dummy` node and two pointers `left` and `right`.",
            "Advance `right` by `n` steps first, then move `left` (starting at `dummy`) and `right` together until `right` hits the end—placing `left` right before the target node.",
            "Finds and removes the Nth node from the end in a single pass with a `dummy` node that cleanly handles removing the head.",
            """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next"""
        ),
        (
            "05_Copy_List_With_Random_Pointer.py",
            "LeetCode 138: Copy List with Random Pointer",
            "Meta, Amazon, Microsoft, Bloomberg, Google, Nvidia",
            "O(N) - Two linear passes over the linked list.",
            "O(N) - Hash map mapping each original node to its cloned counterpart.",
            "Pass 1 creates a clone for every node in a dictionary `{old_node: new_node}`. Pass 2 wires up `.next` and `.random` pointers via O(1) dictionary lookups.",
            "Handles arbitrary cycles and forward/backward `.random` pointers cleanly in O(N) time.",
            """from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_copy = {None: None}
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next
        return old_to_copy[head]"""
        ),
        (
            "06_Add_Two_Numbers.py",
            "LeetCode 2: Add Two Numbers",
            "Amazon, Google, Meta, Microsoft, Apple, Bloomberg, Adobe",
            "O(max(N, M)) - Single pass through both digit lists.",
            "O(max(N, M)) - Output linked list storing the summed digits.",
            "Simulate elementary school addition digit-by-digit from least significant to most significant, carrying `carry = total // 10` to the next node.",
            "Processes arbitrarily long numbers directly without integer conversion overflow.",
            """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, digit = divmod(v1 + v2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next"""
        ),
        (
            "07_Linked_List_Cycle.py",
            "LeetCode 141: Linked List Cycle",
            "Amazon, Microsoft, Spotify, Apple, Google, Visa",
            "O(N) - Fast pointer catches slow pointer within one cycle loop.",
            "O(1) - Floyd's Tortoise and Hare uses only two pointers.",
            "Move `slow` by 1 step and `fast` by 2 steps. If a cycle exists, `fast` will eventually lap and meet `slow` inside the cycle.",
            "A hash set of visited nodes takes O(N) memory. Floyd's cycle-finding algorithm detects cycles in O(1) constant space.",
            """from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False"""
        ),
        (
            "08_Find_the_Duplicate_Number.py",
            "LeetCode 287: Find the Duplicate Number",
            "Amazon, Meta, Microsoft, Google, Apple, Bloomberg",
            "O(N) - Two-phase Floyd's cycle detection.",
            "O(1) - Zero array modification and zero extra memory.",
            "Treat array values in `[1..n]` as `.next` pointers (`i -> nums[i]`). A duplicate value means two indices point to the same node, creating a cycle whose entrance is the duplicate!",
            "Sorting mutates the array and sets use O(N) space. Floyd's Tortoise & Hare finds the cycle entrance in O(N) time and O(1) space without modifying `nums`.",
            """from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow"""
        ),
        (
            "09_LRU_Cache.py",
            "LeetCode 146: LRU Cache",
            "Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber, TikTok, Stripe",
            "O(1) - Both `get` and `put` run in strict O(1) time.",
            "O(capacity) - Hash map and doubly linked list store at most `capacity` nodes.",
            "Combine a Hash Map `{key: Node}` for O(1) lookup with a Doubly Linked List (`left` = LRU, `right` = MRU) for O(1) removal and re-insertion at the most-recently-used end.",
            "Singly linked lists or arrays require O(N) shifts on access. A Doubly Linked List with sentinel `left`/`right` nodes detaches and promotes any node in O(1) pointer updates.",
            """class Node:
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
            del self.cache[lru.key]"""
        ),
        (
            "10_Merge_K_Sorted_Lists.py",
            "LeetCode 23: Merge k Sorted Lists",
            "Meta, Amazon, Google, Microsoft, Apple, Uber, LinkedIn",
            "O(N log K) - Min-heap of size K processes all N total nodes.",
            "O(K) - Heap holds at most one head node from each of the K lists.",
            "Push the head of each non-empty list into a Min-Heap `(node.val, idx, node)`. Repeatedly pop the smallest node, attach it to `tail.next`, and push its `.next` node.",
            "Merging lists one-by-one takes O(N * K) time. A min-heap of size K finds the next smallest node across all K lists in O(log K) time.",
            """from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        tail = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next"""
        ),
        (
            "11_Reverse_Nodes_in_K_Group.py",
            "LeetCode 25: Reverse Nodes in k-Group",
            "Amazon, Microsoft, Meta, Google, Apple, Bloomberg",
            "O(N) - Each node is visited twice (once by `get_kth`, once during reversal).",
            "O(1) - Reverses each group of `k` nodes in-place using pointer manipulation.",
            "Use `group_prev` before each chunk of `k` nodes. Check if `k` nodes remain; if so, reverse those `k` nodes in-place and stitch `group_prev.next` to the new chunk head.",
            "Achieves O(1) space in-place reversal without recursion or auxiliary arrays.",
            """from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp"""
        ),
    ],
    "07_Trees": [
        (
            "01_Invert_Binary_Tree.py",
            "LeetCode 226: Invert Binary Tree",
            "Google, Amazon, Meta, Apple, Microsoft, Bloomberg",
            "O(N) - Visits every node in the tree once.",
            "O(H) - Recursion call stack proportional to tree height H.",
            "Recursively swap the left and right child pointers of every node in the tree.",
            "Visits each node once in O(N) time with a single clean tuple swap.",
            """from typing import Optional

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
        return root"""
        ),
        (
            "02_Maximum_Depth_of_Binary_Tree.py",
            "LeetCode 104: Maximum Depth of Binary Tree",
            "Amazon, LinkedIn, Meta, Google, Microsoft, Apple",
            "O(N) - Visits all N nodes once.",
            "O(H) - Call stack depth equals tree height H.",
            "The depth of a tree is `1 + max(maxDepth(root.left), maxDepth(root.right))`.",
            "Optimal O(N) divide-and-conquer DFS.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))"""
        ),
        (
            "03_Diameter_of_Binary_Tree.py",
            "LeetCode 543: Diameter of Binary Tree",
            "Meta, Amazon, Google, Microsoft, Apple, Bloomberg",
            "O(N) - Computes height and updates diameter in a single bottom-up DFS pass.",
            "O(H) - Recursion stack depth of height H.",
            "At every node, the longest path passing through that node is `left_height + right_height`. Track the global maximum while returning `1 + max(left_height, right_height)` upward.",
            "Recomputing `maxDepth` at every node would take O(N²) time. Computing height and diameter simultaneously in bottom-up DFS runs in O(N) time.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter"""
        ),
        (
            "04_Balanced_Binary_Tree.py",
            "LeetCode 110: Balanced Binary Tree",
            "Amazon, Google, Meta, Spotify, Adobe",
            "O(N) - Single bottom-up DFS returning `-1` immediately on imbalance.",
            "O(H) - Call stack proportional to tree height H.",
            "Return the subtree height if balanced, or `-1` as a sentinel value as soon as any subtree has `abs(left - right) > 1`.",
            "Top-down height checks cost O(N²). Bottom-up DFS with a `-1` sentinel checks balance and height in a single O(N) pass.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1"""
        ),
        (
            "05_Same_Tree.py",
            "LeetCode 100: Same Tree",
            "Amazon, Google, Apple, Microsoft, LinkedIn",
            "O(N) - Visits corresponding nodes of both trees once.",
            "O(H) - Recursion stack depth of height H.",
            "Two trees are identical if their roots share the same value and their left and right subtrees are recursively identical.",
            "Short-circuits on the first structural or value mismatch in O(N) time.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)"""
        ),
        (
            "06_Subtree_of_Another_Tree.py",
            "LeetCode 572: Subtree of Another Tree",
            "Amazon, Meta, Microsoft, Google, Ebay",
            "O(N * M) - Checks `isSame` of size M at nodes of `root` of size N.",
            "O(H) - Recursion stack depth of `root`.",
            "Traverse `root`; at each node, check if the subtree rooted there is identical to `subRoot` using `isSameTree`.",
            "Clean recursive decomposition with immediate short-circuiting on mismatched root values.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        return False"""
        ),
        (
            "07_Lowest_Common_Ancestor_of_a_BST.py",
            "LeetCode 235: Lowest Common Ancestor of a Binary Search Tree",
            "LinkedIn, Meta, Amazon, Microsoft, Google, Bloomberg",
            "O(H) - Walks down one path of height H in the BST.",
            "O(1) - Iterative pointer traversal uses zero call stack memory.",
            "In a BST, if both `p` and `q` are greater than `curr.val`, move right; if both are smaller, move left. The first node where they split (or equal `curr`) is the LCA!",
            "Exploits the BST ordering property to walk directly down one path in O(H) time and O(1) space without visiting the rest of the tree.",
            """class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr"""
        ),
        (
            "08_Binary_Tree_Level_Order_Traversal.py",
            "LeetCode 102: Binary Tree Level Order Traversal",
            "Amazon, Meta, Microsoft, Bloomberg, LinkedIn, Apple, Google",
            "O(N) - Every node is enqueued and dequeued exactly once.",
            "O(N) - Queue holds at most one full level (up to N/2 nodes).",
            "Use Breadth-First Search (BFS) with a `deque`. At the start of each iteration, `len(q)` tells us the exact number of nodes in the current level.",
            "`collections.deque.popleft()` operates in O(1) time (unlike `list.pop(0)` which is O(N)), ensuring true O(N) level-order traversal.",
            """from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res"""
        ),
        (
            "09_Binary_Tree_Right_Side_View.py",
            "LeetCode 199: Binary Tree Right Side View",
            "Meta, Amazon, Bloomberg, TikTok, Microsoft, ByteDance",
            "O(N) - BFS visits each node once.",
            "O(W) - Queue stores at most the maximum width W of the tree.",
            "Perform level-order BFS and record the very last node processed in each level (`i == level_len - 1`).",
            "Captures the rightmost visible node at every depth even when the right subtree is shorter than the left subtree.",
            """from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if i == level_len - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res"""
        ),
        (
            "10_Count_Good_Nodes_in_Binary_Tree.py",
            "LeetCode 1448: Count Good Nodes in Binary Tree",
            "Microsoft, Amazon, Meta, Google, Apple",
            "O(N) - Preorder DFS visits each node once.",
            "O(H) - Call stack depth equals tree height H.",
            "Pass the maximum value seen along the path from root (`max_so_far`) down the DFS recursion. A node is 'good' if `node.val >= max_so_far`.",
            "Carrying `max_so_far` as a scalar parameter avoids storing or re-scanning ancestor paths, solving the problem in O(N) time.",
            """class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)"""
        ),
        (
            "11_Validate_Binary_Search_Tree.py",
            "LeetCode 98: Validate Binary Search Tree",
            "Amazon, Bloomberg, Microsoft, Meta, Google, Salesforce",
            "O(N) - Visits every node once with O(1) range comparison.",
            "O(H) - Recursion stack depth of height H.",
            "Every node in a valid BST must fall within a strict open interval `(low, high)` inherited from its ancestors: going left tightens `high = node.val`, going right tightens `low = node.val`.",
            "Checking only immediate children fails on deeper invalid descendants. Propagating `(low, high)` bounds validates the entire tree in one O(N) pass.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))"""
        ),
        (
            "12_Kth_Smallest_Element_in_a_BST.py",
            "LeetCode 230: Kth Smallest Element in a BST",
            "Uber, Amazon, Meta, Microsoft, Google, Apple",
            "O(H + k) - Walks down to the smallest leaf in O(H) and pops `k` nodes.",
            "O(H) - Iterative stack holds at most H ancestor nodes.",
            "Inorder traversal (`Left -> Node -> Right`) of a BST visits values in strictly sorted ascending order. Use an explicit stack to stop immediately at the `k`-th popped node.",
            "Iterative inorder stops as soon as the `k`-th element is found in O(H + k) time without traversing the entire N-node tree.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1"""
        ),
        (
            "13_Construct_Binary_Tree_From_Preorder_and_Inorder_Traversal.py",
            "LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal",
            "Amazon, Microsoft, Bloomberg, Google, Meta",
            "O(N) - Pre-maps inorder indices in a dict and builds each of the N nodes in O(1).",
            "O(N) - Dictionary of N inorder indices plus O(H) recursion stack.",
            "The next element in `preorder` is always the root of the current subtree, and its index in `inorder` splits the remaining elements into the left and right subtrees.",
            "Slicing lists and calling `inorder.index()` on every call takes O(N²) time. Pre-building an `inorder_idx` hash map and passing index bounds reduces construction to O(N) time!",
            """from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)"""
        ),
        (
            "14_Binary_Tree_Maximum_Path_Sum.py",
            "LeetCode 124: Binary Tree Maximum Path Sum",
            "Meta, Amazon, DoorDash, Google, Microsoft, Bloomberg",
            "O(N) - Single postorder DFS visiting each node once.",
            "O(H) - Recursion call stack proportional to tree height H.",
            "At each node, compute max non-negative gains from left and right (`max(dfs(child), 0)`). Update global `max_sum` with the split path `node.val + left_gain + right_gain`, and return the single-branch max `node.val + max(left_gain, right_gain)` to the parent.",
            "Simultaneously considers every node as the 'highest apex' of a split path while passing only valid extendable single paths upward in O(N) time.",
            """from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum"""
        ),
        (
            "15_Serialize_and_Deserialize_Binary_Tree.py",
            "LeetCode 297: Serialize and Deserialize Binary Tree",
            "Amazon, Meta, LinkedIn, Microsoft, Google, Uber, Citadel",
            "O(N) - Preorder traversal visits every node and null marker once.",
            "O(N) - Token list and recursion stack.",
            "Serialize using Preorder DFS (`Root, Left, Right`) recording `'N'` for `None` pointers. Deserialize by consuming tokens sequentially in the exact same Preorder DFS order.",
            "Preorder with explicit `'N'` null markers uniquely reconstructs the tree in a single O(N) pass without needing a second inorder array.",
            """class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()"""
        ),
    ],
    "08_Tries": [
        (
            "01_Implement_Trie_Prefix_Tree.py",
            "LeetCode 208: Implement Trie (Prefix Tree)",
            "Google, Amazon, Microsoft, Meta, Apple, Twitter, Uber",
            "O(L) - Insert, search, and startsWith each take O(L) where L is word length.",
            "O(N * L) - Total characters across inserted words stored as shared tree nodes.",
            "Each `TrieNode` holds a `children` dictionary mapping `{char: TrieNode}` and an `is_end` boolean flag marking complete words.",
            "Hash sets cannot answer prefix queries (`startsWith`) in O(L) without storing every prefix of every word. A Trie shares common prefixes and answers both exact and prefix queries in O(L) time.",
            """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True"""
        ),
        (
            "02_Design_Add_and_Search_Words_Data_Structure.py",
            "LeetCode 211: Design Add and Search Words Data Structure",
            "Meta, Amazon, Google, Apple, Rubrik, DoorDash",
            "O(L) for `addWord` and exact `search`; O(26^W * L) when W wildcard dots `.` appear.",
            "O(N * L) - Trie storage plus O(L) recursion stack for wildcard branching.",
            "Store words in a Trie. During `search`, normal characters step into `curr.children[ch]`, while a wildcard `'.'` recursively branches across all `curr.children.values()`.",
            "Prunes non-matching prefixes immediately in the Trie instead of scanning every stored word on wildcard queries.",
            """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, node: TrieNode) -> bool:
            curr = node
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    return any(dfs(i + 1, child) for child in curr.children.values())
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]
            return curr.is_end

        return dfs(0, self.root)"""
        ),
        (
            "03_Word_Search_II.py",
            "LeetCode 212: Word Search II",
            "Amazon, Uber, Karat, Microsoft, Google, Meta, Cisco",
            "O(M * N * 4 * 3^(L-1)) - Simultaneous Trie-guided DFS across the grid.",
            "O(W * L) - Trie storing W words of max length L.",
            "Insert all target words into a single Trie, then run DFS from each board cell stepping only into board neighbors that exist in the current `TrieNode.children`.",
            "Running separate Word Search for W words repeats grid traversals W times. A shared Trie searches for all W words simultaneously and prunes dead-end prefixes on the first mismatched letter.",
            """from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for ch in w:
                curr = curr.children.setdefault(ch, TrieNode())
            curr.word = w

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, parent: TrieNode):
            ch = board[r][c]
            curr = parent.children.get(ch)
            if not curr:
                return
            if curr.word:
                res.append(curr.word)
                curr.word = None
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr.children:
                    dfs(nr, nc, curr)
            board[r][c] = ch
            if not curr.children:
                parent.children.pop(ch)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return res"""
        ),
    ],
    "09_Heap_Priority_Queue": [
        (
            "01_Kth_Largest_Element_in_a_Stream.py",
            "LeetCode 703: Kth Largest Element in a Stream",
            "Amazon, Meta, Google, LinkedIn, Adobe",
            "O(log K) per `add` call - Min-heap capped at size K.",
            "O(K) - Stores only the K largest elements seen so far.",
            "Maintain a Min-Heap of size `k` containing the `k` largest elements. The smallest among the top `k` (sitting at `self.heap[0]`) is the exact Kth largest element!",
            "Keeping a sorted list costs O(N) per insertion. A size-K min-heap processes every new stream element in O(log K) time and reads the Kth largest in O(1).",
            """from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]"""
        ),
        (
            "02_Last_Stone_Weight.py",
            "LeetCode 1046: Last Stone Weight",
            "Amazon, Visa, Nvidia, LinkedIn, Google",
            "O(N log N) - O(N) heapify plus N smash rounds taking O(log N) each.",
            "O(N) - Max-heap simulated with negated stone weights.",
            "Negate all weights to simulate a Max-Heap using Python's `heapq` min-heap. Repeatedly pop the two heaviest stones `y` and `x`, pushing `y - x` back if they differ.",
            "Re-sorting the array after every smash takes O(N² log N). A max-heap extracts the two largest stones and re-inserts the remainder in O(log N) per step.",
            """from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first > second:
                heapq.heappush(heap, -(first - second))
        return -heap[0] if heap else 0"""
        ),
        (
            "03_K_Closest_Points_to_Origin.py",
            "LeetCode 973: K Closest Points to Origin",
            "Meta, Amazon, Google, Asana, Apple, Uber",
            "O(N + K log N) - Linear O(N) `heapify` followed by K `heappop` operations.",
            "O(N) - Heap of squared distances `(x² + y², x, y)`.",
            "Compare squared Euclidean distances `x*x + y*y` (skipping `sqrt`), `heapify` all points in O(N) time, and pop the `k` smallest.",
            "Bottom-up `heapq.heapify` builds the heap in O(N) linear time, and popping `k` times costs O(K log N)—faster than full O(N log N) sorting.",
            """from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(heap)
        return [[x, y] for _, x, y in [heapq.heappop(heap) for _ in range(k)]]"""
        ),
        (
            "04_Kth_Largest_Element_in_an_Array.py",
            "LeetCode 215: Kth Largest Element in an Array",
            "Meta, Amazon, LinkedIn, Google, Microsoft, Apple, Bloomberg",
            "O(N log K) - Maintains a min-heap of size K across N elements.",
            "O(K) - Heap stores at most K elements at any time.",
            "Maintain a Min-Heap of size `k`. After scanning all numbers and evicting anything smaller than the top `k`, `heap[0]` is the `k`-th largest element.",
            "Avoids O(N log N) full sort and avoids Quickselect's O(N²) worst-case degradation on duplicate-heavy inputs.",
            """from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]"""
        ),
        (
            "05_Task_Scheduler.py",
            "LeetCode 621: Task Scheduler",
            "Meta, Amazon, Google, Uber, Microsoft, DoorDash, Rubrik",
            "O(N) - Counts task frequencies and simulates cooldown cycles using a max-heap and queue.",
            "O(1) - At most 26 uppercase task types in the heap and cooldown queue.",
            "Always schedule the most frequent available task first (via a Max-Heap), then place its remaining count into a cooldown `deque` `(remaining_count, available_time)` until `time + n`.",
            "Greedily picking the highest-frequency task prevents getting stuck with identical tasks at the end, minimizing idle CPU cycles in O(N) time.",
            """from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time"""
        ),
        (
            "06_Design_Twitter.py",
            "LeetCode 355: Design Twitter",
            "Uber, Amazon, Google, Microsoft, Twitter, Coupang",
            "O(1) for `postTweet`/`follow`/`unfollow`; O(F + 10 log F) for `getNewsFeed` across F followed users.",
            "O(U + T) - Stores user follow sets and tweet lists.",
            "Store each user's tweets with a global timestamp counter, and use a Max-Heap to merge only the latest tweet from each followed user (just like Merge K Sorted Lists, stopping after 10 pops).",
            "Instead of merging and sorting all historical tweets of all followed users, lazy K-way heap merging inspects at most 10 tweets total!",
            """from typing import List
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
        self.follow_map[followerId].discard(followeeId)"""
        ),
        (
            "07_Find_Median_From_Data_Stream.py",
            "LeetCode 295: Find Median from Data Stream",
            "Amazon, Google, Meta, Microsoft, Apple, Goldman Sachs, Bloomberg",
            "O(log N) for `addNum` and O(1) for `findMedian`.",
            "O(N) - Two heaps (`small` max-heap and `large` min-heap) split the stream in half.",
            "Maintain two balanced heaps: `small` (a Max-Heap holding the smaller half of numbers) and `large` (a Min-Heap holding the larger half). Their tops sit right at the median!",
            "Keeping a sorted array requires O(N) shifts on every insertion. Two heaps balance in O(log N) and expose the median at their roots in O(1) time.",
            """import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (-self.small[0] + self.large[0]) / 2.0"""
        ),
    ],
}
