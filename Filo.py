import tkinter as tk
from tkinter import *

#fenetres:

app = tk.Tk()
app.title("")
app.config(bg="#ABB2B9")
app.geometry("400x500")
#app.minsize(400,500)
#app.maxsize(400,500)
app.iconbitmap('Assets/F.ico')
# Comptes id:
username_id = ('Amrane','Amrane2008','2008')
# Chargement image Navbar:

nav_icon = PhotoImage(file='') 
nav_sub_menu = PhotoImage(file='Assets/menu-icon.png')
nav_sub_info = PhotoImage(file='Assets/info-icon.png')
nav_sub_lock = PhotoImage(file='Assets/lock-icon.png')
nav_sub_main = PhotoImage(file='Assets/main1.png')
nav_sub_box = PhotoImage(file='Assets/box-icon.png')
info_sub1 = PhotoImage(file='Assets/settings-icon.png')
info_sub2 = PhotoImage(file='Assets/round-icon.png')
info_sub3 = PhotoImage(file='Assets/Load-icon.png')
# Navigation "Top":
top_frame = tk.Frame(app,bg="#616A6B")
top_frame.pack(side="top", fill=tk.X)

# Les fonctions "nav":
info_btn = False
menu_btn = False
lock_btn = False
box_btn = False
# Fonction Switch:
def Switch_info():
    global info_btn, menu_btn, lock_btn
    info_btn = True
    if info_btn == True:
        menu_btn == False
        lab_lock.place(x=400, y=300)
        lab_menu.place(x=400, y=300)
        lab_box.place(x=400, y=300)
        lab_info.place(x=0, y=70)
    else:
        info_btn == True
        lab_info.place(x=0, y=70)
        
def Switch_menu():
    global menu_btn, info_btn, lock_btn
    menu_btn = True
    if menu_btn == True:
        info_btn == False
        lab_info.place(x=400, y=300)
        lab_lock.place(x=400, y=300)
        lab_box.place(x=400, y=300)
        lab_menu.place(x=0, y=70)
    else:
        menu_btn == True
        lab_menu.place(x=400, y=300)

def Switch_lock():
    global menu_btn, info_btn, lock_btn
    lock_btn = True
    if lock_btn == True:
        info_btn == False
        menu_btn == False
        lab_info.place(x=400, y=300)
        lab_menu.place(x=400, y=300)
        lab_box.place(x=400, y=300)
        lab_lock.place(x=0, y=70)
    else:
        lock_btn == True
        lab_lock.place(x=400, y=300)

def Switch_box():
    global menu_btn, info_btn, lock_btn, box_btn
    box_btn = True
    if box_btn == True:
        info_btn == False
        menu_btn == False
        lab_info.place(x=400, y=300)
        lab_menu.place(x=400, y=300)
        lab_lock.place(x=400, y=300)
        lab_box.place(x=0, y=70)
    else:
        box_btn == True
        lab_box.place(x=400, y=300)    

def connexion():
    global username_id
    
    if username_id():
        print("Connexion")
        
    else:
        print("Aucune")
        
# Text de Navigation "Top":
main_text = tk.Label(top_frame, font="ExtraCondensed 20",bg="#616A6B", fg="#ABB2B9", height=2, padx= 20)
main_text.pack()
navbar_main = tk.Button(top_frame, image=nav_sub_main, bg="#616A6B", bd=0, activebackground="#616A6B")
navbar_main.place(x = 155, y = 10)

# Navigation Icons "Top":
#Menu--
navbar_menu = tk.Button(top_frame, image=nav_sub_menu, bg="#616A6B", bd=0, activebackground="#616A6B", command= Switch_menu)
navbar_menu.place(x = 10, y = 17)
#info--
navbar_info = tk.Button(top_frame, image=nav_sub_info, bg="#616A6B", bd=0, activebackground="#616A6B", command= Switch_info)
navbar_info.place(x = 350, y = 17)
#Account--
navbar_lock = tk.Button(top_frame, image=nav_sub_lock, bg="#616A6B", bd=0, activebackground="#616A6B", command= Switch_lock)
navbar_lock.place(x = 300, y = 17)
#Box--
navbar_box = tk.Button(top_frame, image=nav_sub_box, bg="#616A6B", bd=0, activebackground="#616A6B", command= Switch_box)
navbar_box.place(x = 60, y = 17)

# Fenetres mobiles "Lab":
#info
lab_info = tk.Frame(app, bg="gray", width=400,height=500)
lab_info.place(x=400, y=300)
tk.Label(lab_info, font="ExtraCondensed 15", bg="white", fg="black",width=300,height=2,padx=20).place(x=0, y=0)
#menu--
lab_menu = tk.Frame(app, bg="#5DADE2", width=400,height=500)
lab_menu.place(x=400, y=300)
tk.Label(lab_menu, font="ExtraCondensed 15", bg="white", fg="black",width=300,height=2,padx=20).place(x=0, y=0)
#Lock--
lab_lock = tk.Frame(app, bg="#282827", width=400,height=500)
lab_lock.place(x=400, y=300)
tk.Label(lab_lock,font="ExtraCondensed 15", bg="white", fg="black",width=300,height=2,padx=20).place(x=0, y=0)
#Box--
lab_box = tk.Frame(app, bg="#E2DA5D", width=400,height=500)
lab_box.place(x=400, y=300)
tk.Label(lab_box,font="ExtraCondensed 15", bg="white", fg="black",width=300,height=2,padx=20).place(x=0, y=0)
#Text1 = Label(lab_box,font="ExtraCondensed 13",text="douaa..", bg="white", fg="gray30",width=0,height=2,padx=20).place(x=0, y=0)
# Navigation icon
Icon1_info = Button(lab_lock, image=info_sub1, bg="white", bd=0, activebackground="white", command= None,width=710,height=27,padx=20).place(x=10, y=10)
Icon2_box = Button(lab_info, image=info_sub2, bg="white", bd=0, activebackground="white", command= app.quit,width=710,height=27,padx=20).place(x=10, y=10)

# Connexion / Load

Load_lock = Button(lab_lock, image=info_sub3, bg="#282827", bd=0, activebackground="#282827",width=0,height=0,padx=20, command= None).place(x=165, y=180)


app.mainloop()