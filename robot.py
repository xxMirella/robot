from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import warnings
import sys

warnings.filterwarnings('ignore')

value = sys.argv

browser = RoboBrowser()
browser.open('https://www.vagalume.com.br/')

form = browser.get_form(action='/search.php')
form['q'].value = value
browser.submit_form(form)

soup = BeautifulSoup(browser.response.content, 'lxml')
markup_type = 'lxml'
songs = soup.find(id='artSongs').next_element.next_element

for item in songs.find_all('span'):
    print("Músicas = " + item.text)
