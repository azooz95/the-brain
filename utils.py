import os 
import glob

class Utils():
    @staticmethod
    def create_folder(path):
        try:
            os.mkdir(path)
        except:
            pass 

        return path

    @staticmethod
    def move_file(old_file,new_file,extensions):
        for extension in extensions:
            files = glob.glob(os.path.join(old_file,"*"+extension))
            print(files)
            for file_ in files:
                name = os.path.basename(file_)
                new_name = os.path.join(new_file, name)
                try:
                    os.replace(file_,new_name)
                    os.remove(file_)
                except FileNotFoundError: 
                    pass
                except PermissionError:  
                    raise("File is working or not existed")

    @staticmethod
    def rearange_files(path,imgs=True, pdfs=True):
        imgs_extenstion = ['.png', '.jpg', 'jpeg']
        pdfs_extension = '.pdf'

        if imgs: 
            img_path = Utils.create_folder(os.path.join(path, 'images'))
            Utils.move_file(path, img_path, imgs_extenstion)

        if pdfs: 
            pdf_path = Utils.create_folder(os.path.join(path, 'pdfs'))
            Utils.move_file(path, pdf_path, pdfs_extension)


if __name__ == '__main__':
    Utils.rearange_files(r'D:\Downloads')

