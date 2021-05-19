import tkinter as tk
import datetime
import time

#def calculate time(string job, date date, datetime)->timedelta:

#def clock_in(string job, datetime time)->bool:

#def clock_out(string job, datetime time)->bool:

#def create_window(string job):

#stolen colton code->
# root = Tk()
#
# datetime_object = datetime.datetime.now()
#
# e = Entry(root)
# root.geometry("500x500")
# e.pack()
# print(data)
# def Buttonpress():
# 	mylabel = Label(root, text = "look its a button")
# 	mylabel.pack()
#
# mybutton = Button(root, text = "", command=Buttonpress)
# #mybutton.pack()
#
# root.mainloop()


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get()))

master = tk.Tk()
master.geometry("500x500")
tk.Label(master, text="Job Description").grid(row=0)


e1 = tk.Entry(master,width=50)


e1.grid(row=0, column=1)


tk.Button(master,text='Quit',command=master.quit).grid(row=3, column=0,sticky=tk.W,pady=4)
tk.Button(master,text='Start Time', command=show_entry_fields).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.Button(master,text='Stop Time', command=show_entry_fields).grid(row=3,column=2,sticky=tk.W,pady=4)
tk.mainloop()


# fields = 'Last Name', 'First Name', 'Job', 'Country'
#
# def fetch(entries):
#     for entry in entries:
#         field = entry[0]
#         text  = entry[1].get()
#         print('%s: "%s"' % (field, text))
#
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = tk.Frame(root)
#         lab = tk.Label(row, width=15, text=field, anchor='w')
#         ent = tk.Entry(row)
#         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#         entries.append((field, ent))
#     return entries
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     ents = makeform(root, fields)
#     root.bind('<Return>', (lambda event, e=ents: fetch(e)))
#     b1 = tk.Button(root, text='Show',
#                   command=(lambda e=ents: fetch(e)))
#     b1.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='Quit', command=root.quit)
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#     root.mainloop()