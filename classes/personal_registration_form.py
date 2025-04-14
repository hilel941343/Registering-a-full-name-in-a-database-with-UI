from tkinter import *
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('540x640+200+10')
windows.resizable(0,0)
#Frame
frame = Frame(windows,width= 610,height=640 ,bg='black',bd =8)
frame.place(x=0,y=0)
#labels and Entry fields
heading = Label(frame,text='Personal Registration Form', fg= '#97ffff',bg='black', font=('Calibre',20,'bold'))
heading.place(x=90,y=3)

firstname = Label(frame, text ='First Name:', fg ='#97ffff', bg='black',font =('Calibre',15,'bold'))
firstname.place(x=10,y=70)

firstnameEntry =Entry(frame,width =30,borderwidth=2)
firstnameEntry.place(x=240 ,y=70)


lastname = Label(frame, text ='Last Name:', fg ='#97ffff', bg='black',font =('Calibre',15,'bold'))
lastname.place(x=10,y=110)

lastnameEntry =Entry(frame,width =30,borderwidth=2)
lastnameEntry.place(x=240 ,y=110)

gender = Label(frame, text ='Select Gender:', fg ='#97ffff', bg='black',font =('Calibre',15,'bold'))
gender.place(x=10,y=150)

genderRadio1 =Radiobutton(frame,text='Male',variable=gender,value='Male', font='Tahoma 13 bold')
genderRadio1.place(x=240 , y=150)

genderRadio2 =Radiobutton(frame,text='Female',variable=gender,value='Female', font='Tahoma 13 bold')
genderRadio2.place(x=350 , y=150)



windows.mainloop()