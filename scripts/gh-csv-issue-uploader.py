import csv
import requests

# CONFIG - Edit these before running
GITHUB_TOKEN = ''
REPO_OWNER = ''
REPO_NAME = ''
CSV_FILE = ''

# === HEADERS ===
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# === ISSUE CREATION FUNCTION ===
def create_issue(title, body, labels):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"✅ Created issue: {title}")
    else:
        print(f"❌ Failed to create issue: {title}")
        print("Status Code:", response.status_code)
        print("Response:", response.json())

# === READ CSV AND UPLOAD ===
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row["Title"]
        body = row["Body"]
        labels = []

        if row.get("Phase"):
            labels.append(row["Phase"])
        if row.get("Size"):
            labels.append(row["Size"])
        if row.get("Epic") and not title.startswith("[EPIC]"):
            labels.append(row["Epic"])

        create_issue(title, body, labels)
