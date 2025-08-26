import os
import subprocess
import sys

def install_tools():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    tools_dir = os.path.join(base_dir, "tools")
    os.makedirs(tools_dir, exist_ok=True)

    sherlock_dir = os.path.join(tools_dir, "sherlock")
    if not os.path.exists(sherlock_dir):
        subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock.git", sherlock_dir])
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", f"{sherlock_dir}/requirements.txt"])

    whats_dir = os.path.join(tools_dir, "whatsmyname")
    if not os.path.exists(whats_dir):
        subprocess.run(["git", "clone", "https://github.com/WebBreacher/WhatsMyName.git", whats_dir])

    try:
        import holehe
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "holehe"])