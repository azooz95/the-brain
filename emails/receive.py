import imaplib
from datetime import datetime
import mailparser
from bs4 import BeautifulSoup

IMAP_SERVER = 'joe13th.com'
class EmailReciver():
    def __init__(self, email_address='aabdoh@joe13th.com', password='aabdohaijoe13') -> None:
        self.email_address = email_address
        self.password = password
        self.mail = self.login()

    def login(self):
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(self.email_address, self.password)
        return mail

    def filter_emails(self, message, from_='indeed'):
        sender = message.from_[0][1]
        if from_ in sender: 
            return True
        else: 
            return False
    
    def extract_link(self, message):
        body = message.body
        soup = BeautifulSoup(body, 'html.parser')
        links = soup.find_all(lambda tag: tag.name == 'a' and 'lid=public-resume' in tag.get('href', ''))
        if not links:
            return False
        return links[0].get('href', '')

    def get_emails(self, from_ = None, to_= None, email=None):

        if to_ is None: 
            to_ = datetime.now().date().strftime('%d/%m/%Y')

        
        d1,m1,y1 = from_.split('/')
        d2,m2,y2 = to_.split('/')
        start_time = datetime(int(y1), int(m1), int(d1))  # Replace with your start time
        end_time = datetime(int(y2), int(m2), int(d2))

        search_criteria = f'(SINCE "{start_time.strftime("%d-%b-%Y")}" BEFORE "{end_time.strftime("%d-%b-%Y")}" FROM "{email}")'

        self.mail.select('inbox')
        result, email_ids = self.mail.search(None, search_criteria)
        return result, email_ids
    
    def email_info_extractor(self, from_='1/10/2023', to_='4/10/2023', email = "indeed"):
        result,email_ids = self.get_emails(from_ = from_, to_=to_, email=email)
        links = []
        print(email_ids)
        if result == 'OK':
            if len(email_ids) == 1:
                email_ids = email_ids[0].decode('utf-8')
                email_ids = email_ids.split(" ")

            for email_id in email_ids:
                result, message_data = self.mail.fetch(email_id, '(RFC822)')
                if result == 'OK':
                    message = mailparser.parse_from_bytes(message_data[0][1])
                    # is_email = self.filter_emails(message)
                    
                    link = self.extract_link(message)
                    if not link: continue
                    links.append(link)

        return links
    
if __name__ == "__main__":
    email_r = EmailReciver()
    links = email_r.email_info_extractor()
    from email_handler import EmailHandler
    EmailHandler.donwload_resume(links)
    print(links)
