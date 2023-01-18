import requests
from bs4 import BeautifulSoup

page = requests.get('https://jadwalsholat.org/jadwal-sholat/monthly.php')

print(page.content)

after_bs = BeautifulSoup(page.content, 'html.parser')
find_data = after_bs.find_all(id="table_navigasi")

for x in find_data:
    print(x.table)
    