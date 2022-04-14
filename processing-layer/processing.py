

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import SATAH_support

class SATAH:
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

        top.geometry("1500x859+528+112")
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
        self.Button1.place(relx=0.85, rely=0.889, height=44, width=77)
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
        self.TCombobox1.place(relx=0.231, rely=0.689, relheight=0.047
                , relwidth=0.273)
        self.value_list = ['The atom on FCC site ','The atom on HCP site ','The atom between two atoms','The atom on top  of  first layer',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(takefocus="")

        self.Button2_1 = tk.Button(self.top)
        self.Button2_1.place(relx=0.033, rely=0.219, height=84, width=107)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#d9d9d9")
        self.Button2_1.configure(compound='left')
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text='''Type of Miller 

Indices of the 

Crystal''')

        self.Button2_1_1 = tk.Button(self.top)
        self.Button2_1_1.place(relx=0.033, rely=0.396, height=54, width=107)
        self.Button2_1_1.configure(activebackground="#ececec")
        self.Button2_1_1.configure(activeforeground="#000000")
        self.Button2_1_1.configure(background="#d9d9d9")
        self.Button2_1_1.configure(compound='left')
        self.Button2_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1.configure(foreground="#000000")
        self.Button2_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1.configure(highlightcolor="black")
        self.Button2_1_1.configure(pady="0")
        self.Button2_1_1.configure(text='''Cut-Off Energy''')

        self.Button2_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1.place(relx=0.033, rely=0.533, height=54, width=107)
        self.Button2_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1.configure(compound='left')
        self.Button2_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1.configure(pady="0")
        self.Button2_1_1_1.configure(text='''Lattice Parameter 

of the Crystal''')

        self.Button2_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1.place(relx=0.033, rely=0.678, height=54, width=107)
        self.Button2_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1.configure(text='''Position of the 

 adsorbed atoms''')

        self.Button2_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1.place(relx=0.553, rely=0.094, height=54
                , width=107)
        self.Button2_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1_1.configure(text='''Number of the
 
atoms''')

        self.Button2_1_1_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1_1_1.place(relx=0.553, rely=0.366, height=54
                , width=107)
        self.Button2_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1_1_1_1.configure(text='''Type of GGA''')

        self.Button2_1_1_1_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1_1_1_1.place(relx=0.553, rely=0.532, height=54
                , width=107)
        self.Button2_1_1_1_1_1_1_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_1_1_1_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_1_1_1_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1.configure(compound='left')
        self.Button2_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_1_1_1_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_1_1_1_1_1.configure(pady="0")
        self.Button2_1_1_1_1_1_1_1_1.configure(text='''Type of element''')

        self.Button2_1_1_1_1_1_1_1_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_1_1_1_1_1_1.place(relx=0.553, rely=0.667, height=54
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

potentials File''')

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
                label="ASE GUI")
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

        self.TCombobox1_1 = ttk.Combobox(self.top)
        self.TCombobox1_1.place(relx=0.707, rely=0.375, relheight=0.047
                , relwidth=0.24)
        self.value_list = ['RPBE ','PBE','revPBE','PBEsol','RPBE+D3','PBE+D3','revPBE+D3','PBEsol+D3',]
        self.TCombobox1_1.configure(values=self.value_list)
        self.TCombobox1_1.configure(takefocus="")

        self.Button2_1_2_1 = tk.Button(self.top)
        self.Button2_1_2_1.place(relx=0.553, rely=0.21, height=74, width=107)
        self.Button2_1_2_1.configure(activebackground="#ececec")
        self.Button2_1_2_1.configure(activeforeground="#000000")
        self.Button2_1_2_1.configure(background="#d9d9d9")
        self.Button2_1_2_1.configure(compound='left')
        self.Button2_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_2_1.configure(foreground="#000000")
        self.Button2_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_2_1.configure(highlightcolor="black")
        self.Button2_1_2_1.configure(pady="0")
        self.Button2_1_2_1.configure(text='''Type of adsorbed 
atom''')

        self.TCombobox2 = ttk.Combobox(self.top)
        self.TCombobox2.place(relx=0.707, rely=0.229, relheight=0.047
                , relwidth=0.238)
        self.value_list = ['H','C','N','S','O',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(takefocus="")

        self.TCombobox4 = ttk.Combobox(self.top)
        self.TCombobox4.place(relx=0.231, rely=0.4, relheight=0.047
                , relwidth=0.271)
        self.value_list = ['400','405','410','415','420','425','430','435','440','445','450','455','460','465','470','475','480','485','490','495','500',]
        self.TCombobox4.configure(values=self.value_list)
        self.TCombobox4.configure(takefocus="")

        self.Checkbutton1 = tk.Checkbutton(self.top)
        self.Checkbutton1.place(relx=0.245, rely=0.467, relheight=0.056
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
        self.Checkbutton2.place(relx=0.733, rely=0.438, relheight=0.056
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

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.033, rely=0.063, height=64, width=107)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Scaling Constant 

Factor''')

        self.TCombobox5 = ttk.Combobox(self.top)
        self.TCombobox5.place(relx=0.231, rely=0.111, relheight=0.048
                , relwidth=0.269)
        self.value_list = ['+/- Two   Decimal places ','+/- Three Decimal places ','+/- Four  Decimal places ','+/- Five  Decimal places ',]
        self.TCombobox5.configure(values=self.value_list)
        self.TCombobox5.configure(takefocus="")

        self.Spinbox1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.231, rely=0.044, relheight=0.042
                , relwidth=0.273)
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

        self.Spinbox2 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox2.place(relx=0.707, rely=0.104, relheight=0.042
                , relwidth=0.24)
        self.Spinbox2.configure(activebackground="#f9f9f9")
        self.Spinbox2.configure(background="white")
        self.Spinbox2.configure(buttonbackground="#d9d9d9")
        self.Spinbox2.configure(disabledforeground="#a3a3a3")
        self.Spinbox2.configure(font="TkDefaultFont")
        self.Spinbox2.configure(foreground="black")
        self.Spinbox2.configure(highlightbackground="black")
        self.Spinbox2.configure(highlightcolor="black")
        self.Spinbox2.configure(insertbackground="black")
        self.Spinbox2.configure(selectbackground="blue")
        self.Spinbox2.configure(selectforeground="white")

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.007, rely=0.01, relheight=0.023
                , relwidth=0.176)
        self.Labelframe1.configure(relief='ridge')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief="ridge")
        self.Labelframe1.configure(text='''SATAH by Mustafa Alsalmi and Arun Chutia''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Button2_1_1_1_2 = tk.Button(self.top)
        self.Button2_1_1_1_2.place(relx=0.231, rely=0.533, height=24, width=17)
        self.Button2_1_1_1_2.configure(activebackground="#ececec")
        self.Button2_1_1_1_2.configure(activeforeground="#000000")
        self.Button2_1_1_1_2.configure(background="#d9d9d9")
        self.Button2_1_1_1_2.configure(compound='left')
        self.Button2_1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_2.configure(foreground="#000000")
        self.Button2_1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_2.configure(highlightcolor="black")
        self.Button2_1_1_1_2.configure(pady="0")
        self.Button2_1_1_1_2.configure(text='''a''')

        self.Button2_1_1_1_2_1 = tk.Button(self.top)
        self.Button2_1_1_1_2_1.place(relx=0.231, rely=0.6, height=24, width=17)
        self.Button2_1_1_1_2_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_2_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_2_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_2_1.configure(compound='left')
        self.Button2_1_1_1_2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_2_1.configure(foreground="#000000")
        self.Button2_1_1_1_2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_2_1.configure(highlightcolor="black")
        self.Button2_1_1_1_2_1.configure(pady="0")
        self.Button2_1_1_1_2_1.configure(text='''b''')

        self.Button2_1_1_1_2_1_1 = tk.Button(self.top)
        self.Button2_1_1_1_2_1_1.place(relx=0.38, rely=0.556, height=24
                , width=17)
        self.Button2_1_1_1_2_1_1.configure(activebackground="#ececec")
        self.Button2_1_1_1_2_1_1.configure(activeforeground="#000000")
        self.Button2_1_1_1_2_1_1.configure(background="#d9d9d9")
        self.Button2_1_1_1_2_1_1.configure(compound='left')
        self.Button2_1_1_1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1_1_1_2_1_1.configure(foreground="#000000")
        self.Button2_1_1_1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1_1_1_2_1_1.configure(highlightcolor="black")
        self.Button2_1_1_1_2_1_1.configure(pady="0")
        self.Button2_1_1_1_2_1_1.configure(text='''c''')

        self.Spinbox1_1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox1_1.place(relx=0.281, rely=0.54, relheight=0.042
                , relwidth=0.074)
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

        self.Spinbox3 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox3.place(relx=0.281, rely=0.6, relheight=0.042
                , relwidth=0.074)
        self.Spinbox3.configure(activebackground="#f9f9f9")
        self.Spinbox3.configure(background="white")
        self.Spinbox3.configure(buttonbackground="#d9d9d9")
        self.Spinbox3.configure(disabledforeground="#a3a3a3")
        self.Spinbox3.configure(font="TkDefaultFont")
        self.Spinbox3.configure(foreground="black")
        self.Spinbox3.configure(highlightbackground="black")
        self.Spinbox3.configure(highlightcolor="black")
        self.Spinbox3.configure(insertbackground="black")
        self.Spinbox3.configure(selectbackground="blue")
        self.Spinbox3.configure(selectforeground="white")

        self.Spinbox3_1 = tk.Spinbox(self.top, from_=1.0, to=100.0)
        self.Spinbox3_1.place(relx=0.43, rely=0.556, relheight=0.042
                , relwidth=0.074)
        self.Spinbox3_1.configure(activebackground="#f9f9f9")
        self.Spinbox3_1.configure(background="white")
        self.Spinbox3_1.configure(buttonbackground="#d9d9d9")
        self.Spinbox3_1.configure(disabledforeground="#a3a3a3")
        self.Spinbox3_1.configure(font="TkDefaultFont")
        self.Spinbox3_1.configure(foreground="black")
        self.Spinbox3_1.configure(highlightbackground="black")
        self.Spinbox3_1.configure(highlightcolor="black")
        self.Spinbox3_1.configure(insertbackground="black")
        self.Spinbox3_1.configure(selectbackground="blue")
        self.Spinbox3_1.configure(selectforeground="white")

        self.TCombobox3 = ttk.Combobox(self.top)
        self.TCombobox3.place(relx=0.7, rely=0.532, relheight=0.047
                , relwidth=0.247)
        self.value_list = ['Al','Fe','Pb','Cu','Zn',]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(textvariable=self.combobox)
        self.TCombobox3.configure(takefocus="")

        self.TCombobox1_2 = ttk.Combobox(self.top)
        self.TCombobox1_2.place(relx=0.227, rely=0.229, relheight=0.047
                , relwidth=0.272)
        self.value_list = ['(111) ','(110) ','(100)',]
        self.TCombobox1_2.configure(values=self.value_list)
        self.TCombobox1_2.configure(takefocus="")

def start_up():
    SATAH_support.main()

if __name__ == '__main__':
    SATAH_support.main()




