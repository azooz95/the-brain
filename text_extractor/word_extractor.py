import docx2txt

class DocxInfoExtractor():

    @staticmethod
    def docx_extractor(file):
        text = docx2txt.process(file).replace('\n', ' ')
        return text
    
    @classmethod
    def run(cls, file):
        text = cls.docx_extractor(file)
        return text



if __name__ == "__main__":
    word_path = '../data/Last_Version_Resume.docx'
    print(DocxInfoExtractor.run(word_path))