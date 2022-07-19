# ほどよくスペースを挟む
# 不要なスペースや改行は削除

from time import sleep, time  # from ~~~ からの import は 1 つにまとめる
from selenium import webdriver


def xform(xpath, txt):  # トップレベルに書く def 等は 2 つ改行をする
    texts = driver.find_element_by_xpath(xpath)
    texts.clear()
    texts.send_keys(txt)


def xclick(xpath):
    driver.find_element_by_xpath(xpath).click()


def to(seconds):
    seconds = int(seconds + 0.5)
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    
    return f"{h:02}:{m:02}:{s:02}"


def touhu():
    driver.delete_all_cookies()
    sleep(0.03)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election01.php")
    sleep(0.03)
    xclick('//*[@id="election"]/div[2]/ul[1]/li[7]/a')
    sleep(0.03)
    xclick('//*[@id="vote"]')
    sleep(0.03)


def ringo():
    driver.delete_all_cookies()
    sleep(0.03)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election02.php")
    sleep(0.03)
    xclick('//*[@id="election"]/div[2]/ul[1]/li[2]/a')
    sleep(0.03)
    xclick('//*[@id="vote"]')
    sleep(0.03)


def wagasi():
    driver.delete_all_cookies()
    sleep(0)
    driver.get("https://iwebms.com/cp/summit_sousenkyo/election03.php")
    sleep(0.03)
    xclick('//*[@id="election"]/div[2]/ul/li[3]/a')
    sleep(0.03)
    xclick('//*[@id="vote"]')
    sleep(0.03)


def nokori(ind, maxed):
    e = str(round(ind / maxed * 100, 2))
    nokor = maxed - ind
    ind = str(ind)
    maxed = str(maxed)
    byo = time() - start
    
    if byo == 0:
        byo = 0.1
        
    ikai = byo / (int(ind) + 1)
    errri = "エラー率:" + str(round(err / (int(ind) + 1) * 100, 2)) + "%"
    byosoku = str(round(1 / ikai, 2)) + "票/s"
    nokobyo = "残り約" + to(ikai * nokor) + "s"
    
    return [ind + "/" + maxed, byosoku, e + "%", errri, nokobyo]


err = 0
start = time()
num = int(input("数量"))  # 変数名 l は曖昧で "l" なのか "I" なのか "1" なのか分かりにくい
driver = webdriver.Chrome()

for i in range(num):
    print(" ".join(nokori(i, num)))
    # print(i+1)
    
    try:
        ringo()
        touhu()

# 素の except は使用せず、"except Exception" のように書く - これでも範囲が広すぎるため、例外の名前が分かれば書く
        err += 1
        print("er")
