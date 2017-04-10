from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

def initGUI():
    master = Tk()
    master.title("CreateBat")
    master.resizable(width=False, height=False)
    
    bots = ListBox(master,16,0,2,8,3,40)
    proxies = ListBox(master,10,3,1,7,3,22)
    
    lowcpu = IntVar()
    lowresource = IntVar()
    
    username = StringVar()
    password = StringVar()
    filename = FileName()
    dirname = FileName()
    batname = StringVar()
    
    botusername = StringVar()
    botpassword = StringVar()
    botpin = StringVar()
    botworld = StringVar()
    botscript = StringVar()
    botparam = StringVar()
    

    ip = StringVar()
    port = StringVar()
    proxyname = StringVar()
    proxypass = StringVar()

    ################### View ############################
    
    
    Checkbutton(master, text="lowcpu", variable=lowcpu, height=2)\
                        .grid(row=2, column=3, sticky=W)
    Checkbutton(master, text="lowresource", variable=lowresource, height=2)\
                        .grid(row=3, column=3, sticky=W)

    #################### Client Details ####################
    
    Label(master, text="Client Username")\
                  .grid(row=2, column=0, sticky=W, padx=5, pady=10)
    Entry(master, textvariable=username, width=20)\
                  .grid(row=2, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="Client Password")\
                  .grid(row=3, column=0, sticky=W, padx=5, pady=10)
    Entry(master, textvariable=password, width=20)\
                  .grid(row=3, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="OSBot Jar")\
                  .grid(row=4, column=0, sticky=W, padx=5, pady=10)
    Label(master, text="Path:").grid(row=5, column=0, sticky=W,padx=5, pady=10)
    pathlabel = Label(master, text="",width = 20)
    pathlabel.grid(row=5, column=1, sticky=W,padx=5, pady=10)

    ################### Bot Details #######################

    Label(master, text="Bot Details")\
                  .grid(row=6, column=0, columnspan=2, padx=5, pady=10)

    Label(master, text="Username")\
                  .grid(row=7, column=0, sticky=W, padx=5, pady=10)
    wbname = Entry(master, textvariable=botusername, width=20)
    wbname.grid(row=7, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="Password")\
                  .grid(row=8, column=0, sticky=W, padx=5, pady=10)
    wbpass = Entry(master, textvariable=botpassword, width=20)
    wbpass.grid(row=8, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="Pin")\
                  .grid(row=9, column=0, sticky=W, padx=5, pady=10)
    wbpin = Entry(master, textvariable=botpin, width=20)
    wbpin.grid(row=9, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="World")\
                  .grid(row=10, column=0, sticky=W, padx=5, pady=10)
    wbworld = Entry(master, textvariable=botworld, width=20)
    wbworld.grid(row=10, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="Script")\
                  .grid(row=11, column=0, sticky=W, padx=5, pady=10)
    wbscript = Entry(master, textvariable=botscript, width=20)
    wbscript.grid(row=11, column=1, sticky=W, padx=5, pady=10)
    Label(master, text="Param")\
                  .grid(row=12, column=0, sticky=W, padx=5, pady=10)
    wbparam = Entry(master, textvariable=botparam, width=20)
    wbparam.grid(row=12, column=1, sticky=W, padx=5, pady=10)

    #Create Proxies box
    Label(master, text="Proxies")\
                  .grid(row=9, column=3)
    proxies.createListBox()

    ############## Proxy details #####################
    
    Label(master, text="Proxy Details")\
                  .grid(row=4, column=2, columnspan=2, padx=5, pady=10)
    Label(master, text="IP")\
                  .grid(row=5, column=2, sticky=W, padx=5, pady=10)
    wip = Entry(master, textvariable=ip, width=20)
    wip.grid(row=5, column=3, sticky=W, padx=(5,20), pady=10)
    Label(master, text="Port")\
                  .grid(row=6, column=2, sticky=W, padx=5, pady=10)
    wport = Entry(master, textvariable=port, width=20)
    wport.grid(row=6, column=3, sticky=W, padx=5, pady=10)
    Label(master, text="Name")\
                  .grid(row=7, column=2, sticky=W, padx=5, pady=10)
    wname = Entry(master, textvariable=proxyname, width=20)
    wname.grid(row=7, column=3, sticky=W, padx=5, pady=10)
    Label(master, text="Password")\
                  .grid(row=8, column=2, sticky=W, padx=5, pady=10)
    wpass = Entry(master, textvariable=proxypass, width=20)
    wpass.grid(row=8, column=3, sticky=W, padx=5, pady=10)

    ####################### Buttons ############################

    Button(master, text="Add Bot", command=lambda: addBot(bots,proxies,botusername,botpassword,botpin,wbname,wbpass,wbpin,botworld,botscript,botparam))\
                   .grid(row=13, column=0, columnspan=2, pady=(0,20))
    Button(master, text="Add Proxy", command=lambda: addProxy(proxies,ip,port\
                    ,proxyname,proxypass,wip,wport,wname,wpass)).grid(row=10, column=2, sticky=E)
    Button(master, text="Clear Proxies", command=lambda: proxies.deleteElements()).grid(row=12, column=2, sticky=E)
    Button(master, text="Delete Proxy", command=lambda: proxies.deleteSelected()).grid(row=11, column=2, sticky=E)
    Button(master, text="Clear Bots", command=lambda: bots.deleteElements()).grid(row=17,column=2)
    Button(master, text="Make Bat",command=lambda: makeBat(pathlabel,lowcpu,lowresource,username,\
                                                           password,bots,batname,dirname,filename)).grid(row=18,column=2)
    Button(master, text="Delete Bot", command=lambda: bots.deleteSelected()).grid(row=16,column=2)
    Button(master, text="Browse",command=lambda: getFile(filename,pathlabel)).grid(row=4,column=1,sticky=W)
    

    #Create Bot Box
    Label(master, text="Bots").grid(row=15,column=0,columnspan=2)
    bots.createListBox()

    #Bat path
    Label(master, text=".bat Location").grid(row=16,column=3,sticky=W)
    Button(master, text="Browse",command=lambda: getDir(dirname,dirlabel)).grid(row=16,column=3,sticky=E,padx=(0,10))
    dirlabel = Label(master, text="",width = 20)
    dirlabel.grid(row=17, column=3, pady=10,sticky=W)
    Label(master, text=".bat Name").grid(row=18,column=3,sticky=W)
    wbatname = Entry(master, textvariable=batname, width=13)
    wbatname.grid(row=18,column=3,padx=(60,0))
    
    


    
    mainloop()
class FileName:
    def __init__(self):
        self.name = None

class ListBox:
    def __init__(self,master,row,column,columnspan,height,rowspan,width):
        self.master = master
        self.elements = []
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.height = height
        self.lb = None
        self.width = width
        

    def createListBox(self):
        self.lb = Listbox(self.master, width=self.width, height=self.height)
        self.lb.grid(row = self.row, column = self.column,\
                     columnspan=self.columnspan,rowspan=self.rowspan, pady=10, padx=5)
    def deleteElements(self):
        self.lb.delete(0,END)
        self.elements = []

    def updateElements(self):
        self.lb.delete(0,END)
        for element in self.elements:
            self.lb.insert(END,element)

    def insertElement(self,element):
        self.elements.append(element)
        self.updateElements()

    def getSelectedElement(self):
        return self.lb.get(self.lb.curselection()[0])

    def selected(self):
        if self.lb.curselection():
            return True
        return False

    def getIndexOfSelected(self):
        return self.lb.curselection()[0]

    def deleteSelected(self):
        if self.selected():
            index = self.getIndexOfSelected()
            self.lb.delete(index)
            self.elements.pop(index)

def addProxy(proxies,ip,port,proxyname,proxypass,wip,wport,wname,wpass):
    check = checkProxy(ip,port,proxyname,proxypass)
    if check:
        error = "Missing: "
        for field in check:
            if check[-1] != field:
                error += field + ","
            else:
                error += field
        messagebox.showinfo("Missing Fields",error)
        return
    proxies.insertElement(ip.get()+":"+port.get()+":"+proxyname.get()+":"+proxypass.get())
    wip.delete(0,END)

def addBot(bots,proxies,botusername,botpassword,botpin,wbname,wbpass,wbpin,botworld,botscript,botparam):
    check = checkBot(botusername,botpassword)
    if check:
        error = "Missing: "
        for field in check:
            if check[-1] != field:
                error += field + ","
            else:
                error += field
        messagebox.showinfo("Missing Fields",error)
        return
    result = botusername.get()+":"+botpassword.get()
    if botpin.get():
        result += ":" + botpin.get()
    else:
        result += ":0000"
    if proxies.selected():
        result += " -proxy "+proxies.getSelectedElement()
    if botscript.get():
        result += " -script " + botscript.get()
        if botparam:
            result += ":" + botparam.get()
        else:
            result += ":0"
    if botworld.get():
        result += " -world " + botworld.get()
        
    bots.insertElement(result)
    wbname.delete(0,END)
    wbpass.delete(0,END)
    wbpin.delete(0,END)

def getFile(filename,pathlabel):
    filename.name = fd.askopenfilename()
    if(filename.name):
        pathlabel.config(text="Path: " + filename.name)

def getDir(dirname,dirlabel):
    dirname.name = fd.askdirectory()
    if(dirname.name):
        dirlabel.config(text=dirname.name)

def makeBat(pathlabel,lowcpu,lowresource,username,password,bots,batname,dirname,filename):
    check = checkFields(username,password,filename,dirname,batname,bots)
    if check:
        error = "Missing: "
        for field in check:
            if check[-1] != field:
                error += field + ","
            else:
                error += field
        messagebox.showinfo("Missing Fields",error)
        return
    outfile = open(dirname.name+"/"+batname.get()+".bat","w").close()
    outfile = open(dirname.name+"/"+batname.get()+".bat","w")
    result = "java -jar \""
    result += pathlabel.cget("text")[6:] + "\""
    if lowcpu.get() or lowresource.get():
        result += " -allow "
    if lowcpu.get():
        result +="lowcpu,"
    if lowresource.get():
        result += "lowresource"
    result += " -login " + username.get() + ":" + password.get() + " -bot "
    for bot in bots.elements:
        outfile.write(result + bot + "\n")
    outfile.close()

def checkFields(username,password,filename,dirname,batname,bots):
    check = []
    if not username.get():
        check.append("Username")
    if not password.get():
        check.append("Password")
    if not filename.name:
        check.append("OSBot Path")
    if not batname.get():
        check.append(".bat Name")
    if not dirname.name:
        check.append(".bat Location")
    if not bots.elements:
        check.append("Bots")
    return check;

def checkProxy(ip,port,proxyname,proxypass):
    check=[]
    if not ip.get():
        check.append("IP")
    if not port.get():
        check.append("Port")
    if not proxyname.get():
        check.append("Name")
    if not proxypass.get():
        check.append("Password")
    return check

def checkBot(botusername,botpassword):
    check=[]
    if not botusername.get():
        check.append("Username")
    if not botpassword.get():
        check.append("Password")
    return check
        

    
        
if __name__ == '__main__':
    initGUI()
        