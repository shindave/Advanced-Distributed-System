from selenium import webdriver
import time
from collections import defaultdict
import pickle

def main(driver):
    save_cookie_name = 'data/ghostery_cookies.p'
    fp = open('input.txt')
    cookie_list = []
    urlList = list()
    for each in fp:
        each = each.strip()
        urlList.append(each)
    fp.close()
    count = 0
    sum = len(urlList)
    for url in urlList:
        try:
            print str(count)+'/'+str(sum)
            driver.get(url)
            cookies = driver.get_cookies()
            for cookie in cookies:
                print cookie
                cookie_list.append(cookie)
                pfile = open(save_cookie_name, 'wb')
                pickle.dump(cookie_list, pfile)
                pfile.close()
        except:
            pass
        count += 1
        time.sleep(1)

if __name__ == '__main__':
    # This part below is for firefox
    fp = webdriver.FirefoxProfile()
    fp.add_extension(extension='fourthparty.xpi')
    #fp.add_extension(extension='donottrackme-4.5.1334-fx.xpi')
    fp.add_extension(extension='ghostery.xpi')
    #fp.add_extension(extension='privacy_badger.xpi')
    #fp.add_extension(extension='trackerblock.xpi')
    #fp.add_extension(extension='disconnect.xpi')
    #fp.add_extension(extension='adblock_plus.xpi')
    driver = webdriver.Firefox(firefox_profile=fp)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)

    try:
        main(driver)
    except KeyboardInterrupt:
        driver.close()
    driver.close()

