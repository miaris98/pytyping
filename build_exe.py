import os
import sys
import subprocess
import shutil

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    print("=== Building LeetType Windows Executable ===")
    
    # Verify icon exists
    ico_path = os.path.join(base_dir, "assets", "icon.ico")
    if not os.path.exists(ico_path):
        import generate_icon
        generate_icon.create_app_icon()

    # Verify sounds exist
    sounds_path = os.path.join(base_dir, "assets", "sounds", "click.wav")
    if not os.path.exists(sounds_path):
        import generate_sounds
        generate_sounds.generate_click()
        generate_sounds.generate_error()

    cmd = [
        "pyinstaller",
        "--noconfirm",
        "--onedir",
        "--windowed",
        "--name=LeetType",
        f"--icon={ico_path}",
        "--add-data=leetcode_problems;leetcode_problems",
        "--add-data=assets;assets",
        "--hidden-import=PyQt5.QtMultimedia",
        "--hidden-import=PyQt5.QtMultimediaWidgets",
        "--hidden-import=edge_tts",
        "--hidden-import=win32com.client",
        "--hidden-import=pythoncom",
        "--hidden-import=requests",
        "main.py"
    ]

    print("Running command:", " ".join(cmd))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("Build failed with returncode:", result.returncode)
        sys.exit(result.returncode)

    # Copy leetcode_problems alongside the exe in dist/LeetType/ as well
    dist_dir = os.path.join(base_dir, "dist", "LeetType")
    target_problems = os.path.join(dist_dir, "leetcode_problems")
    if not os.path.exists(target_problems):
        shutil.copytree(os.path.join(base_dir, "leetcode_problems"), target_problems)
        print("Copied leetcode_problems to dist/LeetType/")

    exe_path = os.path.join(dist_dir, "LeetType.exe")
    if os.path.exists(exe_path):
        print(f"\nSUCCESS! Executable created at: {exe_path}")
        print(f"File size: {os.path.getsize(exe_path) / 1024:.1f} KB")
    else:
        print("\nWarning: LeetType.exe was not found in dist/LeetType/")

if __name__ == "__main__":
    build()

