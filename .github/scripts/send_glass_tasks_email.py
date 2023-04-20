
import os

import requests

from email.message import EmailMessage

def get_glass_tasks():
    token = os.environ.get("GITHUB_TOKEN", "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")
    headers = {
        "Accept": "application/vnd.github.inertia-preview+json",
        "Authorization": f"Bearer {token}",
    }

    owner = "alicemist"
    repo = "alicemist"
    url = f"https://api.github.com/repos/{owner}/{repo}/projects"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    projects = response.json()
    print(projects)
    glass_project = next((project for project in projects if project["name"] == "Glass"), None)

    if glass_project is None:
        print("Glass project not found.")
        return []

    project_id = glass_project["id"]
    columns_url = f"https://api.github.com/projects/{project_id}/columns"
    columns_response = requests.get(columns_url, headers=headers)
    columns_response.raise_for_status()

    columns = columns_response.json()

    task_list = []
    for column in columns:
        column_id = column["id"]
        cards_url = f"https://api.github.com/projects/columns/{column_id}/cards"
        cards_response = requests.get(cards_url, headers=headers)
        cards_response.raise_for_status()

        cards = cards_response.json()
        for card in cards:
            task_list.append(card["note"])

    return task_list

def send_github_notification(task_list):
    user = "alicemist"
    repo = "alicemist"
    token ='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'# os.environ["GITHUB_TOKEN"]

    issue_title = "Your Daily Glass Tasks"
    issue_body = f"Here are your daily Glass tasks:\n\n{task_list}"
    url = f"https://api.github.com/repos/{user}/{repo}/issues"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }
    payload = {
        "title": issue_title,
        "body": issue_body,
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("GitHub notification created successfully")
    else:
        print(f"Error creating GitHub notification: {response.status_code} - {response.text}")

if __name__ == "__main__":
    get_glass_tasks()
    