from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk,Image
from pathlib import Path

def_dir = Path(__file__).parent

class createTk:

    def __init__(self,master=None,cnf={},**kw):
        self.tk=Tk()

    def Window(self,title="TkModule Window",icon=def_dir/"defaultImg/default.ico",fullscreen=False,minh=456,minw=987,maxh=None,maxw=None,size="456x456"):
        self.icon=icon
        if not fullscreen:
            self.tk.geometry(size)
        else:
            self.tk.wm_state('zoomed')
        self.tk.title(title)
        self.tk.minsize(minw,minh)
        self.tk.maxsize(maxw,maxh)
        self.tk.wm_iconbitmap(self.icon)
        
    def label(self,master=None,side=None,anchor=None,fill=None,padxn=None,padyn=None,text="Default Label",**kwargs):
        if not master:
            self.Labelvar=Label(self.tk,kwargs,text=text)
        else:
            self.Labelvar=Label(master,kwargs,text=text)
        self.Labelvar.pack(side=side,anchor=anchor,fill=fill,padx=padxn,pady=padyn)
    
    def labelImg(self,master=None,image=def_dir/"defaultImg/default.ico",side=None,anchor=None,fill=None,padx=None,pady=None,**kwargs):
        global img
        img=ImageTk.PhotoImage(Image.open(image))
        if not master:
            self.Imagevar=Label(self.tk, image=img)
        else:
            self.Imagevar=Label(master, image=img)
        self.Imagevar.pack(side=side,anchor=anchor,fill=fill,padx=padx,pady=pady)

    def textarea(self,master=None,scroll:bool=None,side=None,anchor=None,expand=None,fill=None,padxn=None,padyn=None,**kwargs):
        if scroll is True:
            if not master:
                self.Textvar=ScrolledText(self.tk,cnf=kwargs)
            else:
                self.Textvar=ScrolledText(master,kwargs)
        else:
            if not master:
                self.Textvar=Text(self.tk,kwargs)
            else:
                self.Textvar=Text(master,kwargs)
        self.Textvar.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)
    
    def addbtn(self,master=None,text="Default",side=None,anchor=None,expand=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.newbtn=Button(self.tk,kwargs,text=text)
        else:
            self.newbtn=Button(master,kwargs,text=text)
        self.newbtn.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def addList(self,master=None,side=None,expand=None,anchor=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.listvar=Listbox(self.tk,kwargs)
        else:
            self.listvar=Listbox(master,kwargs)
        self.listvar.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def addFrame(self,master=None,name=NONE,side=None,expand=None,anchor=None,fill=None,padxn=None,padyn=None,**kwargs):
        if not master:
            self.framevar=Frame(self.tk,kwargs)
        else:
            self.framevar=Frame(master,kwargs)
        self.framevar.pack(side=side,anchor=anchor,expand=expand,fill=fill,padx=padxn,pady=padyn)

    def Bindkey(self,keys,cmd):
        self.tk.bind(keys,cmd)

    def Bindkey_ctrl(self,keys,cmd):
        keyl="<Control_L>"+keys
        keyr="<Control_R>"+keys
        self.tk.bind(keyl,cmd)
        self.tk.bind(keyr,cmd)

    def Bindkey_shift(self,keys,cmd):
        keyl="<Shift_L>"+keys
        keyr="<Shift_R>"+keys
        self.tk.bind(keyl,cmd)
        self.tk.bind(keyr,cmd)

    def Bindkey_alt(self,keys,cmd):
        keyl="<Alt_L>"+keys
        keyr="<Alt_R>"+keys
        self.tk.bind(keyl,cmd)
        self.tk.bind(keyr,cmd)

    def Run(self):
        self.tk.mainloop()
    
    def Quit(self):
        self.tk.destroy()

class Menubars(Widget):
    def __init__(self, master=None,cnf={},**kw):
        self.master=master
        self.menubar=Menu(self.master.tk,kw)
        Widget.__init__(self,master.tk, 'menu', cnf, kw)
        
    def createMenu(self,**kwargs):
        self.nav=Menu(self.menubar,kwargs,tearoff=0)
    
    def addCmd(self,**kwargs):
        self.nav.add_command(kwargs)

    def addHead(self,label=None):
        self.menubar.add_cascade(label=label,menu=self.nav)

    def view(self,config=True):
        if config:
            self.master.configure(menu=self.menubar)