"""
LeetCode 271: Encode and Decode Strings
Companies: Google, Meta, Amazon, Uber, LinkedIn, Square
Time Complexity: O(N) - Single pass over total character count N for both encode and decode.
Space Complexity: O(1) - Auxiliary space beyond the output string/list.
Intuition: Prefix each string with its character length followed by a delimiter `#` (e.g., `4#code`). During decoding, read the length up to `#` and slice that exact number of characters.
Why Efficient: Delimiter-escaping fails or scans twice when strings contain `#` or digits. Length-prefixing jumps directly over any inner characters in O(1) index slices.
"""
from typing import List

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
        return res
