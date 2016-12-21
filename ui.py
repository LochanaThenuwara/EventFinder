from Tkinter import *
import xml.etree.ElementTree as ET
import tkMessageBox


# wx_file= open('C:/ProjectSE/WxLoginForm/WxLoginForm/FormLogin.cpp','r')
# wx_file = open('C:/ProjectSE/wxRegitrationForm/WxRegitrationForm/WxRegitrationForm/FormReg.cpp', 'r')
wx_file= open('C:/ProjectSE/OpenCPN/src/AISTargetListDialog.cpp','r')
# wx_file= open('C:/ProjectSE/parser/AISTargetListDialog.cpp','r')
# wx_file= open('C:/ProjectSE/parser/chart1.cpp','r')
map={'onclick':["wxEVT_COMMAND_BUTTON_CLICKED", "wxEVT_BUTTON","EVT_BUTTON","EVT_CHECKBOX","wxEVT_COMMAND_CHECKBOX_ CLICKED","EVT_RADIOBUTTON","wxEVT_COMMAND_ RADIOBUTTON_ SELECTED"],
     'onchange':["EVT_TEXT_ENTER","wxEVT_COMMAND_TEXT_ENTER"],
     'onkeyup':["wxEVT_COMMAND_TEXT_UPDATED","EVT_TEXT"]}


def xmlParser(ui_name):
    tree = ET.parse("C:\wamp\www\BootstrapConverter\event1.xml")
    root=tree.getroot()
    arrayItems=root.findall('item')

    for item in arrayItems:
        obj=item.findall(ui_name)
        for ui in obj:
            events = ui.findall('item')
            for i in events:
                e=i.find('event')
                method=i.find('method')
                print e.text,"999999999999"
                event=e.text
                print method.text

                mapFunction(event)

                lineNo=findMethod(method.text)
                tkMessageBox.showinfo("Show Details",
                                      "Method Name is :   " + method.text + "\nEvent is:   " + event+ "\nMapped Bootstrap Event is:   "
                                      + mapFunction(event)+"\nLine no is:   " + str(lineNo))

    #

def findMethod(method):
    count=1;
    print method,"xxxx"
    for line in wx_file:

        if "void "+method in line:
            print line
            print count
            return count

        count=count+1


def mapFunction(event):
    for key, value in map.iteritems():
        for i in range(0,len(value)):
            if event==value[i]:

                return key
            else:
                return ""


def show_entry_fields():

    ui_name=e1.get()
    print("UI name: %s" % ui_name)
    xmlParser(ui_name)

def show_objects():
    file=open("C:/ProjectSE/Parser/foundUi.txt",'r')
    for line in file:
        print line



master = Tk()
Label(master, text="UI Obj Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
# e2 = Entry(master)

e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)


Button(master, text='Show Object List', command=show_objects).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show Method', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button (master, text='Quit', command=master.quit).grid(row=3, column=2, sticky=W, pady=4)


mainloop( )