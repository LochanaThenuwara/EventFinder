from Tkinter import *
import xml.etree.ElementTree as ET
import tkMessageBox


wx_file= open('C:/ProjectSE/parser/AISTargetListDialog.cpp','r')
map={'onclick':["wxEVT_COMMAND_BUTTON_CLICKED", "wxEVT_BUTTON","EVT_BUTTON"]}


def xmlParser(ui_name):
    tree = ET.parse("C:\wamp\www\BootstrapConverter\event.xml")
    root=tree.getroot()

    for ui in root.findall(ui_name):
        events = ui.findall('item')
        for i in events:
            e=i.find('event')
            method=i.find('method')
            print e.text
            event=e.text
            print method.text

            mapFunction(event)

            lineNo=findMethod(method.text)
            tkMessageBox.showinfo("Show Details",
                                  "Method Name is :   " + method.text + "\nEvent is:   " + event+ "\nMapped Bootstrap Event is:   "
                                  + mapFunction(event)+"\nLine no is:   " + str(lineNo))

#

def findMethod(method):
    count=0;
    for line in wx_file:
        if "void "+method in line:
            print line
            print count
            return count

        count=count+1


def mapFunction(event):
    return event


def show_entry_fields():

    ui_name=e1.get()
    print("UI name: %s" % ui_name)
    xmlParser(ui_name)





master = Tk()
Label(master, text="UI Obj Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
# e2 = Entry(master)

e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)


Button(master, text='Show Method', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)



mainloop( )