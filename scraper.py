from selenium import webdriver
import time

urlList = list()
driver = webdriver.Chrome(executable_path="C:\chrome\chromedriver.exe")
driver.get("http://moz.com/top500/pages")
time.sleep(5)
while True:
    button = driver.find_element_by_id('top-500_next')
    if button.get_attribute('class') == 'button button-small paginate-navigation button-disabled':
        break
    button.click()
    tabs = driver.find_element_by_class_name('tabs')
    table = tabs.find_element_by_tag_name('table')
    tbody = table.find_element_by_tag_name('tbody')
    tr = tbody.find_elements_by_tag_name('tr')
    for eachtr in tr:
        a = eachtr.find_element_by_tag_name('a')
        urlList.append(a.get_attribute('href'))
driver.close()
fp = open('input.txt', 'w')
for url in urlList:
    fp.write(url + '\n')
fp.close()
