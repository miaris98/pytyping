"""
NeetCode 150 Solutions Generator - Part 2 (Categories 10 to 18: 80 problems)
Includes Company tags, Time/Space Big O, Core Intuition, Why Efficient, and Optimal Python 3 Code.
"""

PART2_PROBLEMS = {
    "10_Backtracking": [
        (
            "01_Subsets.py",
            "LeetCode 78: Subsets",
            "Meta, Amazon, Google, Bloomberg, Microsoft, Apple",
            "O(N * 2^N) - Generates all 2^N subsets, copying up to N elements per subset.",
            "O(N) - Recursion stack depth and current `subset` path.",
            "At every index `i`, make a binary decision: either include `nums[i]` in the current subset or skip `nums[i]`.",
            "Explores the binary decision tree directly without generating duplicate subsets.",
            """from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res"""
        ),
        (
            "02_Combination_Sum.py",
            "LeetCode 39: Combination Sum",
            "Amazon, Meta, AirBnB, Google, Microsoft, Apple, Bloomberg",
            "O(2^(T/M)) - Branches up to target T divided by minimum candidate M.",
            "O(T/M) - Maximum recursion stack depth.",
            "At index `i`, branch into: 1) include `candidates[i]` and stay at `i` (allowing unlimited reuse), or 2) skip `candidates[i]` and move to `i + 1` (preventing duplicate permutations).",
            "Advancing the index `i` only on the skip branch guarantees unique combinations without needing a set to deduplicate.",
            """from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i: int, total: int):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, total + candidates[i])
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res"""
        ),
        (
            "03_Permutations.py",
            "LeetCode 46: Permutations",
            "Amazon, LinkedIn, Microsoft, Meta, Google, Apple",
            "O(N * N!) - Generates N! permutations of length N.",
            "O(N) - In-place swapping along the recursion stack of depth N.",
            "Fix each element at index `idx` by swapping `nums[idx]` with every candidate `nums[i]` from `idx` to `n - 1`, recurse on `idx + 1`, then swap back.",
            "In-place swapping avoids allocating boolean `used` arrays or slicing new lists at every recursive step.",
            """from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx: int):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return res"""
        ),
        (
            "04_Subsets_II.py",
            "LeetCode 90: Subsets II",
            "Amazon, Meta, Bloomberg, Google, Yahoo",
            "O(N * 2^N) - Sorting plus exploring unique subset branches.",
            "O(N) - Recursion stack depth.",
            "Sort `nums` first so duplicate numbers are adjacent. When we decide to skip `nums[i]`, advance `i` past all identical copies of `nums[i]` so we never start a duplicate branch.",
            "Sorting and skipping adjacent duplicates in the exclude branch avoids O(2^N) set hashing overhead.",
            """from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []

        def backtrack(i: int):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res"""
        ),
        (
            "05_Combination_Sum_II.py",
            "LeetCode 40: Combination Sum II",
            "Amazon, TikTok, Airbnb, Meta, Google, Microsoft",
            "O(2^N) - Backtracking with duplicate and sum pruning.",
            "O(N) - Recursion stack depth.",
            "Sort `candidates`, prune immediately when `candidates[i] > remain`, and skip duplicate siblings (`if i > start and candidates[i] == candidates[i - 1]: continue`).",
            "Sorting enables both duplicate skipping and early break pruning when the current number exceeds the remaining sum.",
            """from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def backtrack(start: int, remain: int):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return res"""
        ),
        (
            "06_Word_Search.py",
            "LeetCode 79: Word Search",
            "Amazon, Bloomberg, Karat, Uber, Microsoft, Meta, Snap",
            "O(M * N * 4 * 3^(L-1)) - DFS from each grid cell up to word length L.",
            "O(L) - Recursion stack of depth L; marks visited cells in-place on `board`.",
            "From each cell matching `word[0]`, run 4-directional DFS. Temporarily overwrite `board[r][c] = '#'` to mark it visited on the current path, then restore it on backtrack.",
            "In-place `#` marking avoids allocating a `visited` set and checks visited status in O(1) array indexing.",
            """from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = tmp
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))"""
        ),
        (
            "07_Palindrome_Partitioning.py",
            "LeetCode 131: Palindrome Partitioning",
            "Google, Amazon, Meta, Apple, Adobe, TikTok",
            "O(N * 2^N) - Explores partitioning cuts and verifies palindrome substrings.",
            "O(N) - Recursion stack and current partition list.",
            "Try every prefix `s[i:j+1]` starting at `i`. If that prefix is a palindrome (`sub == sub[::-1]`), add it to `part` and recursively partition the suffix starting at `j + 1`.",
            "Prunes non-palindrome prefixes immediately without exploring their suffixes.",
            """from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i: int):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    part.append(sub)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res"""
        ),
        (
            "08_Letter_Combinations_of_a_Phone_Number.py",
            "LeetCode 17: Letter Combinations of a Phone Number",
            "Amazon, Meta, Microsoft, Google, Apple, Uber, Epic Systems",
            "O(N * 4^N) - At most 4 letters per digit across N digits.",
            "O(N) - Recursion depth of length N.",
            "Map each digit `'2'..'9'` to its keypad letters and backtrack character by character from index `0` to `len(digits)`.",
            "Cleanly builds combinations of exact length N in a single depth-first traversal.",
            """from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res, path = [], []

        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res"""
        ),
        (
            "09_N_Queens.py",
            "LeetCode 51: N-Queens",
            "Amazon, Meta, Google, Microsoft, Apple, Bloomberg",
            "O(N!) - Places one queen per row while pruning occupied columns and diagonals.",
            "O(N²) - Board state and 3 constraint sets (`cols`, `pos_diag`, `neg_diag`).",
            "Place one queen per row `r`. All cells on the same positive diagonal share `r + c`, and all cells on the same negative diagonal share `r - c`—allowing O(1) conflict checks with three Sets!",
            "Checking board diagonals by scanning takes O(N) per cell; tracking `r + c` and `r - c` in sets makes conflict checks O(1).",
            """from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_diag, neg_diag = set(), set(), set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res"""
        ),
    ],
    "11_Graphs": [
        (
            "01_Number_of_Islands.py",
            "LeetCode 200: Number of Islands",
            "Amazon, Bloomberg, Meta, Google, Microsoft, Uber, Apple",
            "O(M * N) - Visits each grid cell a constant number of times.",
            "O(M * N) - Worst-case recursion stack depth when grid is all land.",
            "Scan the grid; whenever `'1'` is found, increment `islands` and run DFS flood-fill to sink connected `'1'`s to `'0'`.",
            "Sinking visited land cells to `'0'` in-place avoids allocating an O(M * N) `visited` set.",
            """from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands"""
        ),
        (
            "02_Max_Area_of_Island.py",
            "LeetCode 695: Max Area of Island",
            "Amazon, Meta, Google, DoorDash, Bloomberg, Microsoft",
            "O(M * N) - Each cell is visited at most once by DFS.",
            "O(M * N) - Recursion stack depth in the worst case.",
            "Run DFS on each unvisited land cell `'1'`, sinking it to `0` and summing `1 + area_of_4_neighbors`.",
            "In-place sinking (`grid[r][c] = 0`) counts each island's area in O(M * N) total time without extra visited storage.",
            """from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)"""
        ),
        (
            "03_Clone_Graph.py",
            "LeetCode 133: Clone Graph",
            "Meta, Amazon, Google, Bloomberg, Microsoft, Pinterest",
            "O(V + E) - Visits every vertex V and edge E once.",
            "O(V) - Hash map `old_to_new` stores cloned nodes and prevents infinite cycles.",
            "Use a hash map `old_to_new` during DFS: if `node` is already cloned, return `old_to_new[node]`; otherwise create its clone, register it in the map, and recursively clone its neighbors.",
            "Registering the clone in `old_to_new` BEFORE recursing on neighbors breaks undirected graph cycles immediately.",
            """class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in old_to_new:
                return old_to_new[curr]
            copy = Node(curr.val)
            old_to_new[curr] = copy
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)"""
        ),
        (
            "04_Walls_and_Gates.py",
            "LeetCode 286: Walls and Gates",
            "Meta, Amazon, DoorDash, Google, Uber, Microsoft",
            "O(M * N) - Multi-source BFS visits each empty room once.",
            "O(M * N) - Queue holds at most M * N coordinates.",
            "Enqueue ALL gates (`0`) simultaneously into a BFS queue, then expand outward level-by-level into unvisited empty rooms (`INF = 2147483647`).",
            "Running separate BFS from every empty room takes O((M*N)²). Multi-source BFS from all gates at once guarantees the first time a room is reached is its shortest distance in O(M * N) time!",
            """from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        q = deque([(r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0])
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))"""
        ),
        (
            "05_Rotting_Oranges.py",
            "LeetCode 994: Rotting Oranges",
            "Amazon, Microsoft, Meta, Google, TikTok, Bloomberg, Uber",
            "O(M * N) - Multi-source BFS across the grid.",
            "O(M * N) - BFS queue of rotten orange coordinates.",
            "Count `fresh` oranges and push all initially rotten oranges (`2`) into a queue. Expand level-by-level (1 minute per BFS level), decrementing `fresh` as neighbors rot.",
            "Multi-source BFS simulates simultaneous rot spreading from multiple sources in a single O(M * N) pass.",
            """from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1"""
        ),
        (
            "06_Pacific_Atlantic_Water_Flow.py",
            "LeetCode 417: Pacific Atlantic Water Flow",
            "Google, Amazon, Meta, Microsoft, Bloomberg, Uber",
            "O(M * N) - Two ocean-inward DFS traversals visit each cell at most twice.",
            "O(M * N) - Two reachability sets (`pac` and `atl`) plus recursion stack.",
            "Instead of flowing downhill from every cell, start at the Pacific border and Atlantic border and walk UPHILL (`height >= prev_height`) to find all cells reachable from each ocean, then return `pac & atl`.",
            "Reversing the flow from borders inward reduces O((M*N)²) per-cell searches to just two O(M * N) traversals.",
            """from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visit: set, prev_h: int):
            if (
                (r, c) in visit
                or r < 0 or r >= rows or c < 0 or c >= cols
                or heights[r][c] < prev_h
            ):
                return
            visit.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        return [[r, c] for r, c in pac & atl]"""
        ),
        (
            "07_Surrounded_Regions.py",
            "LeetCode 130: Surrounded Regions",
            "Amazon, Google, Meta, TikTok, Bloomberg",
            "O(M * N) - Border DFS plus single grid sweep.",
            "O(M * N) - Worst-case recursion stack.",
            "Any `'O'` region connected to the border can NEVER be surrounded. Run DFS from all border `'O'` cells to mark them `'T'` (safe), flip remaining interior `'O'`s to `'X'`, and restore `'T'`s back to `'O'`.",
            "In-place `'T'` marking distinguishes border-connected `'O'`s from captured interior `'O'`s without an extra visited matrix.",
            """from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O" """
        ),
        (
            "08_Course_Schedule.py",
            "LeetCode 207: Course Schedule",
            "Amazon, Meta, Google, Microsoft, TikTok, Palantir, Uber",
            "O(V + E) - Visits each course V and prerequisite edge E once.",
            "O(V + E) - Adjacency list and cycle-detection state.",
            "Model courses as a directed graph and run DFS cycle detection. Clear `pre_map[crs] = []` once a course is verified cycle-free so it is never re-checked.",
            "Memoizing verified courses by emptying `pre_map[crs] = []` prevents redundant traversals, running in O(V + E) linear graph time.",
            """from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visiting = set()

        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            if not pre_map[crs]:
                return True
            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []
            return True

        return all(dfs(c) for c in range(numCourses))"""
        ),
        (
            "09_Course_Schedule_II.py",
            "LeetCode 210: Course Schedule II",
            "Amazon, Google, Meta, Microsoft, Robinhood, TikTok, DoorDash",
            "O(V + E) - Postorder topological sort visits each vertex and edge once.",
            "O(V + E) - Adjacency list plus `visited` and `cycle` sets.",
            "Run Postorder DFS: a course can only be appended to the topological order AFTER all of its prerequisites have been appended. Detect cycles via a `cycle` active-path set.",
            "Produces a valid topological ordering and detects cycles in a single O(V + E) DFS pass.",
            """from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit, cycle = set(), set()

        def dfs(crs: int) -> bool:
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output"""
        ),
        (
            "10_Graph_Valid_Tree.py",
            "LeetCode 261: Graph Valid Tree",
            "LinkedIn, Amazon, Google, Meta, Microsoft",
            "O(V + E) - Union-Find with path compression and rank.",
            "O(V) - Parent array for N nodes.",
            "An undirected graph of `n` nodes is a valid tree iff it has exactly `n - 1` edges and contains no cycles (so all `n - 1` edges unite two previously disconnected components).",
            "Checking `len(edges) == n - 1` plus Union-Find cycle detection validates both connectivity and acyclicity in nearly O(N) time.",
            """from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True"""
        ),
        (
            "11_Number_of_Connected_Components_in_an_Undirected_Graph.py",
            "LeetCode 323: Number of Connected Components in an Undirected Graph",
            "Amazon, LinkedIn, Google, Meta, Microsoft, Pinterest",
            "O(V + E * alpha(V)) - Union-Find with path compression and union by rank.",
            "O(V) - `parent` and `rank` arrays of size `n`.",
            "Start with `n` isolated components. For every edge `(a, b)`, if `find(a) != find(b)`, union their roots and decrement the component count by 1.",
            "Union-Find with path compression processes edges in near-constant O(alpha(N)) time without building adjacency lists.",
            """from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        res = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                if rank[ra] < rank[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                rank[ra] += rank[rb]
                res -= 1
        return res"""
        ),
        (
            "12_Redundant_Connection.py",
            "LeetCode 684: Redundant Connection",
            "Amazon, Google, Apple, Microsoft, Meta",
            "O(N * alpha(N)) - Single pass over N edges with Union-Find.",
            "O(N) - Disjoint set `parent` and `rank` arrays.",
            "Process edges in order using Union-Find. The first edge `(u, v)` whose endpoints already share the same root (`find(u) == find(v)`) closes a cycle and is the redundant edge!",
            "Repeatedly running DFS for each edge takes O(N²). Union-Find detects the cycle-closing edge in near-linear O(N) time.",
            """from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]
            parent[ru] = rv
        return []"""
        ),
        (
            "13_Word_Ladder.py",
            "LeetCode 127: Word Ladder",
            "Amazon, Meta, LinkedIn, Google, Microsoft, Uber, Box",
            "O(N * M²) - N words of length M indexed by wildcard patterns.",
            "O(N * M²) - Pattern adjacency dictionary `{*ot: [hot, dot, lot]}`.",
            "Group words by wildcard patterns (e.g. `h*t`, `*ot`, `ho*`), then run unweighted BFS from `beginWord` to find the shortest transformation sequence to `endWord`.",
            "Comparing all pairs of N words takes O(N² * M). Grouping by M wildcard patterns reduces neighbor lookup to O(M²) per word!",
            """from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                nei[word[:j] + "*" + word[j + 1 :]].append(word)
        visit = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for next_word in nei[pattern]:
                    if next_word not in visit:
                        visit.add(next_word)
                        q.append((next_word, steps + 1))
                nei[pattern].clear()
        return 0"""
        ),
    ],
    "12_Advanced_Graphs": [
        (
            "01_Reconstruct_Itinerary.py",
            "LeetCode 332: Reconstruct Itinerary",
            "Uber, Netflix, Google, Meta, Amazon, Bloomberg",
            "O(E log E) - Sorting tickets plus O(E) Hierholzer's Eulerian path traversal.",
            "O(V + E) - Adjacency list and recursion stack.",
            "Sort tickets in reverse lexical order so `adj[src].pop()` always picks the smallest lexical destination in O(1). Use Hierholzer's postorder DFS to build the Eulerian path in reverse.",
            "Backtracking with edge removals/insertions takes exponential time on dead ends; Hierholzer's postorder DFS visits every ticket edge exactly once in O(E) time!",
            """from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        res = []

        def dfs(src: str):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)

        dfs("JFK")
        return res[::-1]"""
        ),
        (
            "02_Min_Cost_to_Connect_All_Points.py",
            "LeetCode 1584: Min Cost to Connect All Points",
            "Amazon, Microsoft, Meta, Directi",
            "O(N² log N) - Prim's Minimum Spanning Tree algorithm across N points.",
            "O(N²) - Min-heap and visited set.",
            "Run Prim's Minimum Spanning Tree (MST) algorithm starting from point `0`: greedily pop the cheapest edge `(cost, u)` to an unvisited point until all N points are connected.",
            "Connects all N points with minimum Manhattan distance without building and sorting all N(N-1)/2 edges upfront.",
            """from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        min_heap = [(0, 0)]
        total_cost = 0
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            visit.add(i)
            total_cost += cost
            x1, y1 = points[i]
            for j in range(n):
                if j not in visit:
                    x2, y2 = points[j]
                    heapq.heappush(min_heap, (abs(x1 - x2) + abs(y1 - y2), j))
        return total_cost"""
        ),
        (
            "03_Network_Delay_Time.py",
            "LeetCode 743: Network Delay Time",
            "Amazon, Google, Akuna Capital, Uber, Microsoft",
            "O(E log V) - Dijkstra's shortest-path algorithm with a min-heap.",
            "O(V + E) - Adjacency list, `visit` set, and priority queue.",
            "Use Dijkstra's algorithm with a Min-Heap `(accumulated_time, node)` from source `k`. The time when the last unvisited node is popped is the total network delay.",
            "Dijkstra's min-heap guarantees the first time each node is popped is its true shortest path from `k`.",
            """from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        visit = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        return t if len(visit) == n else -1"""
        ),
        (
            "04_Swim_in_Rising_Water.py",
            "LeetCode 778: Swim in Rising Water",
            "Google, Amazon, Meta, DoorDash, Uber",
            "O(N² log N) - Modified Dijkstra minimizing the maximum elevation along the path.",
            "O(N²) - Min-heap and `visit` set.",
            "Run Dijkstra where the cost of stepping onto `(nr, nc)` is `max(current_max_height, grid[nr][nc])`. Always expand the frontier cell with the lowest bottleneck elevation.",
            "Finds the minimax bottleneck path directly in O(N² log N) time.",
            """from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = {(0, 0)}
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
        return -1"""
        ),
        (
            "05_Alien_Dictionary.py",
            "LeetCode 269: Alien Dictionary",
            "Airbnb, Meta, Google, Amazon, Uber, Pinterest, Microsoft",
            "O(C) - Total characters C across all words to build graph and topologically sort.",
            "O(U) - At most 26 unique letters in adjacency sets.",
            "Compare adjacent words `w1, w2` to find the first differing character `w1[j] -> w2[j]`, then run topological sort (with cycle and invalid-prefix detection).",
            "Only adjacent word pairs are needed because transitivity covers all non-adjacent pairs, building the graph in linear O(C) time.",
            """from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {ch: set() for w in words for ch in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []

        def dfs(ch: str) -> bool:
            if ch in visit:
                return visit[ch]
            visit[ch] = True
            for nei in adj[ch]:
                if dfs(nei):
                    return True
            visit[ch] = False
            res.append(ch)
            return False

        for ch in adj:
            if dfs(ch):
                return ""
        return "".join(reversed(res))"""
        ),
        (
            "06_Cheapest_Flights_Within_K_Stops.py",
            "LeetCode 787: Cheapest Flights Within K Stops",
            "Amazon, Airbnb, Google, Uber, Bloomberg, Meta",
            "O(K * E) - Bellman-Ford relaxation over `k + 1` rounds across E flights.",
            "O(N) - Two price arrays of length `n`.",
            "Run `k + 1` iterations of Bellman-Ford edge relaxation using a `tmp_prices` copy so each round only extends paths by at most 1 flight edge.",
            "Standard Dijkstra can discard a more expensive path that uses fewer stops. Bellman-Ford with `k + 1` rounds strictly enforces the stop limit in O(K * E) time.",
            """from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, w in flights:
                if prices[u] != float("inf") and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp
        return prices[dst] if prices[dst] != float("inf") else -1"""
        ),
    ],
    "13_1D_Dynamic_Programming": [
        (
            "01_Climbing_Stairs.py",
            "LeetCode 70: Climbing Stairs",
            "Amazon, Google, Adobe, Apple, Microsoft, Meta, Bloomberg",
            "O(N) - Single loop from 3 to N.",
            "O(1) - Rolling Fibonacci state variables.",
            "Ways to reach step `i` is `ways(i - 1) + ways(i - 2)`. Track only the last two values.",
            "Collapses O(2^N) recursion and O(N) DP array space down to O(N) time and O(1) space.",
            """class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 2, 1
        for _ in range(3, n + 1):
            one, two = one + two, one
        return one"""
        ),
        (
            "02_Min_Cost_Climbing_Stairs.py",
            "LeetCode 746: Min Cost Climbing Stairs",
            "Amazon, Bloomberg, Google, Microsoft, Apple",
            "O(N) - Single backward/forward pass over N steps.",
            "O(1) - Two rolling cost variables `down_one` and `down_two`.",
            "At each step `i`, the minimum cost to reach it is `min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`.",
            "Computes the optimal cost in O(N) time using O(1) space without mutating the input array.",
            """from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
        return min(prev1, prev2)"""
        ),
        (
            "03_House_Robber.py",
            "LeetCode 198: House Robber",
            "Amazon, Cisco, Google, Apple, Microsoft, Meta",
            "O(N) - Single pass over N houses.",
            "O(1) - Tracks only `rob1` (two houses back) and `rob2` (one house back).",
            "At each house `n`, decide between robbing it (`n + rob1`) or skipping it (`rob2`): `new_max = max(n + rob1, rob2)`.",
            "Reduces O(2^N) branching and O(N) DP table space to two rolling integers in O(1) space.",
            """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2"""
        ),
        (
            "04_House_Robber_II.py",
            "LeetCode 213: House Robber II",
            "Google, Amazon, Microsoft, TikTok, eBay",
            "O(N) - Two linear passes of standard House Robber.",
            "O(1) - Rolling variables in helper.",
            "Since the first and last houses are adjacent in a circle, you cannot rob both. Run linear House Robber twice: once excluding the first house `nums[1:]` and once excluding the last `nums[:-1]`.",
            "Decomposes a circular DP constraint into two simple linear O(N) passes with O(1) space.",
            """from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob_linear(nums[1:]), self._rob_linear(nums[:-1]))

    def _rob_linear(self, arr: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in arr:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2"""
        ),
        (
            "05_Longest_Palindromic_Substring.py",
            "LeetCode 5: Longest Palindromic Substring",
            "Amazon, Microsoft, Cisco, Google, Meta, Adobe, Bloomberg, Apple",
            "O(N²) - Expands around 2N - 1 possible centers.",
            "O(1) - Tracks only best `(start, end)` indices during expansion.",
            "Every palindrome mirrors around its center (either a single character for odd length or between two characters for even length). Expand outward from all `2N - 1` centers.",
            "Checking all substrings takes O(N³), and 2D DP uses O(N²) space. Expanding around centers achieves O(N²) time in O(1) extra space.",
            """class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def expand(l: int, r: int):
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start : start + max_len]"""
        ),
        (
            "06_Palindromic_Substrings.py",
            "LeetCode 647: Palindromic Substrings",
            "Meta, Amazon, Google, Goldman Sachs, Microsoft",
            "O(N²) - Expands around each odd and even center.",
            "O(1) - Constant space counters.",
            "Expand outward `(l -= 1, r += 1)` from every odd center `(i, i)` and even center `(i, i + 1)`, incrementing `count` for every matching pair.",
            "Counts all palindromes in O(N²) time and O(1) space without a 2D boolean table.",
            """class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count"""
        ),
        (
            "07_Decode_Ways.py",
            "LeetCode 91: Decode Ways",
            "Amazon, Cisco, Google, Meta, TikTok, Uber, Lyft",
            "O(N) - Single backward DP pass.",
            "O(1) - Two rolling variables `dp1` and `dp2`.",
            "At index `i`, if `s[i] != '0'`, we can decode 1 digit (`dp1` ways), plus if `10 <= int(s[i:i+2]) <= 26`, we can also decode 2 digits (`dp2` ways).",
            "Processes 1-digit and 2-digit transitions in O(N) time and O(1) space.",
            """class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            cur = 0 if s[i] == "0" else dp1
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += dp2
            dp1, dp2 = cur, dp1
        return dp1"""
        ),
        (
            "08_Coin_Change.py",
            "LeetCode 322: Coin Change",
            "Amazon, Bloomberg, Microsoft, Google, Meta, Apple, Visa",
            "O(C * A) - C coins times target amount A.",
            "O(A) - 1D DP array of size `amount + 1`.",
            "Build `dp[x]` = fewest coins to make amount `x` via `dp[x] = min(dp[x], dp[x - coin] + 1)`.",
            "Bottom-up 1D DP avoids exponential recursion and solves unbounded knapsack in O(C * A) time.",
            """from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1"""
        ),
        (
            "09_Maximum_Product_Subarray.py",
            "LeetCode 152: Maximum Product Subarray",
            "LinkedIn, Amazon, Google, Microsoft, Meta, InfoSys",
            "O(N) - Single pass tracking both running max and running min.",
            "O(1) - Only scalar variables `cur_max`, `cur_min`, and `res`.",
            "Because multiplying two negative numbers produces a huge positive product, track both `cur_max` and `cur_min` at every element.",
            "Solves sign-flipping subarray products in one O(N) pass and O(1) memory.",
            """from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_min = cur_max = nums[0]
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            res = max(res, cur_max)
        return res"""
        ),
        (
            "10_Word_Break.py",
            "LeetCode 139: Word Break",
            "Amazon, Meta, Google, Bloomberg, Apple, Qualtrics, Walmart",
            "O(N * W * L) - For each index i, checks dictionary words of length L.",
            "O(N) - Boolean DP array of length `len(s) + 1`.",
            "Work backward: `dp[i]` is True if some `w` in `wordDict` matches `s[i : i + len(w)]` and the remaining suffix `dp[i + len(w)]` is also True.",
            "Bottom-up DP eliminates exponential backtracking over overlapping suffix splits.",
            """from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]"""
        ),
        (
            "11_Longest_Increasing_Subsequence.py",
            "LeetCode 300: Longest Increasing Subsequence",
            "Google, Amazon, TikTok, Microsoft, Meta, Oracle",
            "O(N log N) - Patience sorting with binary search (`bisect_left`).",
            "O(N) - `tails` array storing the smallest tail of all increasing subsequences of each length.",
            "Maintain a sorted `tails` list where `tails[k]` is the smallest ending value of an increasing subsequence of length `k + 1`. Use binary search (`bisect_left`) to replace or append each number.",
            "Standard DP takes O(N²) time. Binary searching the `tails` array reduces runtime to O(N log N)!",
            """from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)"""
        ),
        (
            "12_Partition_Equal_Subset_Sum.py",
            "LeetCode 416: Partition Equal Subset Sum",
            "Amazon, Meta, Google, Microsoft, Apple, Expedia",
            "O(N * S) - N elements times half-sum S.",
            "O(S) - Hash set / 1D boolean state of reachable subset sums up to `sum(nums) // 2`.",
            "If `sum(nums)` is odd, return False; otherwise check if any subset sums to `target = sum(nums) // 2` using 0/1 Knapsack DP.",
            "Uses a single 1D set of reachable sums (early-exiting as soon as `target` is formed) instead of an O(N * S) 2D table.",
            """from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp |= {t + n for t in dp if t + n <= target}
            if target in dp:
                return True
        return target in dp"""
        ),
    ],
    "14_2D_Dynamic_Programming": [
        (
            "01_Unique_Paths.py",
            "LeetCode 62: Unique Paths",
            "Amazon, Google, Meta, Microsoft, Cisco, Bloomberg",
            "O(M * N) - Computes each grid cell once.",
            "O(N) - Single 1D row array updated in-place.",
            "Paths to `(r, c)` equal `paths(r-1, c) + paths(r, c-1)`. Maintain a single row `row[c] += row[c - 1]`.",
            "Compresses the 2D `M × N` DP table into a single 1D row of length N.",
            """class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[-1]"""
        ),
        (
            "02_Longest_Common_Subsequence.py",
            "LeetCode 1143: Longest Common Subsequence",
            "Amazon, DoorDash, Google, Microsoft, Karat, Bloomberg",
            "O(M * N) - Nested loop over characters of `text1` and `text2`.",
            "O(N) - 1D row DP array of size `len(text2) + 1`.",
            "If `text1[i] == text2[j]`, `dp[i][j] = 1 + dp[i+1][j+1]`; otherwise `max(dp[i+1][j], dp[i][j+1])`.",
            "Bottom-up DP avoids exponential recursion and solves LCS in O(M * N) time.",
            """class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            prev_diag = 0
            for j in range(len(text2) - 1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev_diag = tmp
        return dp[0]"""
        ),
        (
            "03_Best_Time_to_Buy_and_Sell_Stock_With_Cooldown.py",
            "LeetCode 309: Best Time to Buy and Sell Stock with Cooldown",
            "Amazon, Google, Adobe, Citadel",
            "O(N) - Single pass tracking state machine transitions.",
            "O(1) - Three state variables: `held`, `sold`, and `reset`.",
            "Model the 3 states on each day: `held` (holding stock), `sold` (just sold today, entering cooldown), and `reset` (ready to buy).",
            "State-machine DP uses O(N) time and O(1) space instead of an O(N) recursion cache.",
            """from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float("-inf"), float("-inf"), 0
        for p in prices:
            pre_sold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, pre_sold)
        return max(sold, reset)"""
        ),
        (
            "04_Coin_Change_II.py",
            "LeetCode 518: Coin Change II",
            "Amazon, Bloomberg, Google, Morgan Stanley, Uber",
            "O(C * A) - Outer loop over coins, inner loop up to `amount`.",
            "O(A) - 1D DP array `dp[0..amount]`.",
            "Loop over `coin` in the OUTER loop and `x` in the INNER loop (`dp[x] += dp[x - coin]`) so each coin is used in canonical order, counting combinations instead of permutations.",
            "1D array reduces memory from O(C * A) to O(A).",
            """from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]"""
        ),
        (
            "05_Target_Sum.py",
            "LeetCode 494: Target Sum",
            "Meta, Amazon, Google, Adobe",
            "O(N * S) - Subset sum DP up to `(total + target) // 2`.",
            "O(S) - 1D DP array of size `P + 1`.",
            "Splitting numbers into positive `P` and negative `N` means `P - N = target` and `P + N = total`, so `P = (total + target) // 2`—reducing the problem to 0/1 Subset Sum count!",
            "Algebraic reduction to 0/1 Knapsack avoids negative index offsets and cuts the state space in half.",
            """from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        pos_sum = (total + target) // 2
        dp = [0] * (pos_sum + 1)
        dp[0] = 1
        for n in nums:
            for s in range(pos_sum, n - 1, -1):
                dp[s] += dp[s - n]
        return dp[pos_sum]"""
        ),
        (
            "06_Interleaving_String.py",
            "LeetCode 97: Interleaving String",
            "Amazon, Apple, Google, Microsoft, Bloomberg",
            "O(M * N) - Evaluates each `(i, j)` prefix pair once.",
            "O(N) - 1D boolean DP row.",
            "`dp[i][j]` is True if `s3[i+j:]` can be formed by interleaving `s1[i:]` (matching `s1[i] == s3[i+j]`) or `s2[j:]` (matching `s2[j] == s3[i+j]`).",
            "Collapses exponential branching into O(M * N) time and O(N) space.",
            """class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[j]:
                    dp[j] = True
                elif j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
                elif not (i == len(s1) and j == len(s2)):
                    dp[j] = False
        return dp[0]"""
        ),
        (
            "07_Longest_Increasing_Path_in_a_Matrix.py",
            "LeetCode 329: Longest Increasing Path in a Matrix",
            "Google, DoorDash, Amazon, Meta, TikTok, Apple",
            "O(M * N) - Memoized DFS computes each cell's longest path once.",
            "O(M * N) - 2D memoization dictionary `dp[(r, c)]`.",
            "Because paths must be strictly increasing, the graph is a DAG (no cycles can exist!). Run DFS with memoization `dp[(r, c)]` from every cell.",
            "Memoizing `dp[(r, c)]` ensures every cell's 4 neighbors are explored only once across the entire run, achieving O(M * N) linear time.",
            """from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            val = matrix[r][c]
            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, val),
                dfs(r - 1, c, val),
                dfs(r, c + 1, val),
                dfs(r, c - 1, val),
            )
            return dp[(r, c)]

        return max(dfs(r, c, -1) for r in range(rows) for c in range(cols))"""
        ),
        (
            "08_Distinct_Subsequences.py",
            "LeetCode 115: Distinct Subsequences",
            "Google, Amazon, Bloomberg, Citadel, Apple",
            "O(M * N) - Bottom-up DP over lengths of `s` and `t`.",
            "O(N) - 1D DP array of length `len(t) + 1`.",
            "When `s[i] == t[j]`, we can either match them (`dp[j + 1]`) or skip `s[i]` (`dp[j]`), so `dp[j] += dp[j + 1]`.",
            "1D reverse-order update computes the exact count in O(M * N) time and O(N) memory.",
            """class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]"""
        ),
        (
            "09_Edit_Distance.py",
            "LeetCode 72: Edit Distance",
            "Amazon, Google, LinkedIn, Rubrik, Microsoft, Goldman Sachs",
            "O(M * N) - Levenshtein DP over both strings.",
            "O(M * N) - 2D DP table storing minimum operations for each suffix pair.",
            "If `word1[i] == word2[j]`, cost is `dp[i+1][j+1]`; otherwise `1 + min(insert, delete, replace)` = `1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])`.",
            "Bottom-up tabulation computes the minimum Levenshtein distance in O(M * N) polynomial time.",
            """class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]"""
        ),
        (
            "10_Burst_Balloons.py",
            "LeetCode 312: Burst Balloons",
            "Amazon, Google, Samsung, Adobe, C3 IoT",
            "O(N³) - Interval DP over subarray lengths and last-burst pivot `i`.",
            "O(N²) - 2D interval DP table `dp[l][r]`.",
            "Think in reverse: instead of choosing which balloon to burst FIRST (which makes non-adjacent balloons become adjacent), choose which balloon `i` in `(l, r)` is burst LAST—so its neighbors are guaranteed to be `nums[l-1]` and `nums[r+1]`!",
            "Choosing the LAST balloon to burst makes the left and right sub-intervals `[l, i-1]` and `[i+1, r]` completely independent, reducing O(N!) to O(N³) interval DP.",
            """from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n - 1):
            for l in range(1, n - length):
                r = l + length - 1
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n - 2]"""
        ),
        (
            "11_Regular_Expression_Matching.py",
            "LeetCode 10: Regular Expression Matching",
            "Meta, Google, Amazon, Microsoft, Nvidia, Apple, Coursera",
            "O(M * N) - Memoized top-down DP over indices `(i, j)`.",
            "O(M * N) - Cache dictionary storing `(i, j)` states.",
            "When the next pattern char is `'*'` (`p[j+1] == '*'`), branch into skipping `x*` (`dfs(i, j + 2)`) or consuming one matching char from `s` (`match and dfs(i + 1, j)`).",
            "Memoizing `(i, j)` prevents exponential backtracking when multiple `*` wildcards appear.",
            """class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)"""
        ),
    ],
    "15_Greedy": [
        (
            "01_Maximum_Subarray.py",
            "LeetCode 53: Maximum Subarray",
            "LinkedIn, Amazon, Apple, Microsoft, Meta, Google, Bloomberg, Cisco",
            "O(N) - Kadane's single-pass algorithm.",
            "O(1) - Two scalar variables `cur_sum` and `max_sub`.",
            "Kadane's Algorithm: whenever the running prefix sum `cur_sum` becomes negative, reset it to `0` because a negative prefix can only hurt any future subarray.",
            "Solves maximum contiguous sum in a single O(N) pass with O(1) memory instead of O(N²) prefix scans.",
            """from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub"""
        ),
        (
            "02_Jump_Game.py",
            "LeetCode 55: Jump Game",
            "Amazon, Google, Microsoft, Meta, Apple, Uber, DoorDash",
            "O(N) - Single backward greedy pass.",
            "O(1) - Single `goal` index variable.",
            "Start with `goal = len(nums) - 1` and walk backward. Whenever index `i` can reach or pass `goal` (`i + nums[i] >= goal`), shift `goal = i`.",
            "Dynamic programming takes O(N²) time and O(N) space. Backward greedy goal-shifting runs in O(N) time and O(1) space.",
            """from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0"""
        ),
        (
            "03_Jump_Game_II.py",
            "LeetCode 45: Jump Game II",
            "Amazon, Google, Apple, TikTok, Microsoft, Bloomberg",
            "O(N) - 1D level-by-level greedy BFS window `[l, r]`.",
            "O(1) - Tracks only window pointers `l`, `r`, and `jumps`.",
            "Maintain the current jump range `[l, r]` (like a BFS level). Scan `[l, r]` to find the `farthest` index reachable in one more jump, then advance `(l, r) = (r + 1, farthest)`.",
            "Simulates level-order shortest-path BFS on the array in O(N) time using O(1) pointers instead of a queue.",
            """from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = max(i + nums[i] for i in range(l, r + 1))
            l = r + 1
            r = farthest
            jumps += 1
        return jumps"""
        ),
        (
            "04_Gas_Station.py",
            "LeetCode 134: Gas Station",
            "Amazon, Microsoft, Google, Bloomberg, Apple, Goldman Sachs",
            "O(N) - Single greedy pass over all stations.",
            "O(1) - Scalar `total` and `start` variables.",
            "If `sum(gas) < sum(cost)`, no solution exists. Otherwise, maintain a running `tank`; whenever `tank < 0` at index `i`, none of the stations up to `i` can be the start, so reset `start = i + 1` and `tank = 0`.",
            "Eliminates the entire failed prefix at once instead of restarting from every station in O(N²) time.",
            """from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start"""
        ),
        (
            "05_Hand_of_Straights.py",
            "LeetCode 846: Hand of Straights",
            "Google, Amazon, Straights, Rubrik",
            "O(N log N) - Frequency map plus min-heap of unique card values.",
            "O(N) - Counter dictionary and min-heap.",
            "The smallest remaining card `first = min_heap[0]` MUST be the start of a consecutive run `first, first+1, ..., first+groupSize-1`. Greedily decrement counts and pop exhausted values from the min-heap.",
            "Using a min-heap over unique values always anchors each group at the smallest available card in O(N log N) time.",
            """from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True"""
        ),
        (
            "06_Merge_Triplets_to_Form_Target_Triplet.py",
            "LeetCode 1899: Merge Triplets to Form Target Triplet",
            "Google, Amazon",
            "O(N) - Single filter and match pass over N triplets.",
            "O(1) - Set of at most 3 matched coordinate indices `{0, 1, 2}`.",
            "Any triplet with a value exceeding `target` in ANY position is unusable (since `max` can never shrink it). Among usable triplets, check if `target[0]`, `target[1]`, and `target[2]` each appear at least once.",
            "Single O(N) pass with O(1) space.",
            """from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3"""
        ),
        (
            "07_Partition_Labels.py",
            "LeetCode 763: Partition Labels",
            "Amazon, Meta, Google, LinkedIn, Nvidia",
            "O(N) - One pass to record last indices, one pass to cut partitions.",
            "O(1) - Dictionary of at most 26 lowercase character last-occurrence indices.",
            "Precompute `last[ch]` for every character. As we scan `i`, extend the current partition's right boundary `end = max(end, last[s[i]])`. When `i == end`, close the partition!",
            "Finds all minimal self-contained partitions in two O(N) passes with O(1) space.",
            """from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        size = end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, last[ch])
            if i == end:
                res.append(size)
                size = 0
        return res"""
        ),
        (
            "08_Valid_Parenthesis_String.py",
            "LeetCode 678: Valid Parenthesis String",
            "Amazon, Meta, Yahoo, Google, LinkedIn, Apple",
            "O(N) - Single pass tracking `[left_min, left_max]` range.",
            "O(1) - Two integer range variables.",
            "Track the range `[left_min, left_max]` of possible unmatched open parentheses: `'('` increments both, `')'` decrements both, and `'*'` decrements `left_min` and increments `left_max` (clamping `left_min = max(left_min, 0)`).",
            "Reduces O(3^N) wildcard branching and O(N²) DP down to O(N) time and O(1) space.",
            """class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for ch in s:
            if ch == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif ch == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0"""
        ),
    ],
    "16_Intervals": [
        (
            "01_Insert_Interval.py",
            "LeetCode 57: Insert Interval",
            "Google, LinkedIn, Amazon, Meta, Robinhood, Uber, Apple",
            "O(N) - Single pass over already-sorted intervals.",
            "O(N) - Output list of merged intervals.",
            "For each interval: if it ends strictly before `newInterval`, append it; if it starts strictly after `newInterval`, append `newInterval` and return with the rest; otherwise merge them via `[min(starts), max(ends)]`.",
            "Exploits the pre-sorted order to insert and merge in O(N) time without re-sorting.",
            """from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > e:
                res.append([s, e])
            else:
                newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
        res.append(newInterval)
        return res"""
        ),
        (
            "02_Merge_Intervals.py",
            "LeetCode 56: Merge Intervals",
            "Meta, Amazon, Google, Bloomberg, Salesforce, Microsoft, Uber, Apple",
            "O(N log N) - Sort by start time followed by O(N) linear merge.",
            "O(N) - Output list of merged intervals.",
            "Sort intervals by start time. If the current interval's `start` is `<=` the previous merged interval's `end`, extend the previous interval's `end = max(prev_end, end)`.",
            "Sorting by start time ensures all overlapping intervals become contiguous, allowing a single O(N) merge pass.",
            """from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output"""
        ),
        (
            "03_Non_Overlapping_Intervals.py",
            "LeetCode 435: Non-overlapping Intervals",
            "Amazon, Meta, Google, JPMorgan, Microsoft",
            "O(N log N) - Sort by start/end time plus O(N) greedy sweep.",
            "O(1) - Tracks only `prev_end` and `removals`.",
            "When two intervals overlap (`start < prev_end`), greedily remove the interval with the LARGER end time (`prev_end = min(prev_end, end)`) so it is less likely to collide with future intervals.",
            "Greedy earliest-end selection is provably optimal and runs in O(N log N) time with O(1) extra space.",
            """from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        return res"""
        ),
        (
            "04_Meeting_Rooms.py",
            "LeetCode 252: Meeting Rooms",
            "Amazon, Google, Meta, Bloomberg, Microsoft",
            "O(N log N) - Sorts intervals by start time and checks adjacent pairs.",
            "O(1) - In-place sort and constant comparison.",
            "Sort meetings by start time and verify that every meeting finishes before or when the next meeting begins (`intervals[i-1][1] <= intervals[i][0]`).",
            "Reduces O(N²) all-pairs overlap checks to N - 1 adjacent checks after sorting.",
            """from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True"""
        ),
        (
            "05_Meeting_Rooms_II.py",
            "LeetCode 253: Meeting Rooms II",
            "Amazon, Bloomberg, Meta, Google, Uber, Microsoft, Apple, Snap",
            "O(N log N) - Sorts separate start and end arrays and sweeps with two pointers.",
            "O(N) - Sorted `starts` and `ends` lists.",
            "Separate all `starts` and `ends` into two sorted arrays. Walk through chronologically: each start before the earliest end increments active rooms (`count += 1`), while an end frees a room (`count -= 1`).",
            "Two-pointer chronological sweep avoids heap push/pop overhead while tracking the exact peak concurrent meetings.",
            """from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        res = count = s = e = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res"""
        ),
        (
            "06_Minimum_Interval_to_Include_Each_Query.py",
            "LeetCode 1851: Minimum Interval to Include Each Query",
            "Google, Amazon, Bloomberg",
            "O(N log N + Q log Q) - Offline sorted queries with a min-heap of active intervals.",
            "O(N + Q) - Min-heap of `(size, right_end)` and query answers.",
            "Sort both `intervals` and `queries`. For each query `q`, push all intervals starting `<= q` into a Min-Heap keyed by `(interval_size, right_end)`, and pop expired intervals where `right_end < q`.",
            "Offline sorting + min-heap processes all Q queries and N intervals in a single pass instead of O(N * Q) brute force.",
            """from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]"""
        ),
    ],
    "17_Math_and_Geometry": [
        (
            "01_Rotate_Image.py",
            "LeetCode 48: Rotate Image",
            "Amazon, Cisco, Microsoft, Apple, Meta, Google, Bloomberg",
            "O(N²) - Visits each matrix cell once.",
            "O(1) - In-place transpose followed by horizontal row reversal.",
            "A 90-degree clockwise rotation is mathematically equivalent to: 1) Transposing the matrix across its main diagonal (`matrix[r][c] <-> matrix[c][r]`), then 2) Reversing each row.",
            "Rotates the matrix in-place in O(1) space without complex 4-corner index arithmetic.",
            """from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()"""
        ),
        (
            "02_Spiral_Matrix.py",
            "LeetCode 54: Spiral Matrix",
            "Amazon, Microsoft, Apple, Meta, Google, Cisco, Bloomberg",
            "O(M * N) - Visits every cell in the matrix exactly once.",
            "O(1) - Four boundary pointers `left`, `right`, `top`, `bottom`.",
            "Maintain four shrinking boundaries (`top`, `bottom`, `left`, `right`). Sweep right across `top`, down along `right`, left across `bottom`, and up along `left`, shrinking each boundary after its sweep.",
            "Cleanly handles non-square matrices in O(1) auxiliary space.",
            """from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res"""
        ),
        (
            "03_Set_Matrix_Zeroes.py",
            "LeetCode 73: Set Matrix Zeroes",
            "Amazon, Microsoft, Meta, Bloomberg, Apple, Oracle",
            "O(M * N) - Two passes over the matrix.",
            "O(1) - Uses the first row and first column of `matrix` itself as markers.",
            "Use `matrix[r][0]` and `matrix[0][c]` as in-place boolean flags to mark which rows and columns must be zeroed, plus a single boolean `row_zero` for row 0.",
            "Eliminates O(M + N) row/column marker arrays by storing the markers inside row 0 and col 0 in O(1) space.",
            """from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0"""
        ),
        (
            "04_Happy_Number.py",
            "LeetCode 202: Happy Number",
            "Amazon, Google, Apple, Uber, Bloomberg, PayPal",
            "O(log N) - Digit-square transitions quickly drop below 243 and terminate or cycle.",
            "O(1) - Floyd's Tortoise and Hare cycle detection.",
            "Repeatedly replace `n` with the sum of squares of its digits. Use `slow` and `fast` pointers to detect whether the sequence reaches `1` or enters a cycle.",
            "Floyd's cycle detection avoids storing seen numbers in a hash set, running in O(1) memory.",
            """class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1"""
        ),
        (
            "05_Plus_One.py",
            "LeetCode 66: Plus One",
            "Google, Amazon, Microsoft, Meta, Apple",
            "O(N) - Scans from the rightmost digit and exits early as soon as a non-9 digit is found.",
            "O(1) - Mutates `digits` in-place.",
            "Walk right-to-left: if `digits[i] < 9`, increment `digits[i] += 1` and return immediately; otherwise set `digits[i] = 0` and carry left. If all digits were `9`, return `[1] + digits`.",
            "Handles carries in-place without string/integer conversion.",
            """from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits"""
        ),
        (
            "06_Pow_x_n.py",
            "LeetCode 50: Pow(x, n)",
            "Meta, Amazon, Bloomberg, Google, LinkedIn, Apple, Microsoft",
            "O(log N) - Binary exponentiation halves the exponent each step.",
            "O(1) - Iterative squaring loop.",
            "Binary Exponentiation: `x^n = (x * x)^(n // 2)`. Whenever `n` is odd, multiply `res *= x`; then square `x *= x` and halve `n //= 2`.",
            "Multiplying `x` N times takes O(N) time and times out for `n = 2^31`. Squaring halves the exponent every step for O(log N) speed.",
            """class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res"""
        ),
        (
            "07_Multiply_Strings.py",
            "LeetCode 43: Multiply Strings",
            "Meta, Microsoft, Amazon, Google, Apple, Yandex",
            "O(M * N) - Grade-school digit-by-digit multiplication.",
            "O(M + N) - Result digit array of length `len(num1) + len(num2)`.",
            "Multiplying `num1[i]` and `num2[j]` from reversed strings contributes directly to positions `res[i + j]` (ones place) and `res[i + j + 1]` (carry).",
            "Accumulates products directly into a fixed `M + N` array without intermediate string additions.",
            """class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))"""
        ),
        (
            "08_Detect_Squares.py",
            "LeetCode 2013: Detect Squares",
            "Google, Amazon, Goldman Sachs",
            "O(1) for `add`, O(N) for `count` by checking diagonal points.",
            "O(N) - Counter map of `(x, y)` point frequencies.",
            "To count axis-aligned squares with query point `(px, py)`, iterate over each stored point `(x, y)`: if it forms a valid non-zero square diagonal (`abs(py - y) == abs(px - x)` and `x != px`), multiply the counts of the other two required corners `(x, py)` and `(px, y)`.",
            "Iterating only over diagonal candidates fixes the side length immediately, reducing 3-corner search to O(1) hash lookups per point.",
            """from typing import List
from collections import Counter

class DetectSquares:
    def __init__(self):
        self.pts_count = Counter()

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.pts_count.items():
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += cnt * self.pts_count[(x, py)] * self.pts_count[(px, y)]
        return res"""
        ),
    ],
    "18_Bit_Manipulation": [
        (
            "01_Single_Number.py",
            "LeetCode 136: Single Number",
            "Amazon, Google, Apple, Microsoft, Meta, Bloomberg",
            "O(N) - Single XOR reduction over all N numbers.",
            "O(1) - Single accumulator variable `res`.",
            "XOR has the properties `a ^ a = 0` and `a ^ 0 = a`. XORing all numbers together cancels every duplicate pair to `0`, leaving only the unique number!",
            "Achieves O(N) time and strict O(1) memory without a hash set.",
            """from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res"""
        ),
        (
            "02_Number_of_1_Bits.py",
            "LeetCode 191: Number of 1 Bits",
            "Apple, Amazon, Qualcomm, Microsoft, Box, Cisco",
            "O(K) - Runs exactly K times where K is the number of set `1` bits (at most 32).",
            "O(1) - Constant space.",
            "Brian Kernighan's trick: `n &= (n - 1)` clears the lowest set `1` bit of `n` in a single operation. Count how many times this operation runs until `n == 0`.",
            "Skips all `0` bits completely, looping only as many times as there are `1` bits.",
            """class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res"""
        ),
        (
            "03_Counting_Bits.py",
            "LeetCode 338: Counting Bits",
            "Amazon, Google, Goldman Sachs, Nvidia, Apple",
            "O(N) - Computes each number's bit count in O(1) using `dp[i >> 1] + (i & 1)`.",
            "O(N) - Output array `dp` of length `n + 1`.",
            "The number of 1-bits in `i` equals the number of 1-bits in `i >> 1` (which is `i // 2`, already computed!) plus the lowest bit `(i & 1)`.",
            "Reuses previously computed bit counts in O(1) per number instead of O(N log N).",
            """from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp"""
        ),
        (
            "04_Reverse_Bits.py",
            "LeetCode 190: Reverse Bits",
            "Apple, Amazon, Qualcomm, Nvidia, Meta",
            "O(1) - Fixed 32 iterations for a 32-bit unsigned integer.",
            "O(1) - Constant bitwise accumulator.",
            "For each bit position `i` from 0 to 31, extract the `i`-th bit `(n >> i) & 1` and shift it into its mirrored position `31 - i`.",
            "Constant-time 32-bit manipulation without string conversion.",
            """class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res"""
        ),
        (
            "05_Missing_Number.py",
            "LeetCode 268: Missing Number",
            "Amazon, Microsoft, Nvidia, Google, Meta, Apple",
            "O(N) - Single pass using XOR or Gauss's sum formula.",
            "O(1) - Single integer variable.",
            "By Gauss's formula, the expected sum of `0..n` is `n * (n + 1) // 2`. Subtracting `sum(nums)` leaves the exact missing number (or XOR `0..n` with `nums`).",
            "Finds the missing number in O(N) time and O(1) space without sorting or a hash set.",
            """from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)"""
        ),
        (
            "06_Sum_of_Two_Integers.py",
            "LeetCode 371: Sum of Two Integers",
            "Meta, Amazon, Apple, Microsoft, Hulu",
            "O(1) - At most 32 bitwise carry-propagation iterations.",
            "O(1) - 32-bit mask constants.",
            "Bitwise XOR `(a ^ b)` computes addition without carry, while `((a & b) << 1)` computes the carry bits. Repeat with a 32-bit mask `0xFFFFFFFF` until carry `b == 0`.",
            "Simulates hardware half-adder logic using pure bitwise operations without `+` or `-`.",
            """class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)"""
        ),
        (
            "07_Reverse_Integer.py",
            "LeetCode 7: Reverse Integer",
            "Amazon, Apple, Adobe, Google, Bloomberg, Microsoft, Meta",
            "O(log₁₀ X) - Processes at most 10 base-10 digits.",
            "O(1) - Scalar accumulator and 32-bit overflow bounds.",
            "Pop the last digit `digit = x % 10` and push it onto `res = res * 10 + digit`, checking before the final step if `res` would overflow signed 32-bit bounds `[-2^31, 2^31 - 1]`.",
            "Checks overflow mathematically before multiplying by 10 in O(1) space.",
            """class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            x, digit = divmod(x, 10)
            res = res * 10 + digit
        res *= sign
        return res if -(2**31) <= res <= 2**31 - 1 else 0"""
        ),
    ],
}
