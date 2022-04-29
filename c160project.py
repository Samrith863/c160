from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("NotePad")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="yellow")
open_image=ImageTk.PhotoImage(Image.open("new.png"),master=root)
save_image=ImageTk.PhotoImage(Image.open("save.png"),master=root)
close_image=ImageTk.PhotoImage(Image.open("cross.png"),master=root)
label1=Label(root,text="File Name")
input_1=Entry(root)
text_area=Text(root,height=35,width=80)

save_btn=Button(root,image=save_image,command=saveFile)
open_btn=Button(root,image=open_image,command=openFile)
close_btn=Button(root,image=close_image,command=closeWindow)

save_btn.place(relx=0.05,rely=0.03,anchor=CENTER)
open_btn.place(relx=0.11,rely=0.03,anchor=CENTER)
close_btn.place(relx=0.17,rely=0.03,anchor=CENTER)
label1.place(relx=0.28,rely=0.03,anchor=CENTER)
input_1.place(relx=0.46,rely=0.03,anchor=CENTER)
text_area.place(relx=0.5,rely=0.55,anchor=CENTER)
root.mainloop()

