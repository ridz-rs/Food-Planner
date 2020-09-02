from bs4 import BeautifulSoup
import requests, csv

csv_file = open("../data_files/SubwayData_raw.csv", 'w')
writer = csv.writer(csv_file)
writer.writerow(['Food Item', 'Size', 'Price', 'Category'])
source = requests.get('https://allfoodmenuprices.org/subway-menu-prices/').text
soup = BeautifulSoup(source, "lxml")
table = soup.find('table')
item = ''
size = ''
price = ''
current_category = ''
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols)==0:
        print(row)
        print("======......................=======")
        continue
    if len(cols) == 1:
        current_category = cols[0].text
        print("Category is", current_category)
        continue
    elif len(cols) == 2:
        print(cols[0].text, "\t", cols[1])
        item, price = cols[0].text, cols[1].text
    else:
        print(cols[0].text, "\t", cols[1].text, "\t", cols[2].text)
        item = cols[0].text
        size = cols[1].text
        price = cols[2].text

    print("==============================")
    writer.writerow([item, size, price, current_category])
csv_file.close()