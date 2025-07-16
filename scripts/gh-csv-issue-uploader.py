# Optional mapping from your CSV fields to GitHub labels
def generate_labels(row):
    labels = []
    if row.get('Epic'):
        labels.append(row['Epic'])
    if row.get('Status'):
        labels.append(row['Status'])
    return labels

def create_issue(title, body, labels):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json'
    }
    data = {
        'title': title,
        'body': body,
        'labels': labels
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'Issue created: {title}')
    else:
        print(f'URL: {url}')
        print(f'Failed to create issue: {title}')
        print(f'Status Code: {response.status_code}')
        print(f'Response: {response.json()}')

def main():
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row.get('Title', 'No Title')
            body = row.get('Body', '')
            labels = generate_labels(row)
            create_issue(title, body, labels)

if __name__ == '__main__':
    main()
