from pywinauto.application import Application
import time
import re
# app = Application(backend="uia").start("C:\Program Files\ChatGPT\ChatGPT.exe")
# time.sleep(5)
# app = Application(backend='uia').connect(title=u'ChatGPT', top_level_only=True,ctrl_index=1)
# time.sleep(3)
# # app.CHATGPT.print_control_identifiers()
# print('_________________________________________________________')
# app.CHATGPT.type_keys('write suggestion names for shared offices, Note put them in graph not listing {ENTER}',with_spaces = True)
# time.sleep(30)
# # print(app.CHATGPT.GroupBox6.dump_tree())
# controls = app.CHATGPT.GroupBox6.children()
# for i in controls:
#     if i.friendly_class_name() == 'Static' or i.friendly_class_name() == 'ListBox':
#         if i.texts()[0].lower() == 'you' or i.texts()[0].lower() == 'chatgpt': 
#             continue
#         print(i.texts())
# app.kill()
# controls = app.find_elements(class_name="Static")
# app.CHATGPT.ChatGPT3.print_control_identifiers()
# print(app.CHATGPT.get_items())
# controls = app.CHATGPT.Pane.ChatGPT.ChatGPTWebContent.Pane.Pane.expand

# app.CHATGPT.print_control_identifiers()
# from pywinauto.application import Application
# app = Application().start("notepad.exe")

# app.UntitledNotepad.menu_select("Help->About Notepad")
# app.AboutNotepad.OK.click()
# app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)

# app = Application(backend="uia").start("notepad.exe")
# time.sleep(5)
# app = Application(backend='uia').connect(title=u'Untitled - Notepad', top_level_only=True,ctrl_index=1)
# app.UntitledNotepad.print_control_identifiers()
# wrapper_type = app.UntitledNotepad.wrapper_object()
# print(app.Notepad)
# print(app.top_window())
# print(app.windows())
# app.UntitledNotepad.draw_outline()
# app.UntitledNotepad.Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)
# app.UntitledNotepad.UntitledPane3.menu_select('File -> Exit')
# print(wrapper_type)

class ChatgptAPI():

    @staticmethod
    def inputs(app,text):
        text = text + '{ENTER}'
        app.CHATGPT.type_keys(text,with_spaces = True)

    @staticmethod
    def open_app():
        app = Application(backend="uia").start("C:\Program Files\ChatGPT\ChatGPT.exe")
        time.sleep(5)
        app = Application(backend='uia').connect(title=u'ChatGPT', top_level_only=True,ctrl_index=1)
        return app
    
    @staticmethod
    def info(app, func):
        controls = app.CHATGPT.GroupBox6.children()
        output = []
        flag = 0
        for i in controls:
            # print(i.friendly_class_name())
            # print(i.texts())
            # if i.friendly_class_name() == 'Static' or i.friendly_class_name() == 'ListBox':
            a = func(i)
            if '//' in a: 
                continue
            output.append(a)

        return ''.join(output[2:])
    
    @staticmethod
    def close(app):
        app.kill()


if __name__ == "__main__":
    from templete import word,create_message
    import sys
    sys.path.append(r'E:\joe13\the brain\Datawritor')
    sys.path.append(r'E:\joe13\the brain')
    from writor import WriteAdaptor
    from text_handler import TextHandler
    
    word = create_message(word)
    app = ChatgptAPI.open_app()
    ChatgptAPI.inputs(app,word)
    time.sleep(30)
    data = ChatgptAPI.info(app,lambda x : x.texts()[0])
    data = TextHandler.json_paraser(data)
    edf = WriteAdaptor.to_dataframe(**data)
    WriteAdaptor.to_excel(edf,'text.xlsx')

    print(data)
    # fas = '''
    # ChatGPTCertainly, here is the extracted information in JSON format:json{
    # "name": "Abdul Aziz",
    # "occupation": "Research Assistant in Sound Localization and AI, AI Engineer",
    # "phone": "^0164378902",
    # "age": null,  // Age information is not provided in the resume
    # "email": "aziz.alhaj25@gmail.com"
    # }
    # ChatGPT can make mistakes. Consider checking important information.
    # '''
    # ChatgptAPI.json_paraser(fas)
    ChatgptAPI.close(app)



        