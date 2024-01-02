import tkinter as t
from tkinter import messagebox
import random as r
import string as s
import json

def on_generate_pass():
    chars=list(s.ascii_letters+s.punctuation+s.digits)
    password = ''.join(r.choices(chars,k=12))
    e_pass.delete(0,t.END)
    e_pass.insert(0,password)
    return password

def on_search():
    website = e_web.get()
    try:
        with open('data.json','r') as file:
            data=json.load(file)            
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title='Error',message='No records')
    else:
        try:
            e_user.delete(0, t.END)
            e_user.insert(0, (data[website]['user']))
            e_pass.delete(0, t.END)
            e_pass.insert(0, (data[website]['pass']))
        except KeyError:
            messagebox.showerror(title='Error',message='No record')
        
def on_save():
    website = e_web.get()
    user=e_user.get()
    password= e_pass.get()
    new_data = {
        website:{
            'user':user,
            'pass':password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title='Not saved',message='Empty')
    else:
        try:
            with open('data.json','r') as file:
                #file.writelines(f'{website} | {user} | {password}\n')
                #json.dump(new_data,file,indent=4)
                data=json.load(file)
                data.update(new_data)
        except json.decoder.JSONDecodeError:
            with open('data.json','w') as file:
                json.dump(new_data,file,indent=4)
        else:
            with open('data.json','w') as file:
                json.dump(data,file,indent=4)

        messagebox.showinfo(title='Saved',message='Saved')
        e_web.delete(0,t.END)
        e_user.delete(0,t.END)
        e_pass.delete(0,t.END) 

win=t.Tk()
win.title('PassMan')
win.minsize(350,200)

l_web=t.Label(text='website')
l_web.grid(row=0,column=0)

l_user=t.Label(text='User/mail')
l_user.grid(row=1,column=0)

l_pass=t.Label(text='password')
l_pass.grid(row=2,column=0)

e_web=t.Entry(width=20)
e_web.grid(row=0,column=1)
b_search=t.Button(text='Search',width=10,command=on_search)
b_search.grid(row=0,column=2)

e_user=t.Entry(width=35)
e_user.grid(row=1,column=1,columnspan=2)

e_pass=t.Entry(width=20)
e_pass.grid(row=2,column=1)
b_generate=t.Button(text='Generate',width=10,command=on_generate_pass)
b_generate.grid(row=2,column=2)

b_save=t.Button(text='Save', width=30,command=on_save)
b_save.grid(row=3,column=1,columnspan=2)

win.mainloop()