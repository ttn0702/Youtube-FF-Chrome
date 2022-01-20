from utils1 import *
from File_Class import *
import threading

list_comment = File_Interact('./data/list_comment.txt').read_file_list()
list_video = File_Interact('./data/list_video.txt').read_file_list()
list_user_data_path = File_Interact('./data/user_data_path.txt').read_file_list()
config = File_Interact('config.txt').read_file_list()
time_start = int(config[0].split('=')[-1])
time_end = int(config[1].split('=')[-1])
log = File_Interact('log.txt')

log.write_file_line('====================================================')
if len(list_user_data_path)<1:
    print('So luong proxy khong du')
    log.write_file_line('So luong proxy khong du')
else:
    for i in range(len(list_user_data_path)):
        t = threading.Thread(target=run_thread, args=(list_user_data_path[i],list_video,list_comment,time_start,time_end,))
        t.start()
        time.sleep(3)
    t.join()
    print('Done!')

log.write_file_line('====================================================')