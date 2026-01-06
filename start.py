import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_MAIN = os.path.join(BASE_DIR, "app", "main.py")

print("🚀 Starting Telegram Multi-Bot on Render")
print("📂 Base dir:", BASE_DIR)
print("📄 Main file:", APP_MAIN)

if not os.path.exists(APP_MAIN):
    print("❌ main.py not found!")
    print("📁 Current directory tree:")
    for root, dirs, files in os.walk(BASE_DIR):
        print(root, dirs, files)
    sys.exit(1)

# Run app/main.py
subprocess.run([sys.executable, APP_MAIN])
