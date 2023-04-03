# Programa istraukia straipsniu title is oxylabs blog puslapio
from bs4 import BeautifulSoup
import requests
import csv
response = requests.get('https://oxylabs.io/blog').text

# Output:
# Prints all blog tiles on the page
source = requests.get('https://oxylabs.io/blog/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('a', class_ ='e1dscegp0')

# for blokas in blokai:
#     print(blokas)
with open("Oxylabs_straipsniai2.csv", 'w', encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['CATEGORY','TEXT', 'LINK'])
    for blokas in blokai:
        try:
            kategorija = blokas.find_previous('a').text.strip()
            tekstas = blokas.find_previous('h5').text.strip()
            linkas = blokas.find_previous_sibling('a')['href']
            csv_writer.writerow([kategorija,tekstas,f'https://oxylabs.io{linkas}'])
            print(kategorija)
            print(tekstas)
            print(linkas)
        except:
            pass