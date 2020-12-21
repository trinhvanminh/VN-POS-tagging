
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import CRF_tagger



  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened

def Show_result(result):
    root = Tk()
    text=Text(root)
    for i in range(len(result)):
        text.insert(INSERT,result[i]+'\n')
    text.pack()


def open_file(): 
    file_name = askopenfilename(filetypes =[('Text Files', '*.txt')]) 
    file = open(file_name, 'r', encoding='utf-8')
    if file is not None: 
        content = file.read() 
        sen_list = CRF_tagger.sentence_tokenizer(content)
        result = [CRF_tagger.sen_tagger(i) for i in sen_list]
        Show_result(result)




def input_sen():
    root = Tk()
    root.title("Sentence")
    canvas = Canvas(root, width = 300, height = 50)
    canvas.pack()
    source_input = Entry(root) 
    canvas.create_window(150,25, width = 280, height = 30, window=source_input)
    btn_sen_tagger=Button(root, text ='Tagger', command = lambda:Show_result([CRF_tagger.sen_tagger(source_input.get())]))
    btn_sen_tagger.pack()


root = Tk() 
root.geometry('200x100') 
btn_file = Button(root, text ='File', command = lambda:open_file()) 
btn_file.pack(side = TOP, pady = 10) 

btn_sen = Button(root, text ='Sentence', command = lambda:input_sen()) 
btn_sen.pack(side = TOP, pady = 10) 
mainloop() 



