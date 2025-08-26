import subprocess
import os
import json
import hashlib

def run_sherlock(username):
    sherlock_script = os.path.abspath("tools/sherlock/sherlock.py")
    try:
        output = subprocess.getoutput(f"python3 {sherlock_script} {username} --print-found")
        return [line.replace("[+] ", "").strip() for line in output.splitlines() if line.startswith("[+]")]
    except Exception as e:
        return [f"❌ Sherlock Error: {e}"]

def run_holehe(email):
    try:
        cmd = f"holehe {email}"
        result = subprocess.getoutput(cmd)
        return [line for line in result.splitlines() if "[" in line]
    except Exception as e:
        return [f"❌ Holehe Error: {e}"]

def run_whatsmyname(username):
    try:
        with open("tools/whatsmyname/web_accounts_list.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        results = []
        for entry in data["accounts"]:
            if entry.get("check_type") == "url" and entry.get("url"):
                url = entry["url"].replace("{account}", username)
                results.append(url)
        return results[:30]
    except Exception as e:
        return [f"❌ WhatsMyName Error: {e}"]

def analyze_person(username=None, email=None, phone=None, name=None):
    result = {}
    if username:
        result['Sherlock Results'] = run_sherlock(username)
        result['WhatsMyName Links'] = run_whatsmyname(username)
    if email:
        result['Holehe Email Check'] = run_holehe(email)
        hashmail = hashlib.md5(email.lower().encode()).hexdigest()
        result['Gravatar'] = f"https://www.gravatar.com/avatar/{hashmail}?d=identicon"
    if phone:
        result['Google Search Phone'] = f"https://www.google.com/search?q=\"{phone}\""
    if name:
        result['Google Dork (Name)'] = f"https://www.google.com/search?q=\"{name}\" site:linkedin.com"
    return result