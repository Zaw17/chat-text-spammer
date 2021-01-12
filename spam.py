import pyautogui, time
import os
import tkinter as tk 


dir_path = os.path.dirname(os.path.realpath(__file__))

root = tk.Tk()

root.resizable(0,0)

root.title("Spammer")

canvas1 = tk.Canvas(root, width = 400, height = 310,  relief = 'raised', bg="#0059b3")
canvas1.pack()

label1 = tk.Label(root, text='Spam text from file', bg="#0059b3")
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Type in the file name that's in the same folder", bg="#0059b3")
label2.config(font=('helvetica', 14))
canvas1.create_window(200, 140, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 170, window=entry1)

ftypes=[".txt", 
    	".docx", 
        ".rtf", 
		]  

v = tk.StringVar(root)
v.set(ftypes[0])

label3 = tk.Label(root, text = "Select file type", bg="#0059b3")
label3.config(font=('helvetica', 14))
canvas1.create_window(200,100 , window=label3)

opt = tk.OptionMenu(root, v, *ftypes)
opt.config(width=10, font=('Helvetica', 12), bg="#0059b3")
canvas1.create_window(200,120 , window= opt)

label5 = tk.Label(root, text= "Move your mouse cursor to the top right in order to cancel the process", bg="#0059b3")
label5.config(font=('helvetica', 10))
canvas1.create_window(200,250, window=label5)


label5 = tk.Label(root, text= "©Myo Khant Zaw 2020", bg="#0059b3")
label5.config(font=('helvetica', 10))
canvas1.create_window(200,300, window=label5)

def write():
	x1 = entry1.get()
	selection = str(v.get())
	f = open(dir_path + "/" + str(x1) + selection,'r')

	time.sleep(10)

	for word in f:
		pyautogui.typewrite(word)
		pyautogui.press('return')

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red', bg="#0059b3")
labelTest.pack(side="top")
canvas1.create_window(200,280, window=labelTest)

def callback(*args):
	labelTest.configure(text="Will spam " +entry1.get() + str(v.get()))
v.trace("w", callback)

button1 = tk.Button(text='Spam the text', command=write, bg='white', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 200, window=button1)

root.mainloop()


