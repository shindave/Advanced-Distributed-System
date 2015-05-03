from selenium import webdriver
import time


def main(driver):
    fp = open('input.txt')
    cookie_list = open()
    urlList = list()
    for each in fp:
        each = each.strip()
        urlList.append(each)
    fp.close()
    for url in urlList:
        try:
            driver.get(url)
            print driver.get_cookies()
        except:
            pass
        time.sleep(1)

if __name__ == '__main__':
    '''
    chrome_options = Options()
    chrome_options.add_extension('floodwatch.crx')
    chrome_options.add_extension('disconnected.crx')
    driver = webdriver.Chrome(executable_path="C:\chrome\chromedriver.exe", chrome_options=chrome_options)
    '''
    # This part below is for firefox
    fp = webdriver.FirefoxProfile()
    fp.add_extension(extension='donottrackme-4.5.1334-fx.xpi')
    fp.add_extension(extension='fourthparty.xpi')
    # fp.add_extension(extension='privacy_badger.xpi')
    # fp.add_extension(extension='disconnect.xpi')
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)

    try:
        main(driver)
    except KeyboardInterrupt:
        driver.close()
    driver.close()

