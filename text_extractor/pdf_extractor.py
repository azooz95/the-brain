
class PdfInfoExtrator:

    @staticmethod
    def pdf_reader(path: str):
        return PdfReader(path)
    
    @staticmethod
    def info_extractor(file: PdfReader):
        text = ""
        for page in file.pages:
            text += page.extract_text()

        return text

    @classmethod
    def run(cls, path):
        reader = cls.pdf_reader(path)
        return cls.info_extractor(reader)

    

if __name__ == "__main__":
    pdf_path = '../data/Abdulaziz_updated_cv_V3.pdf'
    print(PdfInfoExtrator.run(pdf_path))