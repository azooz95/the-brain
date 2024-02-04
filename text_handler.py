
from langdetect import detect
from enums import langauge
from translate import Translator
import re
class TextHandler:

    @staticmethod
    def lang_detector(text):
        return detect(text)
    
    @staticmethod
    def convert_2_arabic(text):
        return text[::-1]
    
    @staticmethod
    def translate(text):
        lang = TextHandler.lang_detector(text[:1000]) 
        if lang != langauge.en.name:
            translator = Translator(to_lang="en", from_lang="ar")
            text = translator.translate(text)
        
        return text
    
    @staticmethod
    def json_paraser(texts):
        result = re.findall(r'{[^{}]*}', texts)[0]
        result = result.replace('\n', '')
        # result = re.sub(r'//[^"]*$', '', result, flags=re.MULTILINE)
        result = result.replace('null', 'None')
        try: 
            result = eval(result)
        except: 
            result = re.sub(r'//[^"]*$', '', result, flags=re.MULTILINE)
            result = eval(result)

        return result

if __name__ == "__main__":
    print(TextHandler.translate("انا لست انسان"))
