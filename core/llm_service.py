import os
import json
import ast
import hashlib
import requests
from typing import Dict, Any, Optional, List
from config import config, get_data_dir
from core.curated_explanations import CURATED_EXPLANATIONS

CACHE_DIR = os.path.join(get_data_dir(), "cache", "explanations")
os.makedirs(CACHE_DIR, exist_ok=True)


class OfflineCodeAnalyzer:
    """
    Intelligent AST-based analyzer and curated knowledge base for Python LeetCode solutions.
    Produces two distinct explanations and audio tracks:
    1. Code Walkthrough, Core Understanding & Why It Is Most Efficient
    2. Separate Big O Runtime & Memory Complexity Analysis
    """
    @staticmethod
    def analyze(code: str, problem_name: str = "") -> Dict[str, Any]:
        # Check curated database first for built-in problems
        if problem_name in CURATED_EXPLANATIONS:
            entry = dict(CURATED_EXPLANATIONS[problem_name])
            entry["provider"] = "Curated Algorithm Mentor (Offline)"
            return entry

        # Otherwise perform deep AST analysis for custom problem files
        has_sort = False
        has_heap = False
        has_dict = False
        has_set = False
        max_loop_depth = 0
        has_binary_search_pattern = False
        has_recursion = False
        has_two_pointers = False
        has_dp = False
        walkthrough_steps: List[str] = []

        try:
            tree = ast.parse(code)
            func_names = set()

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_names.add(node.name)
                    if node.name != "__init__":
                        args = [a.arg for a in node.args.args if a.arg != "self"]
                        walkthrough_steps.append(
                            f"Define `{node.name}({', '.join(args)})` to process the input parameters."
                        )

                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Attribute):
                        if node.func.attr == "sort":
                            has_sort = True
                        elif node.func.attr in ("heappush", "heappop"):
                            has_heap = True
                    elif isinstance(node.func, ast.Name):
                        if node.func.id == "sorted":
                            has_sort = True
                        elif node.func.id in ("dict", "defaultdict", "Counter"):
                            has_dict = True
                        elif node.func.id == "set":
                            has_set = True
                        elif node.func.id in func_names:
                            has_recursion = True

            class LoopVisitor(ast.NodeVisitor):
                def __init__(self):
                    self.current_depth = 0
                    self.max_depth = 0

                def visit_For(self, node):
                    self.current_depth += 1
                    self.max_depth = max(self.max_depth, self.current_depth)
                    self.generic_visit(node)
                    self.current_depth -= 1

                def visit_While(self, node):
                    self.current_depth += 1
                    self.max_depth = max(self.max_depth, self.current_depth)
                    self.generic_visit(node)
                    self.current_depth -= 1

            visitor = LoopVisitor()
            visitor.visit(tree)
            max_loop_depth = visitor.max_depth
        except Exception:
            pass

        code_lower = code.lower()
        if "low <= high" in code_lower or "left <= right" in code_lower or "// 2" in code_lower:
            has_binary_search_pattern = True
        if "left" in code_lower and "right" in code_lower:
            has_two_pointers = True
        if "dfs(" in code_lower or "bfs(" in code_lower:
            has_recursion = True
        if "dict" in code_lower or "{" in code_lower or "seen" in code_lower or "count" in code_lower:
            has_dict = True
        if "set(" in code_lower or "set()" in code_lower:
            has_set = True
        if "dp =" in code_lower or "dp[" in code_lower:
            has_dp = True

        # Line-by-line code walkthrough extraction
        code_lines = [
            ln.strip() for ln in code.splitlines()
            if ln.strip() and not ln.strip().startswith("#") and not ln.strip().startswith('"""')
        ]
        for ln in code_lines:
            if ln.startswith(("from ", "import ", "class ")):
                continue
            if len(walkthrough_steps) < 6:
                if ln.startswith("for ") or ln.startswith("while "):
                    walkthrough_steps.append(f"Iterate with `{ln.rstrip(':')}` to advance through the search state.")
                elif ln.startswith("if ") or ln.startswith("elif "):
                    walkthrough_steps.append(f"Check condition `{ln.rstrip(':')}` to handle branching or boundary logic.")
                elif ln.startswith("return "):
                    walkthrough_steps.append(f"Return final computed result via `{ln}`.")
                elif "=" in ln:
                    walkthrough_steps.append(f"Update state variable: `{ln}`.")

        if not walkthrough_steps:
            walkthrough_steps = [
                "Initialize auxiliary state variables and data structures.",
                "Traverse the input elements while maintaining problem invariants.",
                "Return the optimal result once traversal completes."
            ]

        # Determine Algorithmic Paradigm, Intuition & Efficiency
        if has_binary_search_pattern:
            paradigm = "Binary Search (Divide & Conquer)"
            core_understanding = (
                "By exploiting monotonic/sorted order, inspecting the midpoint immediately tells us which half "
                "contains the answer, letting us discard 50% of the remaining candidates on every step."
            )
            why_most_efficient = (
                "A linear scan checks every element in O(N) time. Binary search halves the search range each iteration, "
                "achieving logarithmic O(log N) runtime with O(1) extra memory."
            )
            time_comp = "O(log N)"
            time_expl = "Halves the search interval on each iteration, requiring at most log₂(N) comparisons."
        elif has_two_pointers and not has_sort:
            paradigm = "Two Pointers / Sliding Window"
            core_understanding = (
                "Coordinating `left` and `right` pointers across the sequence lets us evaluate or maintain a valid window "
                "in a single synchronized pass without re-scanning elements."
            )
            why_most_efficient = (
                "Nested brute-force loops re-examine the same elements in O(N²) time. Advancing two monotonic pointers "
                "visits each element a constant number of times, reducing runtime to O(N)."
            )
            time_comp = "O(N)"
            time_expl = "Both `left` and `right` pointers move monotonically across the N elements at most once."
        elif has_heap:
            paradigm = "Priority Queue / Heap"
            core_understanding = (
                "A heap maintains the minimum or maximum element at the root in logarithmic time without needing to "
                "sort the entire dataset."
            )
            why_most_efficient = (
                "Full sorting costs O(N log N). Keeping a bounded heap of size K costs only O(log K) per operation, "
                "achieving O(N log K) time."
            )
            time_comp = "O(N log K)"
            time_expl = "Iterates through N elements while performing O(log K) heap push/pop operations."
        elif has_dp:
            paradigm = "Dynamic Programming"
            core_understanding = (
                "Breaks the problem into overlapping subproblems and caches each subproblem's optimal answer so it is "
                "computed only once."
            )
            why_most_efficient = (
                "Naive recursion recomputes overlapping branches in exponential O(2^N) time. Tabulation/memoization "
                "collapses exponential branches into polynomial/linear time."
            )
            time_comp = "O(N²)" if max_loop_depth >= 2 else "O(N)"
            time_expl = "Computes each subproblem state once using O(1) state transitions."
        elif has_dict or has_set:
            paradigm = "Hash Map / Hash Set Lookup"
            core_understanding = (
                "By trading a small amount of memory to store previously seen values in a hash table, we turn slow "
                "linear searches into instantaneous O(1) lookups."
            )
            why_most_efficient = (
                "Eliminates the inner search loop of an O(N²) brute-force approach by answering membership or key "
                "queries in O(1) average time."
            )
            time_comp = "O(N)" if max_loop_depth <= 1 else "O(N²)"
            time_expl = "Visits each element and performs O(1) average-time hash table lookups and insertions."
        elif has_sort:
            paradigm = "Sorting + Greedy / Two-Pointer Sweep"
            core_understanding = (
                "Sorting organizes elements in monotonic order so duplicates sit next to each other and greedy or "
                "two-pointer decisions become deterministic."
            )
            why_most_efficient = (
                "Avoids higher-degree polynomial or exponential combinations by paying an upfront O(N log N) sort cost."
            )
            time_comp = "O(N log N)" if max_loop_depth <= 1 else "O(N²)"
            time_expl = "Sorting N elements takes O(N log N) time followed by a linear or two-pointer scan."
        elif max_loop_depth >= 2:
            paradigm = "Nested Iteration / Matrix Traversal"
            core_understanding = (
                "Systematically explores all 2D coordinates or element pairs while maintaining running invariants."
            )
            why_most_efficient = (
                "Processes each state directly without redundant recomputation."
            )
            time_comp = "O(N²)"
            time_expl = "Nested loops iterate across pairs or 2D grid dimensions."
        else:
            paradigm = "Single-Pass Traversal"
            core_understanding = (
                "Maintains running state variables as we walk through the data structure in a single forward pass."
            )
            why_most_efficient = (
                "Since every element must be inspected at least once, O(N) single-pass traversal is asymptotically optimal."
            )
            time_comp = "O(N)" if (max_loop_depth == 1 or has_recursion) else "O(1)"
            time_expl = "Visits each element once with O(1) work per step."

        # Determine Space Complexity
        if has_dp and ("[0] *" in code or "float('inf')" in code):
            space_comp = "O(N)"
            space_expl = "Allocates a dynamic programming table to store intermediate subproblem results."
        elif has_dict or has_set:
            space_comp = "O(N)"
            space_expl = "Uses an auxiliary hash map or hash set storing up to N elements in the worst case."
        elif has_recursion:
            space_comp = "O(H)"
            space_expl = "Recursive call stack depth grows proportional to the recursion tree height H."
        elif has_heap:
            space_comp = "O(K)"
            space_expl = "Maintains up to K elements inside the heap structure."
        else:
            space_comp = "O(1)"
            space_expl = "Operates in-place using only a fixed number of pointer or scalar variables."

        clean_name = problem_name.replace(".py", "").replace("_", " ")

        walkthrough_audio = (
            f"Code walkthrough and intuition for {clean_name}. "
            f"This solution uses {paradigm}. "
            f"{core_understanding} "
            f"Why is this the most efficient solution? {why_most_efficient} "
            f"Here is how the code works step by step: {' '.join(walkthrough_steps)}"
        )

        bigo_audio = (
            f"Big O Runtime and Memory analysis for {clean_name}. "
            f"The Time Complexity is {time_comp.replace('O(', 'O of ').replace(')', '')}. {time_expl} "
            f"The Space Complexity is {space_comp.replace('O(', 'O of ').replace(')', '')}. {space_expl}"
        )

        return {
            "title": clean_name,
            "core_understanding": core_understanding,
            "why_most_efficient": why_most_efficient,
            "code_walkthrough": walkthrough_steps,
            "walkthrough_audio_text": walkthrough_audio,
            "time_complexity": time_comp,
            "time_explanation": time_expl,
            "space_complexity": space_comp,
            "space_explanation": space_expl,
            "bigo_deep_dive": [
                f"Paradigm: {paradigm}",
                f"Runtime Bound: {time_comp} — {time_expl}",
                f"Memory Bound: {space_comp} — {space_expl}"
            ],
            "bigo_audio_text": bigo_audio,
            "provider": "Built-in Static Analyzer"
        }


class LLMService:
    def __init__(self):
        pass

    def _get_cache_path(self, code: str, problem_name: str) -> str:
        key = f"v2_{problem_name}_{hashlib.sha256(code.encode('utf-8')).hexdigest()[:12]}"
        return os.path.join(CACHE_DIR, f"{key}.json")

    def get_explanation(self, code: str, problem_name: str, force_refresh: bool = False) -> Dict[str, Any]:
        """Fetch dual explanation (Walkthrough + Big O) from cache, online LLM, or offline analyzer."""
        cache_file = self._get_cache_path(code, problem_name)

        if not force_refresh and os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cached = json.load(f)
                    if "core_understanding" in cached and "bigo_audio_text" in cached:
                        return cached
            except Exception:
                pass

        provider = config.get("llm_provider", "offline")
        result = None

        if provider == "groq" and config.get("groq_api_key"):
            result = self._call_groq(code, problem_name)
        elif provider == "gemini" and config.get("gemini_api_key"):
            result = self._call_gemini(code, problem_name)
        elif provider == "openrouter" and config.get("openrouter_api_key"):
            result = self._call_openrouter(code, problem_name)
        elif provider == "ollama":
            result = self._call_ollama(code, problem_name)

        if not result:
            result = OfflineCodeAnalyzer.analyze(code, problem_name)

        # Save to cache
        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
        except Exception as e:
            print(f"Error saving explanation cache: {e}")

        return result

    def _build_prompt(self, code: str, problem_name: str) -> str:
        return f"""You are a world-class coding interview mentor and algorithmic complexity expert.
Analyze this LeetCode Python solution for '{problem_name}':

```python
{code}
```

You must provide TWO comprehensive, distinct explanations and TWO separate spoken audio scripts:
1. Code Walkthrough, Core Understanding & Why This Is the Most Efficient Solution
2. Separate Big O Runtime & Memory Complexity Analysis

Return ONLY valid JSON matching this exact schema:
{{
  "title": "{problem_name}",
  "core_understanding": "Clear explanation of the core mental model and intuition behind the solution (2-3 sentences)",
  "why_most_efficient": "Explain why this is the most efficient solution compared to brute force or naive alternatives (2-3 sentences)",
  "code_walkthrough": [
    "Step 1: Detailed explanation of initialization / setup lines",
    "Step 2: Detailed explanation of the main loop / recursion and condition checks",
    "Step 3: Detailed explanation of state updates and return value"
  ],
  "walkthrough_audio_text": "A natural, engaging 45-60 second spoken audio narration walking through the core intuition, why this solution is optimal compared to brute force, and how the code works line by line as the user types it.",
  "time_complexity": "O(...)",
  "time_explanation": "Detailed explanation of why the runtime complexity is O(...) based on loop iterations and inner operations",
  "space_complexity": "O(...)",
  "space_explanation": "Detailed explanation of why the auxiliary memory complexity is O(...) based on allocated data structures or recursion stack",
  "bigo_deep_dive": [
    "Best/Worst case runtime breakdown",
    "Auxiliary memory vs input storage breakdown"
  ],
  "bigo_audio_text": "A dedicated, clear 30-45 second spoken audio narration explaining only the Big O runtime complexity and memory complexity in detail."
}}
Do not include any markdown backticks or commentary outside the JSON object.
"""

    def _call_groq(self, code: str, problem_name: str) -> Optional[Dict[str, Any]]:
        api_key = config.get("groq_api_key")
        model = config.get("groq_model", "llama-3.3-70b-versatile")
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a concise algorithm analysis assistant that responds only in JSON."},
                {"role": "user", "content": self._build_prompt(code, problem_name)}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.2
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                parsed = json.loads(content)
                parsed["provider"] = f"Groq ({model})"
                return parsed
        except Exception as e:
            print(f"Groq API call failed: {e}")
        return None

    def _call_gemini(self, code: str, problem_name: str) -> Optional[Dict[str, Any]]:
        api_key = config.get("gemini_api_key")
        model = config.get("gemini_model", "gemini-2.0-flash")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        prompt = self._build_prompt(code, problem_name)
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"response_mime_type": "application/json", "temperature": 0.2}
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = json.loads(text)
                parsed["provider"] = f"Google Gemini ({model})"
                return parsed
        except Exception as e:
            print(f"Gemini API call failed: {e}")
        return None

    def _call_openrouter(self, code: str, problem_name: str) -> Optional[Dict[str, Any]]:
        api_key = config.get("openrouter_api_key")
        model = config.get("openrouter_model", "google/gemini-2.0-flash-lite:free")
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a concise algorithm analysis assistant that responds only in JSON."},
                {"role": "user", "content": self._build_prompt(code, problem_name)}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.2
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                parsed = json.loads(content)
                parsed["provider"] = f"OpenRouter ({model})"
                return parsed
        except Exception as e:
            print(f"OpenRouter API call failed: {e}")
        return None

    def _call_ollama(self, code: str, problem_name: str) -> Optional[Dict[str, Any]]:
        base_url = config.get("ollama_url", "http://localhost:11434").rstrip("/")
        model = config.get("ollama_model", "llama3")
        url = f"{base_url}/api/generate"
        payload = {
            "model": model,
            "prompt": self._build_prompt(code, problem_name),
            "format": "json",
            "stream": False
        }
        try:
            resp = requests.post(url, json=payload, timeout=20)
            if resp.status_code == 200:
                content = resp.json().get("response", "")
                parsed = json.loads(content)
                parsed["provider"] = f"Ollama ({model})"
                return parsed
        except Exception as e:
            print(f"Ollama call failed: {e}")
        return None


# Global service instance
llm_service = LLMService()
