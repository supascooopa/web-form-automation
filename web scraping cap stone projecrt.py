from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="geckodriver.exe")

url = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66775128825587%2C%22north%22%3A37.88267541816452%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A1235192%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

list_of_links = []
list_of_price = []
list_of_address = []
for div in soup.find_all('div', attrs={"class": 'list-card-info'}):
    try:
        link = div.find('a')['href']
        if link.startswith("https://www.zillow.com"):
            list_of_links.append(link)
            price = div.find('div', {"class": "list-card-price"}).text
            address = div.find('address').text
            list_of_price.append(price)
            list_of_address.append(address)
    except TypeError:
        print("no link!")
for link, price, address in zip(list_of_links, list_of_price, list_of_address):
    driver.get('https://forms.gle/3NfssLunatHNuDMJ6')
    time.sleep(5)
    link_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link)
    price_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
    address_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
    time.sleep(5)
    driver.find_element_by_css_selector("div .appsMaterialWizButtonEl").click()




