
import os

import requests

from email.message import EmailMessage

def get_user_project(user, project_number):
    token = os.environ["GITHUB_TOKEN"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    query = f"""
    query {{
      user(login: "{user}") {{
        projectV2(number: {project_number}) {{
          id
          title
          number
        }}
      }}
    }}
    """

    response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)
    response.raise_for_status()

    data = response.json()
    

    return data

def get_project_columns_and_cards(project_id):
    token = os.environ["GITHUB_TOKEN"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    query = f"""
 query {{
      node(id: "{project_id}") {{
        ... on ProjectV2 {{
            items(first:100) {{
                nodes{{
                    fieldValues(first: 4){{
                    nodes{{
                    ... on ProjectV2ItemFieldTextValue {{
                    text
                    field{{
                    ... on ProjectV2FieldCommon {{
                    name
                    }}
                    }}
                    }}
                                        }}
                    }}
                
                    
                }}
            }}
        
        }}
      }}
    }}
    
    """

    response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data
    

def send_github_notification(task_list):
    user = "alicemist"
    repo = "alicemist"
    token = os.environ["GITHUB_TOKEN"]

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

def get_last_three_tasks(user, project_number):
    project = get_user_project(user, project_number)
    
    project_id = project["data"]["user"]["projectV2"]["id"]
    task = get_project_columns_and_cards(project_id)
    task_list = []

    for item in task["data"]["node"]["items"]["nodes"]:
        
        for field_value in item["fieldValues"]["nodes"]:
            
            if "text" in field_value:
                task_list.append(field_value["text"])

    return task_list[-3:]

if __name__ == "__main__":
    user = "alicemist"
    project_number = 3
    last_three_tasks = get_last_three_tasks(user, project_number)
    print(last_three_tasks)