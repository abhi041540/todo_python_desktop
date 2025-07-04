import time as tm
import FreeSimpleGUI as sg
with open("todo.txt","w") as wf:
    pass
def getdata():
    with open("todo.txt","r") as rf:
        return rf.readlines()

lable=sg.Text("Type in a ToDo",text_color="black",font=["Bold",18])
inputfield=sg.InputText(tooltip="enter a todo",key="textfield")
clock=sg.Text("",key="clock")
add_btn=sg.Button("Add")
Exit_btn=sg.Button("Exit")
edit_btn=sg.Button("Edit")
delete_btn=sg.Button("Delete")
todo_list=sg.Listbox(values=getdata(),key="list",size=(45,10),enable_events=True)
window=sg.Window("My Todo GUI",layout=[[clock],[lable,inputfield,add_btn],
                                       [todo_list],[edit_btn,delete_btn,Exit_btn]]
                 ,font=["Arial",15])
while(True):
    event,value = window.read(timeout=200)
    window["clock"].update(tm.strftime("%D(%H:%M:%S)"))
    # print(event)
    # print(value)
    match event:
        case "Add":
            if(len(value["textfield"].strip())>0):
                with open("todo.txt","a") as wf:
                    wf.write(value["textfield"]+"\n")
                    wf.close()
                window["list"].update(values=getdata())
                window["textfield"].update("")
        case "Edit":
             if value["textfield"]!= "" and value["list"][0] != "":
                 tval=value["list"][0]
                 uval=value["textfield"]
                 with open("todo.txt","r") as rf:
                     lst=rf.readlines()
                     for ind,l in enumerate(lst):
                         if l==tval:
                             lst[ind]=uval+"\n"
                             break
                     with open("todo.txt","w") as wf:
                         wf.writelines(lst)
                         wf.close()
                     rf.close()
                 window["list"].update(values=getdata())
             window["textfield"].update("")
        case "list":
            window["textfield"].update(value["list"][0].replace("\n",""))
        case "Delete":
                if len(value["list"])>0 and value["list"][0] != "":
                    tval = value["list"][0]
                    with open("todo.txt", "r") as rf:
                        lst = rf.readlines()
                        for ind, l in enumerate(lst):
                            if l == tval:
                                lst.remove(lst[ind])
                                break
                        with open("todo.txt", "w") as wf:
                            wf.writelines(lst)
                            wf.close()
                        rf.close()
                    window["list"].update(values=getdata())
                    window["textfield"].update("")
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
