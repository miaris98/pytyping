"""
Curated deep explanations for built-in LeetCode solutions.
Provides two distinct pillars for every problem:
1. Code Walkthrough, Core Understanding & Why It Is the Most Efficient Solution (with dedicated audio narration)
2. Big O Runtime & Memory Complexity Analysis (with dedicated audio narration)
"""

CURATED_EXPLANATIONS = {
    "01_Two_Sum.py": {
        "title": "01 Two Sum",
        "core_understanding": (
            "Instead of searching for two numbers blindly, reframe the question: as we stand at any number 'num', "
            "we already know the exact partner we need: 'complement = target - num'. We just need a way to remember "
            "every number we have already passed and its index."
        ),
        "why_most_efficient": (
            "A naive brute-force solution uses nested loops to check every pair (i, j), taking O(N²) time. "
            "By trading O(N) memory for a Hash Map (Python dict), we reduce the partner lookup from an O(N) linear scan "
            "down to an O(1) constant-time hash lookup. We solve the entire problem in a single pass."
        ),
        "code_walkthrough": [
            "Initialize `seen = {}` as an empty dictionary mapping each value we've seen to its index.",
            "Loop through `nums` using `enumerate(nums)` so we have both the index `i` and value `num` simultaneously.",
            "Compute `complement = target - num`, which is the exact value needed to reach `target`.",
            "Check `if complement in seen:` — dictionary key lookup in Python is O(1) on average. If found, immediately return `[seen[complement], i]`.",
            "Otherwise, store `seen[num] = i` so future elements can match against the current number."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Two Sum and why a single-pass hash map is the most efficient solution. "
            "The core understanding is simple: when you look at any number, you already know the exact partner you need, which is target minus num. "
            "A brute-force approach checks every pair with nested loops in O of N squared time. "
            "Instead, we initialize an empty dictionary called seen. "
            "As we loop with enumerate to get both index i and value num, we calculate complement equals target minus num. "
            "We check if complement is already in seen. Because dictionary lookups are instant, if it's there, we immediately return seen of complement and i. "
            "Otherwise, we record seen of num equals i and continue."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We iterate through the list of N elements at most once. Inside the loop, computing the complement, "
            "checking `if complement in seen`, and inserting `seen[num] = i` each take O(1) average time in a hash table."
        ),
        "space_complexity": "O(N)",
        "space_explanation": (
            "In the worst case where the pair is at the very end of the array, the `seen` dictionary stores up to N - 1 "
            "key-value pairs, requiring O(N) auxiliary memory."
        ),
        "bigo_deep_dive": [
            "Best Case Time: O(1) if the first two elements sum to target.",
            "Worst & Average Case Time: O(N) single pass with O(1) amortized hash operations.",
            "Auxiliary Memory: O(N) for the `seen` dictionary storing `{value: index}` entries."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Two Sum. "
            "The Time Complexity is O of N linear time. We traverse the N elements of the array at most once, and each hash map lookup and insertion inside the loop takes O of 1 constant average time. "
            "The Space Complexity is O of N linear memory, because in the worst case the dictionary stores up to N minus 1 numbers and their indices before finding the matching pair."
        )
    },
    "02_Contains_Duplicate.py": {
        "title": "02 Contains Duplicate",
        "core_understanding": (
            "To detect if any value appears twice, we need a data structure that enforces uniqueness and answers "
            "membership queries ('have I seen this before?') instantaneously."
        ),
        "why_most_efficient": (
            "Comparing every element with every other element takes O(N²) time, and sorting the array first takes O(N log N) time. "
            "Using a Hash Set (`set()`) gives O(1) average membership checks and allows early termination the exact moment the first duplicate is encountered."
        ),
        "code_walkthrough": [
            "Initialize `seen = set()` to track unique numbers encountered so far.",
            "Iterate through each `num` in `nums`.",
            "Check `if num in seen:` — if True, we found a duplicate and can immediately return `True` without checking the rest of the list.",
            "Add `seen.add(num)` to record the current number.",
            "If the loop finishes without returning, all elements are distinct, so return `False`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Contains Duplicate. "
            "The core understanding is that a Hash Set is purpose-built for fast uniqueness checks. "
            "While sorting takes N log N time and brute force takes N squared time, a Python set checks membership in constant time and stops early as soon as a duplicate appears. "
            "In the code, we start with seen equals set. We loop over each num in nums. "
            "If num is already in seen, we immediately return True. Otherwise, we call seen dot add num. "
            "If we finish the whole loop, no duplicates exist, so we return False."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We scan the array of N elements at most once. Set membership (`num in seen`) and insertion (`seen.add(num)`) "
            "each operate in O(1) average time."
        ),
        "space_complexity": "O(N)",
        "space_explanation": (
            "In the worst case where there are no duplicates, the hash set `seen` grows to hold all N elements."
        ),
        "bigo_deep_dive": [
            "Time vs Sorting Trade-off: Sorting uses O(1) space (if in-place) at the cost of O(N log N) time; the Hash Set achieves optimal O(N) time.",
            "Early Exit Advantage: If a duplicate occurs at index 1, runtime is effectively O(1)."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Contains Duplicate. "
            "The Time Complexity is O of N, because we visit each number at most once and perform constant-time O of 1 hash set lookups and insertions. "
            "The Space Complexity is O of N, as the seen set stores up to N unique integers in the worst case when all elements are distinct."
        )
    },
    "03_Valid_Anagram.py": {
        "title": "03 Valid Anagram",
        "core_understanding": (
            "Two strings are anagrams if and only if they have the exact same length and the exact same frequency count "
            "for every character."
        ),
        "why_most_efficient": (
            "Sorting both strings (`sorted(s) == sorted(t)`) takes O(N log N) time. Instead, counting character frequencies "
            "with a hash map—incrementing for `s` and decrementing for `t`—runs in optimal O(N) linear time."
        ),
        "code_walkthrough": [
            "First guard clause: `if len(s) != len(t): return False`. Strings of different lengths can never be anagrams.",
            "Create `count = defaultdict(int)` so any new character defaults to a count of 0.",
            "First loop: `for char in s: count[char] += 1` tallies every character in string `s`.",
            "Second loop: `for char in t: count[char] -= 1` subtracts each character in `t`.",
            "Inside the second loop, `if count[char] < 0: return False` catches immediately if `t` has more of `char` than `s`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Valid Anagram. "
            "Two strings are anagrams if they contain the exact same characters in the exact same quantities. "
            "Sorting both strings would take N log N time, but frequency counting solves this in optimal linear time. "
            "First, we check if len of s is not equal to len of t, returning False immediately if their lengths differ. "
            "Next, we initialize count as a defaultdict of int. "
            "We loop over every char in s and increment count of char. "
            "Then we loop over every char in t, decrement count of char, and if count of char ever drops below zero, we immediately return False. "
            "Since both strings have equal length and no count went negative, we return True."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "Where N is the length of the strings. We iterate over `s` once (N steps) and `t` once (N steps), "
            "doing O(1) dictionary increments and decrements at each step."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "Although we use a dictionary `count`, the number of distinct lowercase English letters is bounded by 26 "
            "(or a fixed alphabet size K), which is O(1) constant space—or O(K) for general Unicode."
        ),
        "bigo_deep_dive": [
            "Runtime: 2N constant-time operations simplify to O(N).",
            "Memory: At most 26 keys for lowercase English letters, meaning memory does not grow as string length N grows to millions."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Valid Anagram. "
            "The Time Complexity is O of N linear time, because we do two simple passes of length N over the strings with O of 1 hash map updates. "
            "The Space Complexity is O of 1 constant space for lowercase English letters, because the frequency map can hold at most 26 keys regardless of how long the input strings are."
        )
    },
    "04_Group_Anagrams.py": {
        "title": "04 Group Anagrams",
        "core_understanding": (
            "All anagrams share an identical character frequency signature. If we convert every word into a 26-element "
            "tuple of character counts `(count_a, count_b, ..., count_z)`, all anagrams will map to the exact same dictionary key."
        ),
        "why_most_efficient": (
            "Sorting each word of length K to form a key takes O(K log K) per word, or O(N * K log K) total. "
            "Counting characters into a fixed array of size 26 avoids sorting completely, reducing key construction to O(K) "
            "and achieving the theoretical optimal O(N * K) time."
        ),
        "code_walkthrough": [
            "Initialize `groups = defaultdict(list)` to map each 26-count tuple key to a list of matching words.",
            "Outer loop: iterate over each `word` in `strs`.",
            "Initialize `key = [0] * 26` to count occurrences of `'a'` through `'z'`.",
            "Inner loop: for each `char` in `word`, increment `key[ord(char) - ord('a')] += 1` using ASCII offset math.",
            "Convert `key` to an immutable `tuple(key)` (since Python lists cannot be dictionary keys) and append `word` to `groups[tuple(key)]`.",
            "Return `list(groups.values())` containing all grouped anagram lists."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Group Anagrams and why character-count tuples beat sorting. "
            "The core idea is that every group of anagrams shares the exact same letter counts from a to z. "
            "If you sorted each word of length K, it would cost N times K log K. By using a 26-slot frequency array instead, we drop the log K factor and achieve optimal N times K time. "
            "In the code, we create groups as a defaultdict of list. For each word in strs, we initialize key as 26 zeros. "
            "For each char in word, we use ord of char minus ord of a to increment the exact index from 0 to 25. "
            "We convert the list to tuple of key so it is hashable, append the word to groups, and finally return list of groups dot values."
        ),
        "time_complexity": "O(N · K)",
        "time_explanation": (
            "Where N is the number of strings and K is the maximum length of a string. For each of the N words, "
            "we iterate over its K characters and build a 26-element tuple in O(K + 26) = O(K) time."
        ),
        "space_complexity": "O(N · K)",
        "space_explanation": (
            "The `groups` dictionary stores all N strings of up to length K, plus at most N tuple keys of size 26."
        ),
        "bigo_deep_dive": [
            "Why Tuple Conversion Matters: Python `list` is mutable and unhashable; `tuple(key)` takes O(26) = O(1) time and makes a valid dict key.",
            "Comparison: O(N · K) character counting vs O(N · K log K) string sorting."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Group Anagrams. "
            "The Time Complexity is O of N times K, where N is the number of words and K is the maximum length of a word. We visit every character of every word once and convert a fixed 26-element list into a tuple. "
            "The Space Complexity is O of N times K to store all the grouped words and their 26-integer frequency keys inside the hash map."
        )
    },
    "05_Top_K_Frequent_Elements.py": {
        "title": "05 Top K Frequent Elements",
        "core_understanding": (
            "First count how often each number appears, then maintain a Min-Heap of size at most K. "
            "Whenever the heap exceeds size K, pop the smallest frequency—leaving only the K highest frequencies at the end."
        ),
        "why_most_efficient": (
            "Sorting all unique frequencies takes O(N log N) time. By keeping a min-heap capped at size K, each push/pop "
            "only costs O(log K) instead of O(log N), giving O(N log K) time and O(K) heap space."
        ),
        "code_walkthrough": [
            "Use `counts = Counter(nums)` to build a frequency map `{number: frequency}` in one O(N) pass.",
            "Initialize an empty list `heap = []` to act as our min-heap.",
            "Iterate `for num, freq in counts.items():` over the unique numbers and their frequencies.",
            "Push `(freq, num)` using `heapq.heappush(heap, (freq, num))` — putting `freq` first so Python orders tuples by frequency.",
            "If `len(heap) > k:`, evict the smallest frequency element via `heapq.heappop(heap)`.",
            "Finally, extract the numbers with a list comprehension: `[num for freq, num in heap]`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Top K Frequent Elements. "
            "Instead of sorting all unique numbers in N log N time, we only care about the top K. "
            "We first count every number's frequency in linear time using Counter of nums. "
            "Then we maintain a min-heap of size K. For each num and freq in counts dot items, we push the tuple freq comma num onto the heap. "
            "Notice freq goes first in the tuple so heapq compares by frequency. "
            "Whenever len of heap exceeds k, we pop the smallest frequency with heapq dot heappop. "
            "At the end, the heap contains the exact top K elements, which we return with a list comprehension."
        ),
        "time_complexity": "O(N log K)",
        "time_explanation": (
            "Building `Counter(nums)` takes O(N) time. Pushing and popping from a heap bounded by size K for at most N unique "
            "elements takes O(N log K) time."
        ),
        "space_complexity": "O(N)",
        "space_explanation": (
            "The `counts` hash map stores up to N unique elements, while the `heap` itself only uses O(K) auxiliary space."
        ),
        "bigo_deep_dive": [
            "Frequency Map Step: O(N) time and O(N) space.",
            "Bounded Min-Heap Step: O(U log K) time where U ≤ N is the number of unique elements, and O(K) heap space."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Top K Frequent Elements. "
            "The Time Complexity is O of N log K. Counting frequencies takes O of N time, and maintaining a min-heap of size at most K across the unique elements takes O of N log K time, which is strictly faster than O of N log N when K is small. "
            "The Space Complexity is O of N to store the frequency Counter map, plus O of K space for the min-heap."
        )
    },
    "01_Valid_Palindrome.py": {
        "title": "01 Valid Palindrome",
        "core_understanding": (
            "A palindrome reads the same forwards and backwards. By placing one pointer at the start (`left`) and one at the end (`right`), "
            "we can walk inward from both ends simultaneously, skipping punctuation and spaces on the fly."
        ),
        "why_most_efficient": (
            "Creating a filtered lowercase string and reversing it (`s == s[::-1]`) allocates two new O(N) strings in memory. "
            "Two pointers inspect characters directly in-place using O(1) constant memory and stop early on the first mismatch."
        ),
        "code_walkthrough": [
            "Initialize `left, right = 0, len(s) - 1` at the two ends of the string.",
            "Loop `while left < right:` until the two pointers meet or cross in the middle.",
            "Advance `left += 1` in an inner while loop whenever `not s[left].isalnum()` to skip spaces and symbols.",
            "Decrement `right -= 1` in an inner while loop whenever `not s[right].isalnum()`.",
            "Compare `if s[left].lower() != s[right].lower(): return False`.",
            "Move both pointers inward (`left += 1`, `right -= 1`). If they cross without mismatch, return `True`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Valid Palindrome using Two Pointers. "
            "Building a new filtered string and reversing it wastes O of N memory. Instead, we place left at 0 and right at len of s minus 1 to compare characters in-place with zero extra string allocations. "
            "While left is less than right, we first advance left past any non-alphanumeric characters using s of left dot isalnum. "
            "We do the same for right, stepping backward past spaces or punctuation. "
            "Then we compare s of left dot lower with s of right dot lower. If they don't match, we return False immediately. "
            "Otherwise, we step both pointers inward and return True once they meet."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "The `left` pointer only moves right and the `right` pointer only moves left. Even with the inner `while` loops, "
            "each character in the string of length N is visited at most once."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "We only store two integer index pointers (`left` and `right`) and never allocate a copy of the string."
        ),
        "bigo_deep_dive": [
            "Amortized Nested Loops: Although there are inner `while` loops inside the outer `while`, `left` and `right` together take at most N total steps.",
            "Memory Optimality: O(1) auxiliary space vs O(N) for string slicing `s[::-1]`."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Valid Palindrome. "
            "The Time Complexity is O of N linear time. Don't be fooled by the inner while loops: left only increments and right only decrements, so they cross after visiting each of the N characters at most once. "
            "The Space Complexity is O of 1 constant memory, because we validate the string in-place using only two integer pointers."
        )
    },
    "02_Two_Sum_II.py": {
        "title": "02 Two Sum II (Sorted Array)",
        "core_understanding": (
            "Because the input array is already sorted in ascending order, the sum of the smallest (`left`) and largest (`right`) "
            "elements tells us with 100% certainty which pointer to move: if the sum is too small, we must increase `left`; "
            "if the sum is too large, we must decrease `right`."
        ),
        "why_most_efficient": (
            "Standard Two Sum uses an O(N) hash map because the array is unsorted. Here, exploiting the sorted order with Two Pointers "
            "achieves the same O(N) runtime while shrinking extra memory from O(N) down to O(1)!"
        ),
        "code_walkthrough": [
            "Set `left, right = 0, len(numbers) - 1` at the smallest and largest values.",
            "Loop `while left < right:`.",
            "Compute `current_sum = numbers[left] + numbers[right]`.",
            "If `current_sum == target:`, return 1-based indices `[left + 1, right + 1]` as required by the problem.",
            "If `current_sum < target:`, we need a larger sum, so move `left += 1`.",
            "Otherwise (`current_sum > target`), we need a smaller sum, so move `right -= 1`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Two Sum 2 on a sorted array. "
            "In regular Two Sum, we needed an O of N hash map. Because this array is sorted, we can achieve O of 1 constant space using Two Pointers! "
            "We place left at index 0 and right at the end of the array. "
            "In each step, we compute current_sum equals numbers of left plus numbers of right. "
            "If current_sum equals target, we return left plus 1 and right plus 1 for 1-indexed output. "
            "If current_sum is less than target, the only way to make the sum bigger is to move left forward. "
            "If current_sum is too big, we move right backward."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "In each iteration, either `left` increments or `right` decrements, so the loop runs at most N times."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "No hash map or extra arrays are allocated—only `left`, `right`, and `current_sum` integer variables."
        ),
        "bigo_deep_dive": [
            "Time: O(N) worst case, O(1) per iteration.",
            "Space: O(1) auxiliary space—the primary advantage over the Hash Map approach on sorted data."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Two Sum 2. "
            "The Time Complexity is O of N linear time, because at every step we eliminate either the leftmost or rightmost candidate, taking at most N steps total. "
            "The Space Complexity is O of 1 constant space, using zero auxiliary data structures."
        )
    },
    "03_3Sum.py": {
        "title": "03 3Sum",
        "core_understanding": (
            "By sorting the array first, we reduce 3Sum to fixing one number `nums[i]` and running the O(N) Two-Pointer "
            "Two Sum II algorithm on the remaining subarray `i + 1 ... n - 1` while skipping duplicate values."
        ),
        "why_most_efficient": (
            "Checking all triplets takes O(N³) time and requires a hash set to deduplicate triplets. "
            "Sorting in O(N log N) plus a two-pointer sweep for each `i` reduces runtime to O(N²) and lets us skip duplicates "
            "by simply advancing pointers past identical adjacent numbers."
        ),
        "code_walkthrough": [
            "Call `nums.sort()` so duplicates are adjacent and two-pointer monotonic logic applies.",
            "Loop `for i in range(n - 2):` to pick the first element of the triplet.",
            "Skip duplicate anchors with `if i > 0 and nums[i] == nums[i - 1]: continue`.",
            "Set `left, right = i + 1, n - 1` and loop `while left < right:`.",
            "Calculate `total = nums[i] + nums[left] + nums[right]`. Adjust `left += 1` if `total < 0` or `right -= 1` if `total > 0`.",
            "When `total == 0`, append the triplet, skip duplicate `left` and `right` values with inner `while` loops, then step both inward."
        ],
        "walkthrough_audio_text": (
            "Let's walk through 3Sum. "
            "A naive triple loop takes O of N cubed time. Instead, we sort the array first, which lets us fix the first number at index i and solve the rest with Two Pointers in O of N squared total time. "
            "First, we call nums dot sort. Then we loop i from 0 to n minus 2. "
            "If i is greater than 0 and nums of i equals the previous number, we continue so we never generate duplicate triplets. "
            "Next, we set left to i plus 1 and right to n minus 1. "
            "While left is less than right, we sum the three numbers. If total is negative, we increment left; if positive, we decrement right. "
            "When total is zero, we append the triplet, skip any duplicate values on left and right, and move both pointers inward."
        ),
        "time_complexity": "O(N²)",
        "time_explanation": (
            "Sorting takes O(N log N) time. The outer loop runs N times, and for each `i`, the `left` and `right` pointers "
            "sweep the remaining elements in O(N) time, giving O(N log N + N²) = O(N²)."
        ),
        "space_complexity": "O(1) / O(N)",
        "space_explanation": (
            "Excluding the output list `result`, the two-pointer search uses O(1) pointer variables (Python's Timsort uses up to O(N) temporary sorting space)."
        ),
        "bigo_deep_dive": [
            "Sorting Step: O(N log N) is dominated by the O(N²) two-pointer nested sweep.",
            "Deduplication: Handled in O(1) space via adjacent element comparisons rather than an O(N²) hash set."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for 3Sum. "
            "The Time Complexity is O of N squared. Sorting the array takes N log N time, and then for each of the N elements, our left and right pointers scan the remainder of the array in linear O of N time. "
            "The auxiliary Space Complexity is O of 1 beyond sorting and the output list, because deduplication is handled in-place by skipping equal adjacent elements."
        )
    },
    "04_Container_With_Most_Water.py": {
        "title": "04 Container With Most Water",
        "core_understanding": (
            "The water held between two lines is `min(height[left], height[right]) * (right - left)`. "
            "Because the shorter line caps the water height, keeping the shorter line while shrinking the width can NEVER "
            "produce a larger area—so we must always move the pointer at the shorter line inward."
        ),
        "why_most_efficient": (
            "Testing all pairs of lines takes O(N²) time. Starting at maximum width (`left = 0, right = n - 1`) and greedily "
            "discarding the shorter boundary eliminates N - 1 suboptimal pairs on every single step, finding the global maximum in O(N) time."
        ),
        "code_walkthrough": [
            "Initialize `left, right = 0, len(height) - 1` for the widest possible container, and `max_water = 0`.",
            "Loop `while left < right:`.",
            "Calculate `current_water = min(height[left], height[right]) * (right - left)`.",
            "Update `max_water = max(max_water, current_water)`.",
            "Greedy step: `if height[left] < height[right]: left += 1` else `right -= 1` to replace the limiting shorter wall.",
            "Return `max_water` once the pointers meet."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Container With Most Water. "
            "The area of water is always limited by the shorter of the two walls times the distance between them. "
            "If we start with left at 0 and right at the end, we have the maximum possible width. "
            "Why is moving the shorter wall always optimal? Because as we move inward, the width shrinks; the only way the area can ever increase is if we find a taller wall to replace the shorter limiting wall. "
            "In each iteration, we calculate current_water as min of height left and height right times right minus left, update max_water, and move whichever pointer has the smaller height inward."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We start `left` and `right` at opposite ends and move one pointer inward per step, taking exactly N - 1 iterations."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "Uses only four scalar integer variables (`left`, `right`, `max_water`, `current_water`)."
        ),
        "bigo_deep_dive": [
            "Runtime: Single pass of N - 1 area calculations, each taking O(1) arithmetic.",
            "Memory: Strictly O(1) constant space."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Container With Most Water. "
            "The Time Complexity is O of N linear time, because at every step we either increment left or decrement right, completing in exactly N minus 1 steps. "
            "The Space Complexity is O of 1 constant memory, using only a few integer variables."
        )
    },
    "01_Best_Time_to_Buy_and_Sell_Stock.py": {
        "title": "01 Best Time to Buy and Sell Stock",
        "core_understanding": (
            "To maximize profit on any selling day, you would always want to have bought at the lowest price seen on any prior day. "
            "So as we walk through the prices chronologically, we just track two numbers: the lowest price seen so far (`min_price`) "
            "and the best profit achievable (`max_profit`)."
        ),
        "why_most_efficient": (
            "Checking every buy-sell pair `(i, j)` takes O(N²) time. Maintaining a running minimum in a single forward pass "
            "computes the best buy day for every possible sell day in O(N) time and O(1) memory."
        ),
        "code_walkthrough": [
            "Initialize `min_price = float('inf')` so the very first price becomes our initial minimum, and `max_profit = 0`.",
            "Loop `for price in prices:` through each day's stock price.",
            "If `price < min_price:`, we found a cheaper buying day, so update `min_price = price`.",
            "Else, calculate the profit of selling today (`price - min_price`) and update `max_profit = max(max_profit, price - min_price)`.",
            "Return `max_profit` at the end."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Best Time to Buy and Sell Stock. "
            "The key intuition is that if you sell on day i, the best day you could have bought is simply the lowest price before day i. "
            "Instead of nested loops in O of N squared time, we track min_price initialized to infinity and max_profit initialized to 0. "
            "As we loop over each price in prices, if price is less than min_price, we update min_price. "
            "Otherwise, we check if selling today at price minus min_price beats our max_profit. "
            "After one clean pass, we return max_profit."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We iterate through the `prices` array of length N once, doing O(1) comparison and subtraction per element."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "Only two scalar variables (`min_price` and `max_profit`) are kept in memory."
        ),
        "bigo_deep_dive": [
            "Time: O(N) single pass.",
            "Space: O(1) constant auxiliary memory."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Best Time to Buy and Sell Stock. "
            "The Time Complexity is O of N linear time, since we scan the array of N daily prices once with constant-time comparisons. "
            "The Space Complexity is O of 1 constant memory, requiring only two variables regardless of input size."
        )
    },
    "02_Longest_Substring_Without_Repeating_Characters.py": {
        "title": "02 Longest Substring Without Repeating Characters",
        "core_understanding": (
            "Maintain a sliding window `[left, right]` that always contains unique characters. When `s[right]` is a duplicate "
            "of a character already inside the current window, jump `left` directly past the previous occurrence of that character."
        ),
        "why_most_efficient": (
            "Checking all substrings takes O(N³) or O(N²) time. Even a basic sliding window with a `set` increments `left` one by one. "
            "By storing the last seen index of each character in a dict `char_index`, `left` can jump straight to `char_index[char] + 1` in O(1) time!"
        ),
        "code_walkthrough": [
            "Initialize `char_index = {}` mapping `{char: last_seen_index}`, `max_length = 0`, and window start `left = 0`.",
            "Loop `for right, char in enumerate(s):` to expand the right boundary of the window.",
            "Check `if char in char_index and char_index[char] >= left:` — the `>= left` check ensures the duplicate is actually inside our active window.",
            "If so, shrink the window by jumping `left = char_index[char] + 1`.",
            "Update `char_index[char] = right` with the character's newest index.",
            "Update `max_length = max(max_length, right - left + 1)` and return `max_length` after the loop."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Longest Substring Without Repeating Characters. "
            "We use a Sliding Window from left to right, paired with a dictionary called char_index that remembers the latest index of every character. "
            "Why is this the most efficient approach? Because whenever we hit a duplicate character inside our current window, we don't have to shrink left one step at a time—we jump left directly to char_index of char plus 1 in O of 1 time! "
            "As we loop with enumerate to get right and char, we check if char is in char_index and its stored index is greater than or equal to left. "
            "If so, we jump left forward. Then we update char_index of char to right, and update max_length with right minus left plus 1."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "The `right` pointer visits each of the N characters once, and `left` jumps forward in O(1) time using hash map lookups."
        ),
        "space_complexity": "O(min(N, M))",
        "space_explanation": (
            "The `char_index` dictionary stores at most one entry per unique character in the alphabet of size M (e.g., 128 ASCII chars), which is O(1) bounded or O(min(N, M))."
        ),
        "bigo_deep_dive": [
            "Runtime: Strictly 1 pass (N iterations) vs 2N iterations for a standard set-based sliding window.",
            "Memory: Bounded by the character set size (at most 128 ASCII / 256 extended ASCII keys)."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Longest Substring Without Repeating Characters. "
            "The Time Complexity is O of N linear time, because the right pointer scans from 0 to N minus 1 once, and each dictionary lookup and left pointer jump takes O of 1 constant time. "
            "The Space Complexity is O of min N comma M, where M is the size of the character set, since char_index only stores the latest index for each distinct character."
        )
    },
    "01_Valid_Parentheses.py": {
        "title": "01 Valid Parentheses",
        "core_understanding": (
            "Nested brackets follow a Last-In, First-Out (LIFO) discipline: the most recently opened bracket must be "
            "the very first one closed. A Stack naturally models this exact LIFO order."
        ),
        "why_most_efficient": (
            "Repeatedly replacing `'()'`, `'[]'`, and `'{}'` in the string takes O(N²) time. "
            "Using a Stack with a lookup dictionary processes every bracket in a single O(N) pass and immediately catches mismatches."
        ),
        "code_walkthrough": [
            "Create `matching = {')': '(', '}': '{', ']': '['}` mapping each closing bracket to its required opening partner.",
            "Initialize `stack = []` to hold currently open brackets.",
            "Loop `for char in s:` over each character.",
            "If `char in matching:` (meaning `char` is a closing bracket), check `if not stack or stack[-1] != matching[char]: return False`, then `stack.pop()`.",
            "Else (`char` is an opening bracket), push it with `stack.append(char)`.",
            "Finally, `return len(stack) == 0` to ensure no unclosed opening brackets remain."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Valid Parentheses. "
            "Because the most recently opened bracket must always be closed first, a Last-In First-Out stack is the ideal data structure. "
            "We define a dictionary called matching that maps each closing bracket to its corresponding opening bracket, and initialize an empty list as our stack. "
            "As we loop over each char in s, if char is in matching, it's a closing bracket: we check if the stack is empty or if the top of the stack, stack of minus 1, does not equal matching of char—returning False if so, or popping the stack if it matches. "
            "Otherwise, it's an opening bracket, so we append it to the stack. At the end, we return len of stack equals 0."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We process each of the N characters once. Pushing (`append`), popping (`pop`), and dictionary lookup each take O(1) time."
        ),
        "space_complexity": "O(N)",
        "space_explanation": (
            "In the worst case (e.g., `'((((((('`), all N characters are pushed onto the `stack`, consuming O(N) memory."
        ),
        "bigo_deep_dive": [
            "Time: O(1) per character × N characters = O(N).",
            "Space: O(N) stack storage + O(1) for the 3-entry `matching` dictionary."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Valid Parentheses. "
            "The Time Complexity is O of N linear time, as each character is pushed and popped from the stack at most once in O of 1 time. "
            "The Space Complexity is O of N, because if the string consists entirely of opening brackets, the stack will grow to size N."
        )
    },
    "02_Min_Stack.py": {
        "title": "02 Min Stack",
        "core_understanding": (
            "If we only stored a single `min_val` variable, popping that minimum element would force an O(N) scan to find "
            "the new minimum. By maintaining a parallel `min_stack` that records the minimum at every stack depth, "
            "we always know the minimum in O(1) time even after any number of pops!"
        ),
        "why_most_efficient": (
            "Scanning the stack on `getMin()` takes O(N) time, and keeping a heap takes O(log N) per push/pop. "
            "Synchronizing a second `min_stack` guarantees strict O(1) worst-case time for every single operation (`push`, `pop`, `top`, `getMin`)."
        ),
        "code_walkthrough": [
            "In `__init__`, initialize two lists: `self.stack = []` for values and `self.min_stack = []` for running minimums.",
            "In `push(val)`, append `val` to `self.stack`, compute `min_val = min(val, self.min_stack[-1] if self.min_stack else val)`, and append `min_val` to `self.min_stack`.",
            "In `pop()`, pop from both `self.stack.pop()` and `self.min_stack.pop()` to keep them perfectly synchronized.",
            "In `top()`, return `self.stack[-1]`.",
            "In `getMin()`, return `self.min_stack[-1]` in O(1) time."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Min Stack. "
            "The challenge is supporting getMin in O of 1 constant time even after elements are popped. "
            "If you only kept a single minimum variable, popping it would force an O of N search for the next smallest value. "
            "Instead, we keep two stacks in lockstep: self dot stack for the actual values, and self dot min_stack where each slot stores the minimum of all elements at or below that depth. "
            "On push, we append val to stack, and append the minimum of val and min_stack's top to min_stack. "
            "On pop, we pop from both stacks. Then both top and getMin simply return the last element of their respective stacks in O of 1 time."
        ),
        "time_complexity": "O(1)",
        "time_explanation": (
            "Every method (`push`, `pop`, `top`, `getMin`) performs only list index lookups (`[-1]`), `append`, or `pop` at the end of a dynamic array, which are all O(1)."
        ),
        "space_complexity": "O(N)",
        "space_explanation": (
            "Storing N elements across two parallel stacks uses 2N slots, which simplifies to O(N) memory."
        ),
        "bigo_deep_dive": [
            "Per-Operation Time: O(1) for `push`, O(1) for `pop`, O(1) for `top`, and O(1) for `getMin`.",
            "Space Overhead: One extra integer per pushed element in `min_stack`."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Min Stack. "
            "The Time Complexity is O of 1 constant time for all four operations: push, pop, top, and getMin. "
            "The Space Complexity is O of N linear memory, because for N pushed elements we store N values in self dot stack and N running minimums in self dot min_stack."
        )
    },
    "01_Binary_Search.py": {
        "title": "01 Binary Search",
        "core_understanding": (
            "In a sorted array, checking the middle element immediately tells us which half of the array the target can live in, "
            "allowing us to throw away 50% of the remaining search space on every single comparison."
        ),
        "why_most_efficient": (
            "A linear scan (`for x in nums`) takes O(N) time. Binary search cuts the problem size in half each step "
            "(N -> N/2 -> N/4 -> ... -> 1), finding any element among 1,000,000 items in at most 20 comparisons: O(log N) time."
        ),
        "code_walkthrough": [
            "Initialize search boundaries `low, high = 0, len(nums) - 1`.",
            "Loop `while low <= high:` (using `<=` so single-element ranges are still checked).",
            "Calculate midpoint `mid = low + (high - low) // 2` (a classic overflow-safe formula equivalent to `(low + high) // 2`).",
            "If `nums[mid] == target: return mid`.",
            "If `nums[mid] < target:`, target must be in the right half, so set `low = mid + 1`.",
            "Else (`nums[mid] > target`), target must be in the left half, so set `high = mid - 1`. Return `-1` if the loop ends."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Binary Search. "
            "Because the array is sorted, comparing target against the middle element lets us eliminate half of the remaining array on every step, reducing O of N linear time to O of log N logarithmic time. "
            "We start with low at 0 and high at len of nums minus 1, and loop while low is less than or equal to high. "
            "We compute mid as low plus high minus low integer divided by 2. "
            "If nums of mid equals target, we return mid. If nums of mid is less than target, we discard the left half by setting low to mid plus 1. "
            "Otherwise, we discard the right half by setting high to mid minus 1. If the pointers cross without finding target, we return minus 1."
        ),
        "time_complexity": "O(log N)",
        "time_explanation": (
            "Each iteration halves the search interval `high - low`. An interval of size N can be halved at most log₂(N) times."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "Iterative binary search uses only three integer index variables (`low`, `high`, `mid`), requiring O(1) constant memory."
        ),
        "bigo_deep_dive": [
            "Logarithmic Scaling: For N = 1,000,000,000 elements, O(log₂ N) takes at most 30 iterations!",
            "Iterative vs Recursive: Iterative uses O(1) space, whereas recursive binary search would use O(log N) call stack space."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Binary Search. "
            "The Time Complexity is O of log N logarithmic time, because we divide the search space by 2 on every iteration. "
            "The Space Complexity is O of 1 constant memory, since our iterative implementation only tracks three integer variables: low, high, and mid."
        )
    },
    "02_Search_2D_Matrix.py": {
        "title": "02 Search a 2D Matrix",
        "core_understanding": (
            "Because each row is sorted and the first number of each row is greater than the last number of the previous row, "
            "the entire M × N matrix is logically equivalent to a single sorted 1D array of length `M * N`. "
            "Any 1D index `mid` maps directly to 2D coordinates `(row, col) = divmod(mid, n)`!"
        ),
        "why_most_efficient": (
            "Scanning the matrix takes O(M * N) time. Treating it as a virtual 1D array lets us run standard Binary Search "
            "from `0` to `M * N - 1` without flattening or copying the matrix, achieving O(log(M * N)) time and O(1) space."
        ),
        "code_walkthrough": [
            "Guard against empty input: `if not matrix or not matrix[0]: return False`.",
            "Get dimensions `m, n = len(matrix), len(matrix[0])` and set 1D bounds `low, high = 0, m * n - 1`.",
            "Loop `while low <= high:` and compute `mid = (low + high) // 2`.",
            "Convert 1D index `mid` into 2D coordinates using `row, col = divmod(mid, n)` (which computes `mid // n` and `mid % n`).",
            "Read `val = matrix[row][col]`. If `val == target`, return `True`; if `val < target`, set `low = mid + 1`; else `high = mid - 1`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Search a 2D Matrix. "
            "Because every row is sorted and continues where the previous row left off, we can imagine the M by N matrix as a single sorted 1D array of length M times N—without actually copying any data! "
            "We set low to 0 and high to m times n minus 1. "
            "Inside the binary search loop, after computing mid, the magic line is row comma col equals divmod of mid comma n, which divides by the number of columns to get the row and takes the remainder to get the column. "
            "We compare matrix of row and col against target, adjusting low or high just like 1D binary search."
        ),
        "time_complexity": "O(log(M · N))",
        "time_explanation": (
            "Binary search over `M * N` virtual elements takes log₂(M · N) = log(M) + log(N) steps, with O(1) coordinate math per step."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "We never flatten the matrix in memory; we compute `(row, col)` on the fly using integer division and modulo."
        ),
        "bigo_deep_dive": [
            "Logarithmic Identity: O(log(M · N)) is mathematically equal to O(log M + log N).",
            "Zero Copy: `divmod(mid, n)` translates 1D to 2D indices in O(1) time and O(1) space."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Search a 2D Matrix. "
            "The Time Complexity is O of log M times N, which is equivalent to O of log M plus log N, because we halve the M times N search range on every step. "
            "The Space Complexity is O of 1 constant memory, as we map 1D indices to 2D row and column coordinates mathematically without allocating a flattened array."
        )
    },
    "01_Reverse_Linked_List.py": {
        "title": "01 Reverse Linked List",
        "core_understanding": (
            "To reverse a singly linked list in-place, walk through the list node by node and flip each node's `.next` pointer "
            "to point backward at `prev`—making sure to save `curr.next` in `next_temp` before overwriting it!"
        ),
        "why_most_efficient": (
            "Copying values into an array or using recursion takes O(N) auxiliary memory. "
            "Iterative three-pointer reversal (`prev`, `curr`, `next_temp`) rewires the existing nodes directly in-place using O(1) memory."
        ),
        "code_walkthrough": [
            "Initialize `prev = None` (which will become the new tail's `.next`) and `curr = head`.",
            "Loop `while curr:` until we walk past the end of the original list.",
            "Save the rest of the list first: `next_temp = curr.next` so we don't lose our bridge forward.",
            "Reverse the link: `curr.next = prev`.",
            "Advance both pointers one step forward: `prev = curr` and `curr = next_temp`.",
            "When `curr` becomes `None`, `prev` is sitting at the new head, so `return prev`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Reverse Linked List. "
            "Instead of allocating new nodes or using an O of N recursive call stack, we reverse the arrows in-place using three pointers: prev, curr, and next_temp. "
            "We start with prev equals None and curr equals head. "
            "While curr is not None, we first save next_temp equals curr dot next so we don't lose the rest of the list. "
            "Next, we flip the pointer backward by setting curr dot next equals prev. "
            "Then we slide our pointers forward: prev becomes curr, and curr becomes next_temp. "
            "When the loop ends, prev points to the new head of the reversed list, so we return prev."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We visit each of the N nodes in the linked list exactly once, performing 4 constant-time pointer assignments per node."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "We mutate `.next` pointers in-place using only three pointer variables (`prev`, `curr`, `next_temp`)."
        ),
        "bigo_deep_dive": [
            "Iterative vs Recursive: Both take O(N) time, but iterative takes O(1) space while recursive takes O(N) call stack space.",
            "Single Pass: Each link is reversed in-place as we traverse."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Reverse Linked List. "
            "The Time Complexity is O of N linear time, because we traverse each of the N nodes once and rewire its next pointer in O of 1 time. "
            "The Space Complexity is O of 1 constant memory, since all pointer reversals happen in-place with just three variables."
        )
    },
    "02_Merge_Two_Sorted_Lists.py": {
        "title": "02 Merge Two Sorted Lists",
        "core_understanding": (
            "Use a `dummy` starter node and a `tail` pointer. At each step, compare the front nodes of `list1` and `list2`, "
            "attach the smaller node to `tail.next`, and advance that list's pointer—just like zipping two sorted chains together."
        ),
        "why_most_efficient": (
            "Using a `dummy` head node eliminates messy special-case code for initializing the head of the merged list, "
            "and rewiring the existing nodes in-place avoids allocating any new list nodes (O(1) extra space)."
        ),
        "code_walkthrough": [
            "Create `dummy = ListNode()` as a placeholder anchor and set `tail = dummy`.",
            "Loop `while list1 and list2:` as long as both lists still have nodes to compare.",
            "If `list1.val < list2.val:`, attach `tail.next = list1` and advance `list1 = list1.next`.",
            "Else, attach `tail.next = list2` and advance `list2 = list2.next`.",
            "Advance the merged builder pointer: `tail = tail.next`.",
            "Once one list runs out, attach the entire remaining non-empty list in O(1) via `tail.next = list1 if list1 else list2`, and `return dummy.next`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Merge Two Sorted Lists. "
            "The trick that makes this code clean and bug-free is creating a dummy ListNode and a tail pointer starting at dummy. "
            "While both list1 and list2 have nodes, we compare list1 dot val with list2 dot val. "
            "We point tail dot next to whichever node is smaller, advance that list's pointer, and advance tail to tail dot next. "
            "As soon as one list becomes empty, we don't even need a loop for the leftovers: we simply set tail dot next to list1 if list1 else list2, and return dummy dot next."
        ),
        "time_complexity": "O(N + M)",
        "time_explanation": (
            "Where N and M are the lengths of `list1` and `list2`. Each iteration advances either `list1` or `list2` by one node."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "We reuse the existing `ListNode` objects from both input lists and only allocate a single `dummy` node."
        ),
        "bigo_deep_dive": [
            "Time: At most N + M comparisons.",
            "Space: O(1) auxiliary space (in-place pointer splicing)."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Merge Two Sorted Lists. "
            "The Time Complexity is O of N plus M, where N and M are the node counts of the two lists, because every comparison advances one of the two pointers. "
            "The Space Complexity is O of 1 constant space, since we splice the existing nodes together in-place using only a single dummy node."
        )
    },
    "01_Invert_Binary_Tree.py": {
        "title": "01 Invert Binary Tree",
        "core_understanding": (
            "Inverting a binary tree means swapping the left and right children of every single node in the tree. "
            "Recursively, if we invert the right subtree and invert the left subtree, we just assign them to `root.left` and `root.right`."
        ),
        "why_most_efficient": (
            "Every node's children must be swapped at least once, so O(N) time is the theoretical lower bound. "
            "Python's simultaneous tuple assignment `root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)` "
            "performs the recursive traversal and child swap in a single expressive line."
        ),
        "code_walkthrough": [
            "Base case: `if not root: return None` — an empty subtree is already inverted.",
            "Recursive swap: `root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)`.",
            "Return `root` so the parent call receives the root of this inverted subtree."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Invert Binary Tree. "
            "To mirror a binary tree, every node needs its left and right subtrees swapped. "
            "First, we handle the base case: if not root, return None. "
            "Then, in one Pythonic tuple assignment, we set root dot left comma root dot right equal to self dot invertTree of root dot right comma self dot invertTree of root dot left. "
            "Finally, we return root. This recursively swaps every subtree from top to bottom in optimal linear time."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "We visit each of the N nodes in the binary tree exactly once and swap its two child pointers in O(1) time."
        ),
        "space_complexity": "O(H)",
        "space_explanation": (
            "Where H is the height of the tree. The recursive call stack reaches depth H: O(log N) for a balanced tree, "
            "or O(N) in the worst case of a skewed line-shaped tree."
        ),
        "bigo_deep_dive": [
            "Time: O(N) because every node is visited once.",
            "Call Stack Space: O(H) where H = log₂(N) best case (balanced) and H = N worst case (skewed)."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Invert Binary Tree. "
            "The Time Complexity is O of N linear time, because the recursion visits every node in the tree once and swaps its two pointers in O of 1 time. "
            "The Space Complexity is O of H, where H is the height of the tree, representing the maximum depth of the recursion call stack—which is O of log N for a balanced tree and O of N for a skewed tree."
        )
    },
    "02_Maximum_Depth_of_Binary_Tree.py": {
        "title": "02 Maximum Depth of Binary Tree",
        "core_understanding": (
            "The maximum depth of any binary tree rooted at `root` is simply `1` (for the root itself) plus the larger "
            "of the maximum depths of its `left` and `right` subtrees."
        ),
        "why_most_efficient": (
            "Any algorithm must inspect every node to know which leaf is deepest, making O(N) time optimal. "
            "Depth-First Search (DFS) recursion expresses the divide-and-conquer recurrence `1 + max(left, right)` in just 5 lines of code."
        ),
        "code_walkthrough": [
            "Base case: `if not root: return 0` — an empty tree has a depth of 0.",
            "Recursively compute the left subtree depth: `left_depth = self.maxDepth(root.left)`.",
            "Recursively compute the right subtree depth: `right_depth = self.maxDepth(root.right)`.",
            "Combine: `return 1 + max(left_depth, right_depth)`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Maximum Depth of Binary Tree. "
            "The recursive insight is that the height of any tree is 1 for the current node plus the maximum height between its left and right subtrees. "
            "First, our base case checks if not root, returning 0. "
            "Next, we recursively find left_depth equals self dot maxDepth of root dot left, and right_depth equals self dot maxDepth of root dot right. "
            "Finally, we return 1 plus max of left_depth and right_depth."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "Every node in the tree of size N is visited once, doing a single O(1) `max` and addition operation per node."
        ),
        "space_complexity": "O(H)",
        "space_explanation": (
            "The recursion stack grows to the height H of the tree: O(log N) for a balanced binary tree and O(N) for a skewed tree."
        ),
        "bigo_deep_dive": [
            "Time: O(N) visits across all N tree nodes.",
            "Space: O(H) call frames active on the stack at the deepest leaf."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Maximum Depth of Binary Tree. "
            "The Time Complexity is O of N linear time, because we visit all N nodes exactly once. "
            "The Space Complexity is O of H, where H is the height of the tree, due to the recursive call stack."
        )
    },
    "01_Climbing_Stairs.py": {
        "title": "01 Climbing Stairs",
        "core_understanding": (
            "To reach step `i`, your very last move had to be either a 1-step from `i - 1` or a 2-step from `i - 2`. "
            "Therefore, `ways(i) = ways(i - 1) + ways(i - 2)`—which is the exact Fibonacci sequence!"
        ),
        "why_most_efficient": (
            "Naive recursion recomputes the same steps exponentially in O(2^N) time, and a full DP array uses O(N) memory. "
            "Since step `i` only depends on the previous two steps, we only keep two variables (`one_step_before` and `two_steps_before`), "
            "achieving O(N) time and O(1) constant space!"
        ),
        "code_walkthrough": [
            "Base cases: `if n <= 2: return n` (1 way for 1 step, 2 ways for 2 steps).",
            "Initialize rolling state: `one_step_before = 2` (ways to reach step 2) and `two_steps_before = 1` (ways to reach step 1).",
            "Loop `for i in range(3, n + 1):` from step 3 up to step `n`.",
            "Compute `current = one_step_before + two_steps_before`.",
            "Slide the window forward: `two_steps_before = one_step_before` and `one_step_before = current`.",
            "Return `one_step_before`."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Climbing Stairs. "
            "To reach step i, you either came from step i minus 1 or step i minus 2, so the number of ways is the sum of the previous two steps. "
            "Unmemoized recursion takes exponential 2 to the N time, and a DP array takes O of N space. "
            "Instead, we optimize space to O of 1 by keeping just two variables: one_step_before initialized to 2, and two_steps_before initialized to 1. "
            "We loop i from 3 to n, set current equal to their sum, shift two_steps_before and one_step_before forward, and return one_step_before."
        ),
        "time_complexity": "O(N)",
        "time_explanation": (
            "A single loop runs from 3 to N, performing O(1) addition and variable assignments on each step."
        ),
        "space_complexity": "O(1)",
        "space_explanation": (
            "Instead of an O(N) `dp` table, we only maintain three integer variables (`one_step_before`, `two_steps_before`, `current`)."
        ),
        "bigo_deep_dive": [
            "Evolution of Optimality: O(2^N) Recursion -> O(N) Time & O(N) Space Memoization -> O(N) Time & O(1) Space Rolling Variables.",
            "Memory: Strictly O(1) constant space."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Climbing Stairs. "
            "The Time Complexity is O of N linear time, because our loop runs N minus 2 times with constant-time addition. "
            "The Space Complexity is O of 1 constant space, because we compressed the dynamic programming table down to just two rolling state variables."
        )
    },
    "02_Coin_Change.py": {
        "title": "02 Coin Change",
        "core_understanding": (
            "Build a bottom-up table `dp[x]` representing the minimum coins needed to make amount `x`. "
            "For every coin, if we use that coin to reach amount `x`, the total coins used is `dp[x - coin] + 1`."
        ),
        "why_most_efficient": (
            "Greedy (always picking the largest coin) fails on cases like `coins = [1, 3, 4], amount = 6` (greedy picks 4+1+1=3 coins instead of 3+3=2 coins), "
            "and brute-force recursion is exponential. Bottom-up 1D Dynamic Programming solves each sub-amount from `0` to `amount` once."
        ),
        "code_walkthrough": [
            "Initialize `dp = [float('inf')] * (amount + 1)` and set base case `dp[0] = 0` (0 coins needed to make amount 0).",
            "Outer loop: `for coin in coins:` iterates through each available coin denomination.",
            "Inner loop: `for x in range(coin, amount + 1):` updates all target amounts `x` that can use `coin`.",
            "Transition: `dp[x] = min(dp[x], dp[x - coin] + 1)` chooses the fewer coins between keeping the existing best or using `coin`.",
            "Return `dp[amount] if dp[amount] != float('inf') else -1` in case the amount is impossible to form."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Coin Change. "
            "A greedy approach fails because picking the largest coin first can trap you into using more coins later. "
            "Instead, we use Bottom-Up Dynamic Programming. We create a dp array of size amount plus 1 filled with infinity, and set dp of 0 to 0. "
            "For each coin in coins, and for each sub-amount x from coin up to amount, we update dp of x as the minimum of its current value and dp of x minus coin plus 1. "
            "Finally, if dp of amount is still infinity, we return minus 1; otherwise we return dp of amount."
        ),
        "time_complexity": "O(C · A)",
        "time_explanation": (
            "Where C is the number of coin denominations (`len(coins)`) and A is the target `amount`. "
            "The nested loops perform at most `C * A` constant-time `min` comparisons."
        ),
        "space_complexity": "O(A)",
        "space_explanation": (
            "We allocate a 1D `dp` list of length `amount + 1`."
        ),
        "bigo_deep_dive": [
            "Time: Pseudo-polynomial O(len(coins) × amount).",
            "Space: 1D array of size `amount + 1` rather than a 2D `C × A` table."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Coin Change. "
            "The Time Complexity is O of C times A, where C is the number of coins and A is the target amount, because for each coin we iterate up to the target amount. "
            "The Space Complexity is O of A, as we allocate a 1D dynamic programming array of size amount plus 1."
        )
    },
    "01_Number_of_Islands.py": {
        "title": "01 Number of Islands",
        "core_understanding": (
            "Scan every cell in the grid. Whenever we discover an unvisited land cell `'1'`, we increment our `island_count` by 1 "
            "and immediately launch a Depth-First Search (DFS) flood-fill to sink (`'0'`) all connected land cells belonging to that same island."
        ),
        "why_most_efficient": (
            "By mutating visited `'1'` cells directly to `'0'` in-place during DFS, we avoid allocating an extra O(M × N) `visited` set "
            "and guarantee that no land cell is ever counted as a new island twice."
        ),
        "code_walkthrough": [
            "Guard against empty grid, then store `rows, cols = len(grid), len(grid[0])` and `island_count = 0`.",
            "Define helper `dfs(r, c)` which returns immediately if `(r, c)` is out of bounds or `grid[r][c] != '1'`.",
            "Inside `dfs`, mark the current land cell as visited by sinking it: `grid[r][c] = '0'`.",
            "Recursively call `dfs` in all 4 cardinal directions (`r + 1`, `r - 1`, `c + 1`, `c - 1`).",
            "In the nested grid loops, whenever `grid[r][c] == '1'`, increment `island_count += 1` and call `dfs(r, c)` to sink the whole island."
        ],
        "walkthrough_audio_text": (
            "Let's walk through Number of Islands. "
            "The core idea is flood-fill using Depth-First Search. As we scan every row and column of the grid, whenever we hit a 1, we know we've discovered a brand new island! "
            "Why is sinking the island in-place so efficient? By setting grid of r and c to 0 inside our DFS, we erase the connected land cells as we visit them, so we never count the same island twice and don't need a separate visited set. "
            "In the code, our dfs helper checks bounds and returns if grid of r and c is not 1. Then it sets grid of r and c to 0 and calls dfs on all four neighbors: down, up, right, and left."
        ),
        "time_complexity": "O(M · N)",
        "time_explanation": (
            "Where M is the number of rows and N is the number of columns. Each cell is visited a constant number of times "
            "(once by the outer grid scan, and at most once by DFS before being flipped to `'0'`)."
        ),
        "space_complexity": "O(M · N)",
        "space_explanation": (
            "In the worst case where the entire grid is land (`'1'`), the DFS recursion stack can grow up to `M * N` frames deep."
        ),
        "bigo_deep_dive": [
            "Amortized Cell Visits: Even though DFS is called inside a double loop, flipping `'1'` to `'0'` ensures DFS never re-expands an already-sunk cell.",
            "Space: Zero extra `visited` matrix needed; O(M · N) worst-case recursion stack."
        ],
        "bigo_audio_text": (
            "Big O Runtime and Memory analysis for Number of Islands. "
            "The Time Complexity is O of M times N, where M is rows and N is columns. Even though we call DFS inside nested loops, each land cell is flipped from 1 to 0 the first time DFS visits it, so every cell is processed in constant amortized time. "
            "The Space Complexity is O of M times N in the worst case for the recursive call stack if the entire grid is one giant landmass."
        )
    }
}

