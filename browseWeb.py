from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def main(driver):
    fp = open('input.txt')
    urlList = list()
    for each in fp:
        each = each.strip()
        urlList.append(each)
    fp.close()
    for url in urlList:
        driver.get(url)
        time.sleep(1)

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_extension('TrackingObserver.crx')
    driver = webdriver.Chrome(executable_path="C:\chrome\chromedriver.exe", chrome_options=chrome_options)
    try:
        main(driver)
    except KeyboardInterrupt:
        driver.close()

