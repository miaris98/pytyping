import os
import sys

def make_shortcut():
    desktop = os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(base_dir, 'dist', 'LeetType', 'LeetType.exe')
    icon = os.path.join(base_dir, 'assets', 'icon.ico')
    shortcut_path = os.path.join(desktop, 'LeetType.lnk')

    if not os.path.exists(target):
        print(f"Error: Executable not found at {target}. Build it first with 'python build_exe.py'.")
        return

    try:
        import win32com.client
        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.path.dirname(target)
        if os.path.exists(icon):
            shortcut.IconLocation = icon
        shortcut.Description = 'LeetType - Code Speed Typing & Big O Complexity Mentor'
        shortcut.save()
        print(f"Desktop shortcut created at: {shortcut_path}")
    except Exception as e:
        print(f"Failed to create shortcut: {e}")

if __name__ == '__main__':
    make_shortcut()

