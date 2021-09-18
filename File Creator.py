from tkinter import *
from tkinter import messagebox
import os

# Main Menu Window

def mainMenu():
    
    main_menu = Tk()
    main_menu.title("File Creator | Main Menu")
    main_menu.geometry('483x298') 
    main_menu.resizable(0,0)
    main_menu.config(background = '#F7F7F7')
    
    main_window.destroy()
    
    create_file_button = Button(main_menu,
                          text = "Create File",
                          font = ('Roboto', 10),
                          fg = 'white',
                          bg = '#5CB85C',
                          activeforeground = 'white',
                          activebackground = '#5CB85C',
                          bd = 0,
                          cursor = 'hand2',
                          padx = 50,
                          pady = 15,
                          command = createfileWindow
                          )
    create_file_button.place(x = 36, y = 72)
    
    read_file_button = Button(main_menu,
                              text = "Read File",
                              font = ('Roboto', 10),
                              fg = 'white',
                              bg = '#0275D8',
                              activeforeground = 'white',
                              activebackground = '#0275D8',
                              bd = 0,
                              cursor = 'hand2',
                              padx = 55,
                              pady = 15,
                              command = readfileWindow
                              )
    read_file_button.place(x = 242, y = 72)
    
    delete_file_button = Button(main_menu,
                                text = "Delete File",
                                font = ('Roboto', 10),
                                fg = 'white',
                                bg = '#D9534F',
                                activeforeground = 'white',
                                activebackground = '#D9534F',
                                bd = 0,
                                cursor = 'hand2',
                                padx = 51,
                                pady = 15,
                                command = deletefileWindow
                                )
    delete_file_button.place(x = 36, y = 147)
    
    about_button = Button(main_menu,
                              text = "About",
                              font = ('Roboto', 10),
                              fg = 'white',
                              bg = '#F0AD4E',
                              activeforeground = 'white',
                              activebackground = '#F0AD4E',
                              bd = 0,
                              cursor = 'hand2',
                              padx = 65,
                              pady = 15,
                              command = aboutWindow
                              )
    about_button.place(x = 242, y = 147)
    
# Create File Window
    
def createfileWindow():
    
    create_file_window = Tk()
    create_file_window.title("File Creator | Create File")
    create_file_window.geometry('437x277')
    create_file_window.resizable(0,0)
    create_file_window.config(background = '#F7F7F7')
    
    create_label = Label(create_file_window,
                         text = "Create a file name",
                         font = ('Roboto', 11),
                         fg = '#070707',
                         bg = '#F7F7F7'
                         )
    create_label.place(x = 49, y = 83)
    
    global create_entry
    
    create_entry = Entry(create_file_window,
                         font = ('Roboto', 11)
                         )
    create_entry.place(x = 187, y = 81)
    
    create_button = Button(create_file_window,
                           text = "Create",
                           font = ('Roboto', 10),
                           padx = 50,
                           pady = 10,
                           bd = 0,
                           cursor = 'hand2',
                           fg = 'white',
                           bg = '#5CB85C',
                           activeforeground = 'white',
                           activebackground = '#5CB85C',
                           command = createButton
                           )
    create_button.place(x = 51, y = 135)
    
    reset_button = Button(create_file_window,
                          text = "Reset",
                          font = ('Roboto', 10),
                          padx = 45,
                          pady = 10,
                          bd = 0,
                          cursor = 'hand2',
                          fg = 'white',
                          bg = '#D9534F',
                          activeforeground = 'white',
                          activebackground = '#D9534F',
                          command = resetButton
                          )
    reset_button.place(x = 225, y = 135)
    
# Create File Window Reset Button
    
def resetButton():
    
    message = messagebox.askquestion(title = "Reset", message = "Are you sure want to reset ?")
    
    if message == 'yes':
        create = create_entry.get()
        create_entry.delete(0, len(create))
        
# Create File Window Create Button
    
def createButton():
    
    try:
        
        created_file = open(create_entry.get(), 'x')
        created_file.close()
        
        if created_file:
            messagebox.showinfo(title = "File Creator", message = "File was successfully created !")
        else:
            messagebox.showerror(title = "File Creator", message = "Sorry, something went wrong :(")
    
    except FileExistsError:
        
        messagebox.showwarning(title = "File Already Exists Warning", message = create_entry.get() + " already exists")
        
    except FileNotFoundError:
        
        messagebox.showwarning(title = "Empty Field", message = "You must fill field to create a file")
        
# Read File Window
        
def readfileWindow():
    
    read_file_window = Tk()
    read_file_window.title("File Creator | Read File")
    read_file_window.geometry('422x521')
    read_file_window.resizable(0,0)
    read_file_window.config(background = '#F7F7F7')
    
    file_name_label = Label(read_file_window,
                            text = "Enter a file name",
                            font = ('Roboto', 11),
                            fg = '#070707',
                            bg = '#F7F7F7'
                            )
    file_name_label.place(x = 32, y = 79)
    
    global file_name_entry
    global file_content_text
    
    file_name_entry = Entry(read_file_window,
                            font = ('Roboto', 11)
                            )
    file_name_entry.place(x = 164, y = 76)
    
    file_content_label = Label(read_file_window,
                               text = "File Contents:",
                               font = ('Roboto', 11),
                               fg = '#070707',
                               bg = '#F7F7F7'
                               )
    file_content_label.place(x = 32, y = 132)
    
    file_content_text = Text(read_file_window,
                             font = ('Roboto', 11),
                             height = 12,
                             width = 43
                             )
    file_content_text.place(x = 35, y = 161)
    
    read_button = Button(read_file_window,
                         text = "Read",
                         font = ('Roboto', 10),
                         fg = 'white',
                         bg = '#0275D8',
                         activeforeground = 'white',
                         activebackground = '#0275D8',
                         cursor = 'hand2',
                         bd = 0,
                         padx = 50,
                         pady = 10,
                         command = readButton
                         )
    read_button.place(x = 35, y = 399)
    
    reset_read_button = Button(read_file_window,
                               text = "Reset All",
                               font = ('Roboto', 10),
                               fg = 'white',
                               bg = '#D9534F',
                               activeforeground = 'white',
                               activebackground = '#D9534F',
                               cursor = 'hand2',
                               bd = 0,
                               padx = 58,
                               pady = 10,
                               command = resetreadButton  
                               )
    reset_read_button.place(x = 212, y = 399)
    
# Read File Window Reset Button
    
def resetreadButton():
    
    message_read_reset = messagebox.askquestion(title = "Reset", message = "Are you sure want to reset ?")
    
    if message_read_reset == 'yes':
        file_name = file_name_entry.get()
        file_content = file_content_text.get("1.0", END)
    
        file_name_entry.delete(0, len(file_name))
        file_content_text.delete("1.0", END)
        
# Read File Window Read Button        
    
def readButton():

    try:
        read_file = open(file_name_entry.get(), 'r')
    
        read_info = (file_content_text.insert("1.0", read_file.read()))
    
        read_file.close()
        
    except FileNotFoundError:
        
        messagebox.showerror(title = "File Not Found Error", message = file_name_entry.get() + " not found")
        
# Delete File Window 
        
def deletefileWindow():
    
    delete_file_window = Tk()
    delete_file_window.title("File Creator | Delete File")
    delete_file_window.geometry('439x307')
    delete_file_window.resizable(0, 0)
    delete_file_window.config(background = '#F7F7F7')
    
    delete_label = Label(delete_file_window,
                         text = "Enter a file name",
                         font = ('Roboto', 11 ),
                         fg = '#070707',
                         bg = '#F7F7F7'
                         )
    delete_label.place(x = 43, y = 90)
    
    global delete_entry
    
    delete_entry = Entry(delete_file_window,
                         font = ('Roboto', 11)
                         )
    delete_entry.place(x = 174, y = 88)
    
    delete_button = Button(delete_file_window,
                           text = "Delete",
                           font = ('Roboto', 10),
                           fg = 'white',
                           bg = '#D9534F',
                           activeforeground = 'white',
                           activebackground = '#D9534F',
                           bd = 0,
                           cursor = 'hand2',
                           padx = 55,
                           pady = 15,
                           command = deleteButton
                           )
    delete_button.place(x = 46, y = 149)
    
    reset_delete_button = Button(delete_file_window,
                                text = "Reset",
                                font = ('Roboto', 10),
                                fg = 'white',
                                bg = '#D9534F',
                                activeforeground = 'white',
                                activebackground = '#D9534F',
                                bd = 0,
                                cursor = 'hand2',
                                padx = 55,
                                pady = 15,
                                command = resetdeleteButton
                                 )
    reset_delete_button.place(x = 213, y = 149)
    
# Delete File Window Delete Button
    
def deleteButton():
    
    try:
        
        delete = delete_entry.get()
        os.remove(delete)
    
    except FileNotFoundError:
        
        messagebox.showerror(title = "File Deleted", message = delete_entry.get() + " is already deleted")
        
# Delete File Window Reset Button
    
def resetdeleteButton():
    
    message_delete = messagebox.askquestion(title = "Reset", message = "Are you sure want to reset ?")
    
    if message_delete == 'yes':
        reset = delete_entry.get()
        delete_entry.delete(0, len(reset))
        
# About Window
        
def aboutWindow():
    
    about_window = Tk()
    about_window.title("File Creator | About")
    about_window.geometry('553x423')
    about_window.resizable(0,0)
    about_window.config(background = '#F7F7F7')
    
    about_title_label = Label(about_window,
                              text = "About File Creator",
                              font = ('Roboto', 14, 'bold'),
                              fg = '#070707',
                              bg = '#F7F7F7'
                              )
    about_title_label.place(x = 27, y = 39)
    
    about_sub_label = Label(about_window,
                            text = "This app is about creating your file in one specific path. With this\napp you may create, read, and delete a file. It is absolutely free.",
                            font = ('Roboto', 12),
                            fg = '#070707',
                            bg = '#F7F7F7'
                            )
    about_sub_label.place(x = 27, y = 71)
    
    about_app_name_label = Label(about_window,
                                 text = "Application",
                                 font = ('Roboto', 14, 'bold'),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    about_app_name_label.place(x = 27, y = 143)
    
    about_app_name_sub_label = Label(about_window,
                                 text = "File Creator",
                                 font = ('Roboto', 12),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    about_app_name_sub_label.place(x = 27, y = 177)
    
    developer_app_name_label = Label(about_window,
                                 text = "Developer",
                                 font = ('Roboto', 14, 'bold'),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    developer_app_name_label.place(x = 27, y = 211)
    
    about_app_name_sub_label = Label(about_window,
                                 text = "Gabbierutt",
                                 font = ('Roboto', 12),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    about_app_name_sub_label.place(x = 27, y = 242)
    
    version_label = Label(about_window,
                                 text = "Version",
                                 font = ('Roboto', 14, 'bold'),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    version_label.place(x = 27, y = 286)
    
    version_sub_label = Label(about_window,
                                 text = "Version 1.0 BETA",
                                 font = ('Roboto', 12),
                                 fg = '#070707',
                                 bg = '#F7F7F7'
                                 )
    version_sub_label.place(x = 27, y = 319)
    
          
# Main Window 
    
main_window = Tk()
main_window.title("File Creator")
main_window.geometry('421x285')
main_window.resizable(0,0)
main_window.config(background = '#F7F7F7')

app_title_label = Label(main_window,
                        text = "File Creator",
                        font = ('Roboto', 21, 'bold'),
                        fg = '#070707',
                        bg = '#F7F7F7'
                        )
app_title_label.place(x = 132, y = 45)

app_subtitle_label = Label(main_window,
                           text = "Copyrights Gabbierutt 2021. All Rights Reserved",
                           font = ('Roboto', 9),
                           fg = '#88898D',
                           bg = '#F7F7F7'
                           )
app_subtitle_label.place(x = 84, y = 95)

open_button = Button(main_window,
                     text = "Open File Creator",
                     font = ('Roboto', 10),
                     fg = 'white',
                     bg = '#0275D8',
                     bd = 0,
                     cursor = 'hand2',
                     activeforeground = 'white',
                     activebackground = '#0275D8',
                     padx = 45,
                     pady = 15,
                     command = mainMenu
                     )
open_button.place(x = 106, y = 143)

main_window.mainloop()