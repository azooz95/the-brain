import sys
import time
import os
sys.path.append("../web_controller")
from web import OpenWeb

class EmailHandler():


    @staticmethod
    def download_wait(directory, timeout, nfiles=None):
        """
        Wait for downloads to finish with a specified timeout.

        Args
        ----
        directory : str
            The path to the folder where the files will be downloaded.
        timeout : int
            How many seconds to wait until timing out.
        nfiles : int, defaults to None
            If provided, also wait for the expected number of files.

        """
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
            time.sleep(1)
            dl_wait = False
            files = os.listdir(directory)
            if nfiles and len(files) != nfiles:
                dl_wait = True

            for fname in files:
                if fname.endswith('.crdownload'):
                    dl_wait = True

            seconds += 1
        return seconds
    
    @staticmethod
    def donwload_resume(links, download_path = r'D:\Downloads'):

        app = OpenWeb(download_path=download_path)
        driver = app()
        for link in links:
            app.open_browser(link)
            driver.click(text='Download')
            EmailHandler.download_wait(download_path,20)
        app.close()




