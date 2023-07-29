import os
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

start_date = datetime(2023, 6, 10)
end_date = datetime(2023, 6, 12)

commit_count = 10  # Change this number as needed

for _ in range(commit_count):
    random_commit_date = random_date(start_date, end_date)
    # Here we adjust the date format
    random_commit_date_str = random_commit_date.isoformat() 

    # Making random change to a file
    with open('file.txt', 'a') as file:  
        file.write(random_commit_date_str + "\n")

    # Staging the changes
    os.system('git add file.txt')

    # Commiting with the specific date
    os.system(f'set GIT_AUTHOR_DATE={random_commit_date_str} && set GIT_COMMITTER_DATE={random_commit_date_str} &&'
              f'git commit -m "random commit"')