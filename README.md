# ⚡ LeetType - Code Speed Typing & Big O Complexity Mentor

**LeetType** is a high-performance desktop application for Windows built to help software engineers **type code faster**, **memorize syntax patterns**, and **deeply understand algorithms and Big O complexities** by listening to dual AI audio explanations while typing.

---

## 🚀 Key Features

### 1. 📁 Organized LeetCode Problem Hierarchy
- Pre-populated with curated LeetCode solutions categorized into topic subfolders:
  - `01_Arrays_and_Hashing` (Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Top K Frequent)
  - `02_Two_Pointers` (Valid Palindrome, Two Sum II, 3Sum, Container With Most Water)
  - `03_Sliding_Window` (Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters)
  - `04_Stack` (Valid Parentheses, Min Stack)
  - `05_Binary_Search` (Binary Search, Search a 2D Matrix)
  - `06_Linked_List` (Reverse Linked List, Merge Two Sorted Lists)
  - `07_Trees` (Invert Binary Tree, Maximum Depth of Binary Tree)
  - `08_Dynamic_Programming` (Climbing Stairs, Coin Change)
  - `09_Graphs` (Number of Islands)
- **Add Your Own Problems**: Click **"📂 Open Solutions Folder"** anytime to drop in your own `.py` files and subfolders.

---

### 2. 💡 Two Distinct Explanations & Dual Audio Playbacks
Every problem features two separate, dedicated learning tracks—both with full text breakdowns and independent **AI Text-to-Speech Audio Playbacks**:

1. **💡 Track 1: Code Walkthrough, Intuition & Why It's Optimal**
   - **Core Understanding & Intuition**: The mental model and key insight behind the algorithm.
   - **Why This Is the Most Efficient Solution**: Direct comparison against naive/brute-force approaches and how the chosen data structure or paradigm eliminates redundant work.
   - **Step-by-Step Code Walkthrough**: Line-by-line explanation of the exact Python syntax you are typing.
   - **▶ 1. Walkthrough Audio**: Dedicated spoken narration walking you through the intuition, optimality, and code line by line while you type.

2. **📊 Track 2: Separate Big O Runtime & Memory Complexity Analysis**
   - **Runtime Complexity (Time Big O)**: Detailed breakdown of loop iterations, recursion depth, and inner operation costs.
   - **Memory Complexity (Space Big O)**: Auxiliary data structures allocated, call stack frames, and in-place optimizations.
   - **Complexity Deep Dive & Trade-offs**: Best vs. worst case bounds and time-space trade-offs.
   - **▶ 2. Big O Audio**: Dedicated spoken narration explaining the runtime and memory bounds in detail.

---

### 3. 🤖 Multi-Provider Free LLM Support & Offline Engine
- **Curated & Offline AST Analyzer** *(Default — Works out of the box with zero setup or API keys!)*
- **Groq API** *(Free & ultra-fast Llama-3.3 70B)*
- **Google Gemini API** *(Free tier Gemini 2.0 Flash)*
- **OpenRouter API** *(Free tier models like `google/gemini-2.0-flash-lite:free`)*
- **Ollama** *(Local offline LLMs running on `http://localhost:11434`)*

---

### 4. 🎧 AI Text-to-Speech (Listen While Typing)
- **Microsoft Edge Neural AI Voices**: Natural voices (Christopher, Guy, Jenny, Aria, Ryan, Sonia).
- **Windows System SAPI Voice**: Built-in zero-latency offline speech fallback.
- **Full Transport Controls**: Play Track 1 (Walkthrough), Play Track 2 (Big O), Pause/Resume, Stop, timeline scrubber, playback speed (`0.75x` to `1.5x`), and Auto-play.

---

### 5. ⌨ Precision Code Typing Arena
- **Real-Time Visual Feedback**: Green for correct characters, red highlight for typos, glowing cursor caret, and active line highlight.
- **Code-Friendly Ergonomics**: `Tab` inserts 4 spaces, `Enter` advances line and auto-matches leading indentation, and `Backspace` corrects mistakes.
- **Live Stats Bar**: Words Per Minute (**WPM**), Accuracy (**ACC**), Elapsed Time (**TIME**), Mistake Counter (**ERRORS**), and progress bar.
- **Tactile Audio Feedback**: Subtle mechanical switch click sounds (toggleable).

---

## 🏃 Running the Application

### Option A: Standalone Windows Executable
Double-click `Launch_LeetType.bat` or run:
```
dist/LeetType/LeetType.exe
```

### Option B: Run from Source
```bash
pip install -r requirements.txt
python main.py
```

### Option C: Build the Windows Executable Yourself
```bash
python build_exe.py
```

---

## ⚙ Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Tab` | Insert 4 spaces / Indent |
| `Ctrl + R` | Restart current problem |
| `Ctrl + N` | Next problem |
| `Ctrl + P` | Previous problem |
| `Ctrl + ,` | Open Settings dialog |
