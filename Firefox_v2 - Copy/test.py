from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scroll_tab(driver):
    for i in range(20):
        js = '''return document.querySelectorAll('div[class="css-1dbjc4n r-1niwhzg r-18u37iz"]').length'''
        len_ele = driver.execute_script(js)
        for i in range(len_ele):
            js = f'''return document.querySelectorAll('div[class="css-1dbjc4n r-1niwhzg r-18u37iz"]')[{i}].innerText'''
            text = driver.execute_script(js)
            if text == 'Read post':
                vt = i
                break
        if vt != -1:
            break
        time.sleep(1)

user_data_path = r'C:\Users\trung\AppData\Roaming\Mozilla\Firefox\Profiles\i5fxnhaz.P1'
# chrome_name = user_data_path.split('\\')[-1].split('.')[-1]
fp = webdriver.FirefoxProfile(user_data_path)
driver = webdriver.Firefox(fp)
list_href = []
reload_number = 3
try:
    driver.get("https://lunarcrush.com/markets?metric=social_volume")
    # WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="css-4rbku5 css-1dbjc4n r-1loqt21 r-eqz5dr r-nsbfu8 r-1otgn73 r-1i6wzkk r-lrvibr"]')))
    WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-901oao r-1q4o75h r-1ui5ee8"]')))
    driver.find_elements_by_css_selector('div[class="css-901oao r-1q4o75h r-1ui5ee8"]')[0].click()
    print('click')
except:
    pass
check = 0

while True:
    js_coin = '''return document.querySelectorAll('a[class="css-4rbku5 css-1dbjc4n r-1loqt21 r-eqz5dr r-nsbfu8 r-1otgn73 r-1i6wzkk r-lrvibr"]').length'''
    len_coin = driver.execute_script(js_coin)
    print(len_coin)
    if len_coin > 35:
        check = 0
        break
    else:
        check += 1
        time.sleep(2)
    if check == 30:
        break

option_success = 0
for i in range(len_coin):
    WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a[class="css-4rbku5 css-1dbjc4n r-1loqt21 r-eqz5dr r-nsbfu8 r-1otgn73 r-1i6wzkk r-lrvibr"]')))
    href = driver.find_elements_by_css_selector('a[class="css-4rbku5 css-1dbjc4n r-1loqt21 r-eqz5dr r-nsbfu8 r-1otgn73 r-1i6wzkk r-lrvibr"]')[i].get_attribute('href')
    list_href.append(href)
    print('i')
for i in range(len(list_href)):
    driver.get(list_href[i])
    try:
        WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[name="question"]')))
        time.sleep(2)
        js_len_question = '''return document.querySelectorAll('svg[name="question"]').length'''
        len_question = driver.execute_script(js_len_question)
        if len_question != 0:
            js_option = '''return document.querySelectorAll('div[data-cssclass="button"]').length'''
            len_option = driver.execute_script(js_option)
            for index_option in range(len_option):
                js_button = f'''return document.querySelectorAll('div[data-cssclass="button"]')[{index_option}].innerText'''
                name = driver.execute_script(js_button)
                if name == 'Buy':
                    js_click_button = f'''document.querySelectorAll('div[data-cssclass="button"]')[{index_option}].click()'''
                    driver.execute_script(js_click_button)
                    print('OK')
                    time.sleep(3)
                    option_success += 1
                    break
    except:
        pass
    if option_success == 35:
        print(option_success)
        break
so_lan_lap = reload_number
count_end = 0
for i in range(so_lan_lap):
    count_end += 1
    try:
        driver.get("https://lunarcrush.com/")
        WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-901oao r-gs8g7 r-1inkyih r-1vr29t4"]')))
        driver.find_elements_by_css_selector('div[class="css-901oao r-gs8g7 r-1inkyih r-1vr29t4"]')[0].click()
        for i in range(0,4):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
        for i in range(0,4):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
            time.sleep(3)
        try:
            WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-901oao css-cens5h r-1q4o75h r-fpv9pr r-1enofrn"]')))
            driver.find_elements_by_css_selector('div[class="css-901oao css-cens5h r-1q4o75h r-fpv9pr r-1enofrn"]')[0].click()
            scroll_tab(driver)
        except:
            print('NN')
        for i in range(0,4):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
        for i in range(0,4):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
            time.sleep(3)

        for i in range(3):
            try:
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-cssclass="button-nextprev"]')))
                driver.find_elements_by_css_selector('div[data-cssclass="button-nextprev"]')[1].click()
            except:
                print('NN')
            scroll_tab(driver)
        driver.refresh()
        if count_end == 4:
            count_end = 0
            driver.get('https://lunarcrush.com/account/points')
            js = '''return document.querySelectorAll('div[class="css-901oao r-1q4o75h r-gs8g7 r-1b43r93 r-1vr29t4"]')[1].innerText'''
            point = driver.execute_script(js)
            if point == '60':
                driver.quit()
            else:
                pass
        time.sleep(5)
    except:
        print('Next')
driver.quit()