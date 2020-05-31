from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from utils.audio import convert_to_audio
locator_for_content = '#section'
locator_for_expander = 'div.expander'
locator_for_section = 'ul.landing-page__umbrella__section__list a.landing-page__umbrella__link'
locator_for_pages = 'div.interior-sticky-nav__main a'
def traverse_main(link,name):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    soup = soup.select_one(locator_for_expander)
    sections = soup.select(locator_for_section)
    sections.pop(0)
    page_links = ['https://www.sparknotes.com'+i.attrs['href'] for i in sections]
    traverse_pages(page_links,name)
def traverse_pages(page_links,name):
    final_data=''
    driver = webdriver.Chrome('chromedriver.exe')
    driver.minimize_window()
    all_pages = []
    for link in page_links:
        driver.get(link)
        time.sleep(0.5)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        extra_links = soup.select(locator_for_pages)
        for extra_link in extra_links:
            all_pages.append(link+extra_link.attrs['href'])
    for page in all_pages:
        driver.get(page)
        time.sleep(0.5)
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        all_data = soup.select_one(locator_for_content)
        for data in all_data.findAll(recursive = False,name=['h4','h3','p']):
            final_data += str(data.string) + '\n'
    convert_to_audio(final_data, name)




