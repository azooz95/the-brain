import os 
from alright import WhatsApp
from selenium.webdriver.common.by import By
import pandas as pd
from utils import DataHandler

import time 

# messenger = WhatsApp(time_out=2000)

# messenger.get_first_chat()
# time.sleep(3)
# # messenger.find_attachment()
# # names = messenger.fetch_all_unread_chats(top=5)
# data = messenger.get_list_of_messages()
# print(data)
# time.sleep(5)

DOWNLOAD_PATH = {'download.default_directory' : 'D:\Downloads'}
class WhatsappReceiving(WhatsApp):

    def __init__(self):
        self.downlaod_path = DOWNLOAD_PATH
        super().__init__(self.downlaod_path)
        
    def get_info_users(self, up_todate, iterations=10):
        # an occure may be raise because, set operation is used to delete deplucate elements
        
        data_tmp = []
        counter = 0
        all_data = []
        element = self.browser.find_element(By.ID, 'pane-side')
        initial_h = self.browser.execute_script("return document.body.scrollHeight;", element)
        high = initial_h//2
        while True: 
            data, is_in_range = self.get_list_of_messages(up_todate)
            print(data, is_in_range)

            if iterations < counter: 
                print(True)
                break

            counter+=1
            
            if not is_in_range:
                continue

            high = self.scrol_down_by_elements(element,high=high, precentage=0.5)
            high+=initial_h*0.3
            # if high == False: 
            #     return all_data
            
            time.sleep(2)
            all_data.extend(data)
            data_tmp = data
            all_data = DataHandler.remove_duplicates_set(all_data)

            # if not is_in_range: 
            #     break
        
        return all_data
    
    def downlaod_info(self, up_todate):
        data = self.get_info_users(up_todate)
        
        for i in data: 
            i = eval(i)
            username = i['sender']
            self.find_by_username(username)
            self.download_all_imgs_pdfs_chat()
            time.sleep(3)

    def get_number_by_search_contectext(self,up_todate='16/11/2023', text='ان شاءالله موعد المقابله الثانية والاخيرة'):
        self.find_by_username(text)
        time.sleep(3)
        contacts = self.get_info_users(up_todate, iterations=130)

        for i in contacts: 
            print(i)
            i = eval(i)
            time_ = i['time'][:2]
            print(time_)
            if time_ == '17' or time_ == '16':
                number = i['sender'][4:].replace(" ","")
                with open('already_sent_1.txt', 'a', encoding='utf-8') as f: 
                    f.write(f'{number}\n')

        

class WriteAdapter():

    @staticmethod
    def read_database(path):
        if os.path.exists(path):
            data = pd.read_csv(path)
            return data
        else: 
            data = {
                'name' : [],
                'time' : [],
                'date' : []
            }
            df = pd.DataFrame(data)
            df.to_csv(path,index=False)
            return data
        
    @staticmethod
    def write_into_dp(dp,path):
        dp.to_csv(path,index=False)
    
    @staticmethod
    def insert_to_dp(dp, **info):

        if not dp.columns.to_list() == list(info.keys()):
            raise ValueError("columns not match with dictionary value")
        dp = pd.concat([dp, pd.DataFrame(info)], ignore_index=True)
        return dp
    

if __name__ == "__main__":
    download_path = {'download.default_directory' : 'D:\Downloads'}
    # path = os.path.join(download_path['download.default_directory'], 'test1.csv')
    # dp = WriteAdapter.read_database(path)
    # demo = {
    #     "name": ["test"],
    #     'time': ['1255'],
    #     'date': ['1233']
    # }
    # print(type(dp))
    # dp = WriteAdapter.insert_to_dp(dp,**demo)
    # WriteAdapter.write_into_dp(dp,path)
    # dp = WriteAdapter.read_database(path)
    # print(dp)
    # time_to = '10/08/2023'
    ws = WhatsappReceiving()
    time.sleep(30)
    all_data = ws.get_info_users('30/12/2023',iterations=10)
    print(all_data)
    # print(all_data)
    for i in all_data: 
        i = eval(i)
        username = i['sender']
        ws.find_by_username(username)
        ws.download_all_imgs_pdfs_chat()
        time.sleep(3)
    # time.sleep(3)
    # ws.get_number_by_search_contectext()
    
    # def get_users_info(self):



