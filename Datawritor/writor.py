

import os
import pandas as pd

class WriteAdaptor():

    @staticmethod
    def dict_el_list(**kwargs):
        for i in kwargs: 
            if not isinstance(kwargs[i], list):
                kwargs[i] = [kwargs[i]]
        
        return kwargs
    
    @staticmethod
    def to_dataframe(**kwargs) -> pd.DataFrame:
        kwargs = WriteAdaptor.dict_el_list(**kwargs)
        return pd.DataFrame(kwargs)
    
    @staticmethod
    def to_excel(df:pd.DataFrame,path:str):
        if os.path.isfile(path):
            d = pd.read_excel(path, index_col=None)
            df = pd.concat([d,df])

        print(df.head())
        df.to_excel(path, index=False)
    


if __name__ == "__main__":
    ed = {'me': 'azooz', 'her': 'mun', 'we': 'love'}
    edf = WriteAdaptor.to_dataframe(**ed)
    WriteAdaptor.to_excel(edf,'text.xlsx')
