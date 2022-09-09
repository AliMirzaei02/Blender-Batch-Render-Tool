import subprocess
from tkinter import *
from tkinter import filedialog


def Render():
	bat_code = "@echo off\ncd "

	path_str = path.get()
	path_str = path_str[1:-1]
	blender_files = path_str.split(", ")

	bat_code += '"' + b_path.get() + '"'

	if len(blender_files) == 1:
		bat_code += "\n" + "blender -b " + '"' + blender_files[0][1:-2] + '"' + " -a"
	else:
		for i in range(len(blender_files)):
			bat_code += "\n" + "blender -b " + '"' + blender_files[i][1:-1] + '"' + " -a"

	bat_file = open(r"Batch.bat", "w+")

	bat_file.write(bat_code)

	bat_file.close()

	subprocess.call([r"Batch.bat"])

def BlenderPath():
	blender_path = filedialog.askdirectory(title='Save Video')
	b_path.set(blender_path)

def Browse():
	blender_path = filedialog.askopenfilenames(title='Save Video')
	path.set(blender_path)

def Reset():
    b_path.set('')
    path.set('')

root = Tk()
root.geometry('400x170')
root.iconbitmap(r'icon.ico')
root.configure(background='orange')
root.resizable(False, False)
root.title("Blender Batch Render Tool")

path = StringVar()
b_path = StringVar()

Label(root, text='Enter your Blender Foundation path: ', fg='blue' ,bg='orange', font='arial 10 bold').place(x=10, y=15)
Entry(root, width=41, textvariable=b_path, fg='red').place(x=30, y=40)
Button(root, text='Browse', font='arial 7 bold', command=BlenderPath, width=13, fg='orange' ,bg='blue', relief=GROOVE).place(x=282, y=40)

Label(root, text='Choose your file(s): ', fg='blue' ,bg='orange', font='arial 10 bold').place(x=10, y=65)
Entry(root, width=41, textvariable=path, fg='red').place(x=30, y=90)
Button(root, text='Browse', font='arial 7 bold', command=Browse, width=13, fg='orange' ,bg='blue', relief=GROOVE).place(x=282, y=90)

Button(root, text='Render', font='arial 15 bold', fg='orange' ,bg='blue', command = Render).place(x=282, y=120)

Button(root, text='Reset', font='arial 15 bold', fg='orange' ,bg='blue', command = Reset).place(x=30, y=120)


root.mainloop()