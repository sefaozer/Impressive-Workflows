import os
import subprocess
from datetime import datetime, timedelta





alphabet = {
    'A': ['010', '101', '111', '101', '101'],
    'B': ['110', '101', '110', '101', '110'],
    'C': ['011', '100', '100', '100', '011'],
    'D': ['110', '101', '101', '101', '110'],
    'E': ['111', '100', '110', '100', '111'],
    'F': ['111', '100', '110', '100', '100'],
    'G': ['011', '100', '101', '101', '011'],
    'H': ['101', '101', '111', '101', '101'],
    'I': ['111', '010', '010', '010', '111'],
    'J': ['001', '001', '001', '101', '011'],
    'K': ['101', '101', '110', '101', '101'],
    'L': ['100', '100', '100', '100', '111'],
    'M': ['111', '101', '101', '101', '101'],
    'N': ['111', '101', '101', '101', '101'],
    'O': ['011', '101', '101', '101', '011'],
    'P': ['110', '101', '110', '100', '100'],
    'Q': ['011', '101', '101', '101', '011', '001'],
    'R': ['110', '101', '110', '101', '101'],
    'S': ['011', '100', '010', '001', '110'],
    'T': ['111', '010', '010', '010', '010'],
    'U': ['101', '101', '101', '101', '011'],
    'V': ['101', '101', '101', '010', '010'],
    'W': ['101', '101', '101', '101', '111'],
    'X': ['101', '101', '010', '101', '101'],
    'Y': ['101', '101', '010', '010', '010'],
    'Z': ['111', '001', '010', '100', '111'],
    ' ': ['000', '000', '000', '000', '000'],
}




def set_date(date):
    date_cmd = f'date -s "{date}"'
    os.system(date_cmd)

def make_commit():
    commit_cmd = 'git commit --allow-empty -m "dummy commit"'
    subprocess.run(commit_cmd, shell=True)

def write_name(name, start_date, commit_every_n_days=2):
    name = name.upper()
    current_date = start_date
    os.environ['GIT_COMMITTER_DATE'] = current_date.strftime("%Y-%m-%d %H:%M:%S")

    for letter in name:
        letter_pattern = alphabet[letter]

        for row in letter_pattern:
            for column in row:
                if column == '1':
                    make_commit()
                current_date += timedelta(days=commit_every_n_days)
                os.environ['GIT_COMMITTER_DATE'] = current_date.strftime("%Y-%m-%d %H:%M:%S")

            current_date += timedelta(days=commit_every_n_days)
            os.environ['GIT_COMMITTER_DATE'] = current_date.strftime("%Y-%m-%d %H:%M:%S")

        current_date += timedelta(days=5*commit_every_n_days)
        os.environ['GIT_COMMITTER_DATE'] = current_date.strftime("%Y-%m-%d %H:%M:%S")

# Set Name and Starting Date
name = "Ali Cem"  # Set Name
start_date = datetime(year=2021, month=1, day=1)  # Set Starting Date


write_name(name, start_date)

# Set System clock to origin
os.system("date -u")

print(f"{name}")
