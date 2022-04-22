import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from distutils import command
from tkinter import messagebox
from setuptools._vendor.importlib_metadata import _top_level_declared


import os
import subprocess
from ase.build import fcc111 
from ase.visualize import view 

def slab_ase_gui():
    slab = fcc111('Cu', size=(2,2,2), vacuum=15.0) 
    view(slab) 

def showMsg():
    messagebox.showinfo('ASE Gui','You open ASE GUI!')

def UploadAction():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def ase_gui():
    _top1_ase_gui=Toplevel(_top1)
    _top1_ase_gui.geometry("400x400")
    _top1_ase_gui.title("ASE GUI")
    my_str1=tk.StringVar()
    l1 = tk.Label(_top1_ase_gui,textvariable=my_str1)
    l1.grid(row=1,column=2)
    my_str1.set("*make sure that you download pip in your terminal* ")
    button = Button(_top1_ase_gui,
    text = 'Open',command = slab_ase_gui())
    button.pack()  
    

class CreateUserInterface:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1500x940+553+158")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("SATAH")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()
        self.che53 = tk.IntVar()
        self.che54 = tk.IntVar()

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.901, rely=0.921, height=44, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Run''')

        self.TCombobox1 = ttk.Combobox(self.top)
        self.TCombobox1.place(relx=0.133, rely=0.495, relheight=0.035
                , relwidth=0.091)
        self.value_list = ['The atom on FCC site ','The atom on HCP site ','The atom between two atoms','The atom on top  of  first layer',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(takefocus="")

        self.Button2_1_1_1_1_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1_1_1_1_1.place(relx=0.033, rely=0.853, height=54
                , width=107)
        self.Button2_1_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1_1_1_1_1_1.configure(text='''Upload Pseudo

potentials File''', command=lambda:UploadAction())

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="Files")
        self.sub_menu.add_command(
                label="New")
        self.sub_menu.add_command(
                label="Open")
        self.sub_menu.add_command(
                label="Close")
        self.sub_menu.add_command(
                label="Save As ..")
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Edit")
        self.sub_menu1.add_command(
                label="New Strucutre")
        self.sub_menu1.add_command(
                label="Bonds")
        self.sub_menu1.add_command(
                label="Vectors")
        self.sub_menu1.add_command(
                label="Lattice Planes")
        self.sub_menu12 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12,
                label="Modulus")
        self.sub_menu12.add_command(
                label="ASE GUI", command=ase_gui)
        self.sub_menu12.add_command(
                label="Equation of state")
        self.sub_menu123 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.sub_menu12.add_cascade(menu=self.sub_menu123,
                label="Bond Centric Manipulation Tool")
        self.sub_menu1234 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.sub_menu12.add_cascade(menu=self.sub_menu1234,
                label="Geometry Tools")
        self.sub_menu1234.add_command(
                label="API")
        self.sub_menu12345 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu12345,
                label="View")
        self.sub_menu123456 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu123456,
                label="Cryptography")
        self.menubar.add_command(
                label="Help")
        self.menubar.add_command(
                label="Exit", command=top.quit)

        self.TCombobox1_1 = ttk.Combobox(self.top)
        self.TCombobox1_1.place(relx=0.133, rely=0.705, relheight=0.034
                , relwidth=0.091)
        self.value_list = ['RPBE ','PBE','revPBE','PBEsol','RPBE+D3','PBE+D3','revPBE+D3','PBEsol+D3',]
        self.TCombobox1_1.configure(values=self.value_list)
        self.TCombobox1_1.configure(takefocus="")

        self.TCombobox2 = ttk.Combobox(self.top)
        self.TCombobox2.place(relx=0.133, rely=0.641, relheight=0.034
                , relwidth=0.091)
        self.value_list = ['H','C','N','S','O',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(takefocus="")

        self.TCombobox4 = ttk.Combobox(self.top)
        self.TCombobox4.place(relx=0.133, rely=0.253, relheight=0.034
                , relwidth=0.091)
        self.value_list = ['400','405','410','415','420','425','430','435','440','445','450','455','460','465','470','475','480','485','490','495','500',]
        self.TCombobox4.configure(values=self.value_list)
        self.TCombobox4.configure(takefocus="")

        self.Checkbutton1 = tk.Checkbutton(self.top)
        self.Checkbutton1.place(relx=0.133, rely=0.295, relheight=0.028
                , relwidth=0.101)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Auto''')
        self.Checkbutton1.configure(variable=self.che53)

        self.Checkbutton2 = tk.Checkbutton(self.top)
        self.Checkbutton2.place(relx=0.133, rely=0.747, relheight=0.024
                , relwidth=0.101)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(anchor='w')
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(compound='left')
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Auto''')
        self.Checkbutton2.configure(variable=self.che54)

        self.TCombobox5 = ttk.Combobox(self.top)
        self.TCombobox5.place(relx=0.133, rely=0.116, relheight=0.035
                , relwidth=0.091)
        self.value_list = ['+/- Two   Decimal places ','+/- Three Decimal places ','+/- Four  Decimal places ','+/- Five  Decimal places ',]
        self.TCombobox5.configure(values=self.value_list)
        self.TCombobox5.configure(takefocus="")

        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.133, rely=0.074, relheight=0.036
                , relwidth=0.023)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="blue")
        self.Spinbox1.configure(selectforeground="white")

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.018, rely=0.935, relheight=0.037
                , relwidth=0.23)
        self.Labelframe1.configure(relief='ridge')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief="ridge")
        self.Labelframe1.configure(text='''SATAH by Mustafa Alsalmi and Arun Chutia''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Spinbox1_1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1_1.place(relx=0.173, rely=0.347, relheight=0.037
                , relwidth=0.023)
        self.Spinbox1_1.configure(activebackground="#f9f9f9")
        self.Spinbox1_1.configure(background="white")
        self.Spinbox1_1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1_1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1_1.configure(font="TkDefaultFont")
        self.Spinbox1_1.configure(foreground="black")
        self.Spinbox1_1.configure(highlightbackground="black")
        self.Spinbox1_1.configure(highlightcolor="black")
        self.Spinbox1_1.configure(insertbackground="black")
        self.Spinbox1_1.configure(selectbackground="blue")
        self.Spinbox1_1.configure(selectforeground="white")

        self.TCombobox3 = ttk.Combobox(self.top)
        self.TCombobox3.place(relx=0.133, rely=0.789, relheight=0.034
                , relwidth=0.091)
        self.value_list = ['Al','Fe','Pb','Cu','Zn',]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=self.combobox)
        self.TCombobox3.configure(takefocus="")

        self.TCombobox1_2 = ttk.Combobox(self.top)
        self.TCombobox1_2.place(relx=0.133, rely=0.179, relheight=0.035
                , relwidth=0.091)
        self.value_list = ['(111) ','(110) ','(100)',]
        self.TCombobox1_2.configure(values=self.value_list)
        self.TCombobox1_2.configure(takefocus="")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.02, rely=0.074, height=64, width=113)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Scaling Constant

Factor''')

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.027, rely=0.241, height=50, width=129)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Cut-Off Energy''')
        self.TLabel1.configure(compound='left')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.013, rely=-0.011, height=74, width=712)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI Historic} -size 24 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Structure Input Parameters :''')

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.027, rely=0.359, height=73, width=154)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Lattice Parameter

of the Crystal''')

        self.Label5 = tk.Label(self.top)
        self.Label5.place(relx=0.133, rely=0.347, height=29, width=46)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''a''')

        self.Label5_1 = tk.Label(self.top)
        self.Label5_1.place(relx=0.133, rely=0.389, height=30, width=46)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(anchor='w')
        self.Label5_1.configure(background="#d9d9d9")
        self.Label5_1.configure(compound='left')
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''b''')

        self.Label5_1_1 = tk.Label(self.top)
        self.Label5_1_1.place(relx=0.133, rely=0.432, height=37, width=46)
        self.Label5_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1.configure(activeforeground="black")
        self.Label5_1_1.configure(anchor='w')
        self.Label5_1_1.configure(background="#d9d9d9")
        self.Label5_1_1.configure(compound='left')
        self.Label5_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1.configure(foreground="#000000")
        self.Label5_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1.configure(highlightcolor="black")
        self.Label5_1_1.configure(text='''c''')

        self.Label4_1 = tk.Label(self.top)
        self.Label4_1.place(relx=0.033, rely=0.463, height=111, width=103)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(activeforeground="black")
        self.Label4_1.configure(anchor='w')
        self.Label4_1.configure(background="#d9d9d9")
        self.Label4_1.configure(compound='left')
        self.Label4_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1.configure(foreground="#000000")
        self.Label4_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1.configure(highlightcolor="black")
        self.Label4_1.configure(text='''Position of the

 adsorbed atoms''')

        self.Spinbox1_1_1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1_1_1.place(relx=0.173, rely=0.389, relheight=0.036
                , relwidth=0.023)
        self.Spinbox1_1_1.configure(activebackground="#f9f9f9")
        self.Spinbox1_1_1.configure(background="white")
        self.Spinbox1_1_1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1_1_1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1_1_1.configure(font="TkDefaultFont")
        self.Spinbox1_1_1.configure(foreground="black")
        self.Spinbox1_1_1.configure(highlightbackground="black")
        self.Spinbox1_1_1.configure(highlightcolor="black")
        self.Spinbox1_1_1.configure(insertbackground="black")
        self.Spinbox1_1_1.configure(selectbackground="blue")
        self.Spinbox1_1_1.configure(selectforeground="white")

        self.Spinbox1_1_1_1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1_1_1_1.place(relx=0.173, rely=0.432, relheight=0.039
                , relwidth=0.023)
        self.Spinbox1_1_1_1.configure(activebackground="#f9f9f9")
        self.Spinbox1_1_1_1.configure(background="white")
        self.Spinbox1_1_1_1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1_1_1_1.configure(font="TkDefaultFont")
        self.Spinbox1_1_1_1.configure(foreground="black")
        self.Spinbox1_1_1_1.configure(highlightbackground="black")
        self.Spinbox1_1_1_1.configure(highlightcolor="black")
        self.Spinbox1_1_1_1.configure(insertbackground="black")
        self.Spinbox1_1_1_1.configure(selectbackground="blue")
        self.Spinbox1_1_1_1.configure(selectforeground="white")

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(relx=0.027, rely=0.159, height=64, width=112)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Miller Indices''')

        self.TLabel1_1 = ttk.Label(self.top)
        self.TLabel1_1.place(relx=0.033, rely=0.568, height=50, width=129)
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(font="TkDefaultFont")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Number of Atoms''')
        self.TLabel1_1.configure(compound='left')

        self.Spinbox1_2 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1_2.place(relx=0.133, rely=0.579, relheight=0.037
                , relwidth=0.023)
        self.Spinbox1_2.configure(activebackground="#f9f9f9")
        self.Spinbox1_2.configure(background="white")
        self.Spinbox1_2.configure(buttonbackground="#d9d9d9")
        self.Spinbox1_2.configure(disabledforeground="#a3a3a3")
        self.Spinbox1_2.configure(font="TkDefaultFont")
        self.Spinbox1_2.configure(foreground="black")
        self.Spinbox1_2.configure(highlightbackground="black")
        self.Spinbox1_2.configure(highlightcolor="black")
        self.Spinbox1_2.configure(insertbackground="black")
        self.Spinbox1_2.configure(selectbackground="blue")
        self.Spinbox1_2.configure(selectforeground="white")

        self.TLabel1_1_1_1 = ttk.Label(self.top)
        self.TLabel1_1_1_1.place(relx=0.4, rely=1.137, height=51, width=129)
        self.TLabel1_1_1_1.configure(background="#d9d9d9")
        self.TLabel1_1_1_1.configure(foreground="#000000")
        self.TLabel1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel1_1_1_1.configure(relief="flat")
        self.TLabel1_1_1_1.configure(anchor='w')
        self.TLabel1_1_1_1.configure(justify='center')
        self.TLabel1_1_1_1.configure(text='''Type of adsorbed
atom''')
        self.TLabel1_1_1_1.configure(compound='left')

        self.Label4_1_1 = tk.Label(self.top)
        self.Label4_1_1.place(relx=0.033, rely=0.632, height=62, width=103)
        self.Label4_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1.configure(activeforeground="black")
        self.Label4_1_1.configure(anchor='w')
        self.Label4_1_1.configure(background="#d9d9d9")
        self.Label4_1_1.configure(compound='left')
        self.Label4_1_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1_1.configure(foreground="#000000")
        self.Label4_1_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1_1.configure(highlightcolor="black")
        self.Label4_1_1.configure(text='''Type of the

 adsorbed atoms''')

        self.Label4_1_1_1 = tk.Label(self.top)
        self.Label4_1_1_1.place(relx=0.04, rely=0.705, height=62, width=104)
        self.Label4_1_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1_1.configure(activeforeground="black")
        self.Label4_1_1_1.configure(anchor='w')
        self.Label4_1_1_1.configure(background="#d9d9d9")
        self.Label4_1_1_1.configure(compound='left')
        self.Label4_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1_1_1.configure(foreground="#000000")
        self.Label4_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1_1_1.configure(highlightcolor="black")
        self.Label4_1_1_1.configure(text='''Type of GGA''')

        self.Label4_1_1_1_1 = tk.Label(self.top)
        self.Label4_1_1_1_1.place(relx=0.033, rely=0.779, height=62, width=103)
        self.Label4_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label4_1_1_1_1.configure(activeforeground="black")
        self.Label4_1_1_1_1.configure(anchor='w')
        self.Label4_1_1_1_1.configure(background="#d9d9d9")
        self.Label4_1_1_1_1.configure(compound='left')
        self.Label4_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label4_1_1_1_1.configure(foreground="#000000")
        self.Label4_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label4_1_1_1_1.configure(highlightcolor="black")
        self.Label4_1_1_1_1.configure(text='''Type of Element''')

        self.Button2_1_1_1_1_1_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1_1_1_1_1_1.place(relx=0.14, rely=0.853, height=54
                , width=107)
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1_1_1_1_1_1_1.configure(text='''Upload KPOINT

 File''', command=lambda:UploadAction())

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.26, rely=0.09, relheight=0.811, relwidth=0.717)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")


def show():
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = CreateUserInterface(_top1)
    root.mainloop()
