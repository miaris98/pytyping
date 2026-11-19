import os
import shutil
from generate_neetcode_150_part1 import PART1_PROBLEMS
from generate_neetcode_150_part2 import PART2_PROBLEMS


def generate_all_neetcode_150():
    all_categories = {}
    all_categories.update(PART1_PROBLEMS)
    all_categories.update(PART2_PROBLEMS)

    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leetcode_problems")
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir, exist_ok=True)

    total_files = 0
    for folder, problem_tuples in sorted(all_categories.items()):
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for (
            filename,
            title,
            companies,
            time_comp,
            space_comp,
            intuition,
            why_efficient,
            code_body,
        ) in problem_tuples:
            file_path = os.path.join(folder_path, filename)
            file_content = (
                f'"""\n'
                f"{title}\n"
                f"Companies: {companies}\n"
                f"Time Complexity: {time_comp}\n"
                f"Space Complexity: {space_comp}\n"
                f"Intuition: {intuition}\n"
                f"Why Efficient: {why_efficient}\n"
                f'"""\n'
                f"{code_body.strip()}\n"
            )
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(file_content)
            total_files += 1

    print(f"Successfully generated {total_files} NeetCode solutions across {len(all_categories)} categories in {base_dir}")


if __name__ == "__main__":
    generate_all_neetcode_150()
