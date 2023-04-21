import random
import datetime
import subprocess
import os

def set_date(date):
    date_cmd = f'date -s "{date}"'
    os.system(date_cmd)

def make_commit(commit_date_str):
    commit_cmd = f'git commit --allow-empty -m "dummy commit" --date="{commit_date_str}"'
    subprocess.run(commit_cmd, shell=True)
# Başlangıç ve Bitiş Tarihleri

start_date_str = "2022-02-01"
end_date_str = "2022-3-01"

start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

# Her gün için rastgele commit sayısı ve tarihleri belirleme
for i in range((end_date - start_date).days + 1):
    commit_date = start_date + datetime.timedelta(days=i)
    commit_count = random.randint(0, 7)
    rand=random.randint(0,1) # her gün için 10-25 arası rastgele commit sayısı belirleme
    print(commit_count*rand)
    print(i)
    # Rastgele commit tarihleri belirleme
    for j in range(commit_count):
        commit_datetime_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
        make_commit(commit_datetime_str)
    

    
# Sistem tarihini geri yükleme
