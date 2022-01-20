from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from func import *
from File_Class import *
import random
log = File_Interact('log.txt')

def run_thread(user_data_path,list_video,list_comment,time_start_delay,time_end_delay):
    chrome_name = user_data_path.split('\\')[-1].split('.')[-1]
    fp = webdriver.FirefoxProfile(user_data_path)
    driver = webdriver.Firefox(fp)
    driver.maximize_window()
    # driver.get(url)

    for i in range(len(list_video)):
        try:
            error_video = 0
            count = 0
            isLikeSub = 0
            check_count = random.randint(1,2)
            driver.get(list_video[i])
            driver.execute_script("window.scrollTo(0, 500)")
            try:
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="style-scope ytd-comment-simplebox-renderer"]')))
                driver.find_elements_by_css_selector('div[class="style-scope ytd-comment-simplebox-renderer"]')[0].click()
                print('click')
            except:
                pass
            time.sleep(2)
            # Phát video
            js_pause = '''return document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].title'''
            isPause = driver.execute_script(js_pause)
            print(isPause)
            if 'Pause (k)' == isPause or 'Tạm dừng (k)' == isPause:
                pass
            else:
                js_click_play = '''document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].click()'''
                driver.execute_script(js_click_play)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            # Tương tác
            log.write_file_line(f'{chrome_name}: Đang tương tác...')
            print(f'{chrome_name}: Đang tương tác...')
            js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
            time_end = driver.execute_script(js_time_end)
            time_delay = random.randint(time_start_delay,time_end_delay-1)
            for index_time in range(time_delay):
                #check ket thuc video
                js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
                time_end = driver.execute_script(js_time_end)
                js_time_current = '''return document.querySelectorAll('span[class="ytp-time-current"]')[0].innerText'''
                time_current = driver.execute_script(js_time_current)
                if time_current == time_end:
                    log.write_file_line(f'{chrome_name}: Stop!')
                    print('Stop!')
                    break
                else:
                    if time_current == '0:00':
                        error_video += 1
                    if error_video == 100:
                        break
                    time.sleep(1)
            try:
                try:
                    WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="style-scope ytd-comment-simplebox-renderer"]')))
                    driver.find_elements_by_css_selector('div[class="style-scope ytd-comment-simplebox-renderer"]')[0].click()
                except:
                    pass
                time.sleep(2)
                index = random.randint(0,len(list_comment)-1)
                driver.find_elements_by_css_selector('div[id="contenteditable-root"]')[0].send_keys(list_comment[index])
                print(f'{chrome_name}: - Bình luận: {list_comment[index]}')
                log.write_file_line(f'{chrome_name} bình luận: {list_comment[index]}')
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-button-renderer[id="submit-button"]')))
                driver.find_elements_by_css_selector('ytd-button-renderer[id="submit-button"]')[0].click()
            except:
                # pass
                print('loi')
            while True:
                try:
                    js_ads = '''document.querySelectorAll('div[class="ytp-ad-text ytp-ad-skip-button-text"]')[0].click()'''
                    driver.execute_script(js_ads)
                except:
                    pass
                
                try:
                    # Phát video
                    js_pause = '''return document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].title'''
                    isPause = driver.execute_script(js_pause)
                    print(isPause)
                    if 'Pause (k)' == isPause or 'Tạm dừng (k)' == isPause:
                        pass
                    else:
                        js_click_play = '''document.querySelectorAll('div[class="ytp-left-controls"]')[0].querySelectorAll('button[class="ytp-play-button ytp-button"]')[0].click()'''
                        driver.execute_script(js_click_play)
                    time.sleep(2)
                except:
                    pass


                time_delay = random.randint(time_start_delay,time_end_delay-1)
                print(f'{chrome_name} - time_delay: ',time_delay)
                for index_time in range(time_delay):
                    #check ket thuc video
                    js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
                    time_end = driver.execute_script(js_time_end)
                    js_time_current = '''return document.querySelectorAll('span[class="ytp-time-current"]')[0].innerText'''
                    time_current = driver.execute_script(js_time_current)
                    if time_current == time_end:
                        log.write_file_line(f'{chrome_name}: Stop!')
                        print('Stop!')
                        break
                    else:
                        if time_current == '0:00':
                            error_video += 1
                        if error_video == 100:
                            break
                        time.sleep(1)

                
                #check ket thuc video
                js_time_end = '''return document.querySelectorAll('span[class="ytp-time-duration"]')[0].innerText'''
                time_end = driver.execute_script(js_time_end)
                js_time_current = '''return document.querySelectorAll('span[class="ytp-time-current"]')[0].innerText'''
                time_current = driver.execute_script(js_time_current)
                if time_current == '0:00':
                    error_video += 1
                if error_video == 100:
                    break
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
                    count +=1
                    if count == check_count and isLikeSub == 0:
                        # Like video
                        log.write_file_line(f'{chrome_name}: Đang like video...')
                        print(f'{chrome_name}: Đang like video...')
                        WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'yt-icon[class="style-scope ytd-toggle-button-renderer"]')))
                        js_like = '''return document.querySelectorAll('div[id="menu-container"]')[0].querySelectorAll('button[id="button"]')[0].getAttribute('aria-pressed')'''
                        isLike = driver.execute_script(js_like)
                        print('isLike: ',isLike)
                        if isLike == 'false':
                            driver.find_elements_by_css_selector('yt-icon[class="style-scope ytd-toggle-button-renderer"]')[0].click()
                            print('Like')
                            isLikeSub = 1
                        elif isLike == 'true':
                            isLikeSub = 1
                        else:
                            pass
                        time.sleep(random.randint(10,20))
                        # Đăng kí kênh
                        print(f'{chrome_name}: Đang đăng kí kênh...')
                        log.write_file_line(f'{chrome_name}: Đang đăng kí kênh...')
                        js = '''return document.querySelectorAll('div[id="subscribe-button"]')[1].innerText'''
                        status_sub = driver.execute_script(js)
                        if 'SUBSCRIBE' == status_sub or 'ĐĂNG KÝ' == status_sub:
                            driver.find_elements_by_css_selector('div[id="subscribe-button"]')[1].click()
                except:
                    pass
            if error_video == 100:
                for index_replay in range(0,5):
                    url = list_video[i]
                    replay = func(driver,chrome_name,url,list_comment,time_start_delay,time_end_delay)
                    if replay:
                        break
                    else:
                        time.sleep(2)
            if isLikeSub == 0:
                # Like video
                log.write_file_line(f'{chrome_name}: Đang like video...')
                print(f'{chrome_name}: Đang like video...')
                WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'yt-icon[class="style-scope ytd-toggle-button-renderer"]')))
                js_like = '''return document.querySelectorAll('div[id="menu-container"]')[0].querySelectorAll('button[id="button"]')[0].getAttribute('aria-pressed')'''
                isLike = driver.execute_script(js_like)
                if isLike == 'false':
                    driver.find_elements_by_css_selector('yt-icon[class="style-scope ytd-toggle-button-renderer"]')[0].click()
                    isLikeSub = 1
                    print('Like')
                elif isLike == 'true':
                    isLikeSub = 1
                else:
                    pass
                time.sleep(random.randint(10,20))
                # Đăng kí kênh
                print(f'{chrome_name}: Đang đăng kí kênh...')
                log.write_file_line(f'{chrome_name}: Đang đăng kí kênh...')
                js = '''return document.querySelectorAll('div[id="subscribe-button"]')[1].innerText'''
                status_sub = driver.execute_script(js)
                if 'SUBSCRIBE' == status_sub or 'ĐĂNG KÝ' == status_sub:
                    driver.find_elements_by_css_selector('div[id="subscribe-button"]')[1].click()
            else:
                pass
        except:
            pass
    driver.quit()
