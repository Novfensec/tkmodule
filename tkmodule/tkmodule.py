from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk,Image
from pathlib import Path

def_dir = Path(__file__).parent

class createTk(Tk):

    def __init__(self,master=None,cnf={},**kw):
        super(createTk, self).__init__(**kw)

    def window(self,title="TkModule Window",icon=def_dir/"defaultImg/default.ico",fullscreen=False,minh=456,minw=987,maxh=None,maxw=None,size="456x456"):
        self.icon=icon
        if not fullscreen:
            self.geometry(size)
        else:
            self.wm_state('zoomed')
        self.title(title)
        self.minsize(minw,minh)
        self.maxsize(maxw,maxh)
        self.wm_iconbitmap(self.icon)

    def label(self,master=None,side=None,anchor=None,fill=None,padxn=None,padyn=None,text="Default Label",**kwargs):
        if not master:
            self.Label_var=Label(self,kwargs,text=text)
        else:
            self.Label_var=Label(master,kwargs,text=text)
        self.Label_var.pack(side=side,anchor=anchor,fill=fill,padx=padxn,pady=padyn)

    def labelImg(self,master=None,image=def_dir/"defaultImg/default.ico",side=None,anchor=None,fill=None,padx=None,pady=None,**kwargs):
        global img
        img=ImageTk.PhotoImage(Image.open(image))
        if not master:
            self.Image_var=Label(self, image=img)
        else:
            self.Image_var=Label(master, image=img)
        self.Image_var.pack(side=side,anchor=anchor,fill=fill,padx=padx,pady=pady)

    def textarea(self,master=None,scroll:bool=True,side=None,anchor=None,expand=None,fill=None,padxn=None,padyn=None,**kwargs):
        if scroll is True:
            if not master:
                self.Text_var=ScrolledText(self,cnf=kwargs)
            else:
                self.Text_var=ScrolledText(master,kwargs)
        else:
            if not master:
                self.Text_var=Text(self,kwargs)
            else:
                self.Text_var=Text(master,kwargs)
        self.Text_var.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def addBtn(self,master=None,text="Default",side=None,anchor=None,expand=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.Btn_var=Button(self,kwargs,text=text)
        else:
            self.Btn_var=Button(master,kwargs,text=text)
        self.Btn_var.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def addList(self,master=None,side=None,expand=None,anchor=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.List_var=Listbox(self,kwargs)
        else:
            self.List_var=Listbox(master,kwargs)
        self.List_var.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def addFrame(self,master=None,name=NONE,side=None,expand=None,anchor=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.Frame_var=Frame(self,kwargs)
        else:
            self.Frame_var=Frame(master,kwargs)
        self.Frame_var.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def bindkey(self,keys,cmd):
        self.bind(keys,cmd)

    def bindkey_ctrl(self,keys,cmd):
        keyl="<Control_L>"+keys
        keyr="<Control_R>"+keys
        self.bind(keyl,cmd)
        self.bind(keyr,cmd)

    def bindkey_shift(self,keys,cmd):
        keyl="<Shift_L>"+keys
        keyr="<Shift_R>"+keys
        self.bind(keyl,cmd)
        self.bind(keyr,cmd)

    def bindkey_alt(self,keys,cmd):
        keyl="<Alt_L>"+keys
        keyr="<Alt_R>"+keys
        self.bind(keyl,cmd)
        self.bind(keyr,cmd)

    def run(self):
        self.mainloop()

    def quit(self):
        self.destroy()

class Menubars(Widget):
    def __init__(self, master=None,cnf={},**kw):
        self.master=master
        self.menubar=Menu(self.master,kw)
        super(Menubars, self).__init__(master, 'menu', cnf, kw)

    def createMenu(self,**kwargs):
        self.Navigation_var=Menu(self.menubar,kwargs,tearoff=0)

    def addCmd(self,**kwargs):
        self.Navigation_var.add_command(kwargs)

    def addHead(self,label=None):
        self.menubar.add_cascade(label=label,menu=self.Navigation_var)

    def view(self,config=True):
        if config:
            self.master.configure(menu=self.menubar)
