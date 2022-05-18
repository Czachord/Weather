from turtle import title
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests, sys
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def getSite(country, city):
    global soup
    html = requests.get(f'https://www.timeanddate.com/weather/{country}/{city}', headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

def noneCheck(object):
    if object == None:
        sys.exit("Something went wrong, please try again and make sure you entered the country and city correctly")

def getTitle():
    if len(soup.find_all("td")) > 0:
        title = [soup.find_all("td")[2].getText().strip(), soup.find_all("td")[0].getText().strip()]
        return title
    else:
        sys.exit("Something went wrong, please try again and make sure you entered the country and city correctly")

def getX(id, index):
    object_ = soup.find_all(id)[index]
    noneCheck(object_)
    return object_.get_text().strip()

def createTable():
    table = [
        ["Weather forecast:", getX("p", 0)],
        ["Temperature:", getX("td", 19)],
        ["Min / Max Temp:", getX("p", 1)[26:36]],
        ["Fells Like:", getX("p", 1)[12:17]],
        ["Wind speed:", getX("p", 1)[41:47]],
        ["Pressure:", getX("td", 4)],
        ["Visibility:", getX("td", 3)],
        ["Humidity", getX("td", 5)]
    ]
    return ("\n" + tabulate(table, getTitle(), tablefmt="github"))

def main():
    country = input("Name of country: ").casefold()
    city = input("Name of city: ").casefold()
    getSite(country, city)
    print(createTable())

if __name__ == "__main__":
    main()