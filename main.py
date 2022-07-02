from time import sleep
from selenium import webdriver


def xform(xpath,txt):
    texts = driver.find_element_by_xpath(xpath)
    texts.clear()
    texts.send_keys(txt)
def xclick(xpath):
    driver.find_element_by_xpath(xpath).click()

driver = webdriver.Chrome()

def sakana():
    driver.delete_all_cookies()
    sleep(0.1)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election01.php")
    sleep(0.1)
    xclick('//*[@id="election"]/div[2]/ul[1]/li[4]/a')
    sleep(0.1)
    xclick('//*[@id="vote"]')
    sleep(0.1)
def wagasi():
    driver.delete_all_cookies()
    sleep(0.1)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election03.php")
    sleep(0.1)
    xclick('//*[@id="election"]/div[2]/ul/li[3]/a')
    sleep(0.1)
    xclick('//*[@id="vote"]')
    sleep(0.1)
def bergl():
    driver.delete_all_cookies()
    sleep(0.1)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election02.php")
    sleep(0.1)
    xclick('//*[@id="election"]/div[2]/ul[1]/li[4]/a')
    sleep(0.1)
    xclick('//*[@id="vote"]')
    sleep(0.1)
input("数量")
for i in range(1000):
    sakana()
    wagasi()
    bergl()
