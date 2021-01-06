import pyautogui, time
import os
import tkinter as tk 

dir_path = os.path.dirname(os.path.realpath(__file__))

root= tk.Tk()

root.title("Spammer")

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Spam text from file')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Type in the file name that's in the same folder")
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def write():
	x1 = entry1.get()

	label3 = tk.Label(root, text="Spamming text from" + x1)
	label3.config(font=('helvetica', 10))
	canvas1.create_window(200, 100, window=label3)

	f = open(dir_path + "/" + str(x1) + ".txt",'r')

	time.sleep(10)

	for word in f:
		pyautogui.typewrite(word)
		pyautogui.press('return')

	

button1 = tk.Button(text='Spam the text', command=write, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()


