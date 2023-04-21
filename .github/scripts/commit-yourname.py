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
start_date_str = "2023-01-01"
end_date_str = "2023-01-15"

# Başlangıç ve Bitiş Tarihleri datetime objelerine çevirilir
start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

# Her gün için rastgele commit sayısı belirleme
for i in range((end_date - start_date).days + 1):
    commit_count = random.randint(1, 5) # her gün için 1-5 arası rastgele commit sayısı belirleme
    commit_date = start_date + datetime.timedelta(days=i)
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Tarihi ayarlama
    set_date(commit_date_str)

    # Rastgele sayıda commit oluşturma
    for j in range(commit_count):
        make_commit(commit_date_str)

# Sistem tarihini geri yükleme
os.system("date -s 'now'")
