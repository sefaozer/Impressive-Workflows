import os
import smtplib
import requests
from email.message import EmailMessage

def get_glass_tasks():
    # GitHub API ile projenizdeki taskları alın
    # Örnek olarak, projenizin "Glass" adında bir hedefi olduğunu varsayalım
    user = "alicemist"
    token = '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' #os.environ["GITHUB_TOKEN"]
    url = f"https://api.github.com/users/{user}/projects"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }

    projects = requests.get(url, headers=headers).json()
    print("GitHub API Response:", projects)
    glass_project = next((project for project in projects if project["name"] == "Glass"), None)
    
    if glass_project is None:
        return "No Glass project found."

    tasks_url = glass_project["cards_url"]
    tasks = requests.get(tasks_url, headers=headers).json()

    task_list = []
    for task in tasks:
        task_list.append(task["note"])

    return "\n".join(task_list)

def send_email(task_list):
    email_username =os.environ["EMAIL_USERNAME"]
    email_password = os.environ["EMAIL_PASSWORD"]
    email_recipient = os.environ["EMAIL_RECIPIENT"]

    msg = EmailMessage()
    msg.set_content(f"Here are your daily Glass tasks:\n\n{task_list}")

    msg["Subject"] = "Your Daily Glass Tasks"
    msg["From"] = email_username
    msg["To"] = email_recipient

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email_username, email_password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    task_list = get_glass_tasks()
    send_email(task_list)
