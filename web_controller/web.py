import time
from typing import Any
from webbot import Browser

class OpenWeb():
    def __init__(self, driver=None, download_path = None) -> None:
        self.driver = Browser(downloadPath=download_path)    
    
    def open_browser(self, url):
        self.driver.go_to(url)
        time.sleep(1) # to complete loading

    def action(self, method):
        method()

    def close(self):
        self.driver.quit()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.driver


if __name__ == '__main__':
    driver = Browser()