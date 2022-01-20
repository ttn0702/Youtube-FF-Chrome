from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from File_Class import *
import random
log = File_Interact('log.txt')

def run_thread(user_data_path,list_video,list_comment,time_start_delay,time_end_delay):
    chrome_name = user_data_path.split('\\')[-1]
    options = webdriver.ChromeOptions()
    # options.add_argument('--app=https://www.youtube.com/')
    options.add_argument(f'user-data-dir={user_data_path}')
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
    for i in range(len(list_video)):
        try:
            driver.get(list_video[i])
            WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tp-yt-paper-button[class="style-scope ytd-subscribe-button-renderer"]')))
            # Đăng kí kênh
            print(f'{chrome_name}: Đang đăng kí kênh...')
            log.write_file_line(f'{chrome_name}: Đang đăng kí kênh...')
            js = '''return document.querySelectorAll('div[id="subscribe-button"]')[1].innerText'''
            status_sub = driver.execute_script(js)
            if 'SUBSCRIBE' == status_sub or 'ĐĂNG KÝ' == status_sub:
                driver.find_elements_by_css_selector('div[id="subscribe-button"]')[1].click()

            # Like video
            log.write_file_line(f'{chrome_name}: Đang like video...')
            print(f'{chrome_name}: Đang like video...')
            WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'yt-icon[class="style-scope ytd-toggle-button-renderer"]')))
            js_like = '''return document.querySelectorAll('div[id="menu-container"]')[0].querySelectorAll('button[id="button"]')[0].ariaPressed'''
            isLike = driver.execute_script(js_like)
            if isLike == 'true':
                pass
            else:
                driver.find_elements_by_css_selector('yt-icon[class="style-scope ytd-toggle-button-renderer"]')[0].click()
                print('Like')
            time.sleep(2)

            # Phát video
            js_pause = '''return document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].title'''
            isPause = driver.execute_script(js_pause)
            if 'Pause (k)' == isPause or 'Tạm dừng (k)' == isPause:
                pass
            else:
                js_click_play = '''document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].click()'''
                driver.execute_script(js_click_play)

            driver.execute_script("window.scrollTo(0, 500)")
            # Tương tác
            log.write_file_line(f'{chrome_name}: Đang tương tác...')
            print(f'{chrome_name}: Đang tương tác...')
            js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
            time_end = driver.execute_script(js_time_end)
            time.sleep(random.randint(time_start_delay,time_end_delay-1))
            try:
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="style-scope ytd-comment-simplebox-renderer"]')))
                driver.find_elements_by_css_selector('div[class="style-scope ytd-comment-simplebox-renderer"]')[0].click()
                time.sleep(2)
                index = random.randint(0,len(list_comment)-1)
                driver.find_elements_by_css_selector('div[id="contenteditable-root"]')[0].send_keys(list_comment[index])
                print(f'{chrome_name}: - Bình luận: {list_comment[index]}')
                log.write_file_line(f'{chrome_name} bình luận: {list_comment[index]}')
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-button-renderer[id="submit-button"]')))
                driver.find_elements_by_css_selector('ytd-button-renderer[id="submit-button"]')[0].click()
            except:
                pass

            while True:
                
                try:
                    js_ads = '''document.querySelectorAll('div[class="ytp-ad-text ytp-ad-skip-button-text"]')[0].click()'''
                    driver.execute_script(js_ads)
                except:
                    pass
                time_delay = random.randint(time_start_delay,time_end_delay-1)
                print(f'{chrome_name} - time_delay: ',time_delay)
                time.sleep(time_delay)
                
                js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
                time_end = driver.execute_script(js_time_end)
                js_time_current = '''return document.querySelectorAll('span[class="ytp-time-current"]')[0].innerText'''
                time_current = driver.execute_script(js_time_current)

                # time1 = int(time_current.split(':')[0])*60 + int(time_current.split(':')[-1])
                if time_current == time_end:
                    log.write_file_line(f'{chrome_name}: Stop!')
                    print('Stop!')
                    break
                try:
                    driver.execute_script("window.scrollTo(0, 500)")
                    WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="style-scope ytd-comment-simplebox-renderer"]')))
                    driver.find_elements_by_css_selector('div[class="style-scope ytd-comment-simplebox-renderer"]')[0].click()
                    time.sleep(2)
                    index = random.randint(0,len(list_comment)-1)
                    driver.find_elements_by_css_selector('div[id="contenteditable-root"]')[0].send_keys(list_comment[index])
                    print(f'{chrome_name}: - Bình luận: {list_comment[index]}')
                    log.write_file_line(f'{chrome_name} bình luận: {list_comment[index]}')
                    WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-button-renderer[id="submit-button"]')))
                    driver.find_elements_by_css_selector('ytd-button-renderer[id="submit-button"]')[0].click()
                except:
                    pass
        except:
            pass
    driver.quit()
