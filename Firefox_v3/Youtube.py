'''
    Version 3:
    - Chuyển đổi Profile khi xem hết video trong list comment
'''
from utils import *
from File_Class import *
import threading

list_comment = File_Interact('./data/list_comment.txt').read_file_list()
list_video = File_Interact('./data/list_video.txt').read_file_list()
list_user_data_path = File_Interact('./data/user_data_path.txt').read_file_list()
config = File_Interact('config.txt').read_file_list()
time_start = int(config[0].split('=')[-1])
time_end = int(config[1].split('=')[-1])
thread = int(config[2].split('=')[-1])
log = File_Interact('log.txt')

log.write_file_line('====================================================')
# thread = 2
count = 0
while True:
    if count >= len(list_user_data_path):
        count = 0
    for i in range(count,count + thread):
        try:
            t = threading.Thread(target=run_thread, args=(list_user_data_path[i],list_video,list_comment,time_start,time_end,))
            t.start()
            print('i : ',i+1)
        except:
            pass
    t.join()
    count = count + thread