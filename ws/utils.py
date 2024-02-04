import hashlib
import datetime

DAY_NAME_TO_WEEKDAY = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
class DataHandler():

    @staticmethod
    def hash_element(element):
        return hashlib.md5(element.encode()).hexdigest()
    
    @staticmethod
    def remove_duplicates_hashing(list1: list, list2: list)-> list:
        if not isinstance(list1[0],str) or not isinstance(list2[0],str): 
            list1 = list(map(str,list1))
            list2 = list(map(str,list2))

        list1_hash = [*map(DataHandler.hash_element, list1)]
        list2_hash = [*map(DataHandler.hash_element, list2)]

        for index, i in enumerate(list2_hash): 
            if i in list1_hash: 
                print(i)
                continue
            else: 
                list1.append(list2)
        return list1

    @staticmethod
    def remove_duplicates_set(list1: list) -> list:
        if not isinstance(list1,str): 
            list1 = list(map(str,list1))
        return list(set(list1))
    

    @staticmethod
    def convert2day_name(date):
        d,m,y = date.split('/')
        today_date = datetime.date(int(y), int(m), int(d))
        day_name = today_date.strfindextime("%A")
        return day_name

    @staticmethod
    def calculate_date_diff(date):
        today = datetime.datetime.now().today().date()
        d,m,y = date.split('/')
        other_days = datetime.date(int(y), int(m), int(d))
        return (today - other_days).days
    
    @staticmethod
    def range_dates(day,days, data_format='date2days'):
        dates_range = [day]+[day - datetime.timedelta(days=i+1) for i in range(days)]
        if data_format == 'date2days':
            for index,i in enumerate(dates_range):
                if index == 0:
                    dates_range[index] = "Today"
                elif index == 1:
                    dates_range[index] = "Yesterday"
                elif index in [2,3,4,5,6]:
                    dates_range[index] = handler.convert2day_name(i.strftime(r"%d/%m/%Y"))
                else:
                    dates_range[index] = i.strftime(r"%d/%m/%Y")

        return dates_range

    @staticmethod
    def convert_2_date(date): 
        if '/' in date: 
            return date
        
        current_date =  datetime.datetime.now()
        if 'Am' in date or 'Pm' in date: 
            return current_date.date().strftime("%d/%m/%Y")
        
        if 'Yesterday' in date: 
            date = current_date.date() - datetime.timedelta(days=1)
            return date.strftime("%d/%m/%Y")
            
        day_name = current_date.strftime("%A")
        current_weekday = DAY_NAME_TO_WEEKDAY[day_name]
        desired_weekday = DAY_NAME_TO_WEEKDAY[date]
        days_difference = current_weekday - desired_weekday
        
        if days_difference < 0:
            days_difference+= len(DAY_NAME_TO_WEEKDAY)
        date = current_date.date() - datetime.timedelta(days=days_difference)
        return date.strftime("%d/%m/%Y")

    @staticmethod
    def passed_theDate(goal_date, date):
        if isinstance(goal_date, str):
            d,m,y = goal_date.split('/')
            goal_date = datetime.datetime(int(y),int(m),int(d))
            goal_date = goal_date.date()

        if isinstance(date, str): 
            d,m,y = date.split('/')
            date = datetime.datetime(int(y),int(m),int(d))
            date = date.date()

        # print(date)
        # print(goal_date + datetime.timedelta(days=1), goal_date - datetime.timedelta(days=1))
        # goal_date - datetime.timedelta(days=1) <= date <= goal_date + datetime.timedelta(days=1)
        return goal_date <= date

if __name__ == '__main__':
    handler = DataHandler()
    days = handler.calculate_date_diff('20/09/2023')
    # day = datetime.datetime.now().today().date()
    # dates = handler.range_dates(day,days)
    # dates = handler.convert_2_date('Monday')
    # print(dates)