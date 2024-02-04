import re
from typing import Any 


class test():
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return 1
    
    def printtt(self):
        print(True)
    

a = test()
print(a.printtt())