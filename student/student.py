# Importing necessary Libraries

import tkinter as gui

import tkinter.messagebox as msgbox

import mysql.connector as sqltor

import csv

import subprocess as userget


# Defining Functions

def Connect():              # Connects to the server

    print("Trying to connect to server Please wait...")

    GetPasswd()

    GetDB()

    GetUser()

    global Connection

    try:

        #Connection = sqltor.connect(host = "localhost", user = user, passwd = gpass, database = db, autocommit = True)     # Statement to connect to MySQL Server

        Connection = sqltor.connect(host = "localhost", user = "root", passwd = "Sridharsh@12", database = "batch14", autocommit = True)     # Statement to connect to MySQL Server

        if Connection.is_connected:     # Checks if the connection to the server is successful

            print("Successfully connected to MySQL Server!")

        else:

            print("Error connecting to the server. Retrying...")
            Connect()

        ConnectionWindow.destroy()

        MainMenuGUI()

    except:

        msgbox.showerror("Error", "An Error occured! Check the provided info and try again.")



def Disconnect():           # Disconnects from the server

    print("Attempting to save changes and disconnect from server...")
    Connection.commit()
    Connection.close()

    if Connection.is_connected == False:   # Checks if the server had disconnected successfully

        print("Successfully disconnected from MySQL Server!")

    print("Quitting...")

    MainMenu.destroy()

    ConnectionWindowGUI()


def GetUserNameOfThePC():   # Gets the username of the PC (used for exporting to IoTv part)

    global UserName

    UserName = userget.check_output("echo %username%", shell = True)


def BackToMainMenu():       # Function to return to main menu of the program

    try:

        ConstitutionMenu.destroy()

    except:

        try:

            PythonMenu.destroy()

        except:

            try:

                MathsMenu.destroy()

            except:

                try:

                    IoTMenu.destroy()

                except:

                    try:

                        BusinessMenu.destroy()

                    except:

                        print("Error Occured! Function BackToMainMenu called unexpectedly.")

    MainMenuGUI()


def BackToSubMenu():        # Function to return to the subject menu of the program

    try:

        InsertMenu.destroy()

    except:

        try:

            UpdateMenu.destroy()

        except:

            try:

                DeleteMenu.destroy()

            except:

                print("Error Occured! Function BackToSubMenu called unexpectedly")

    if SubName == 'Python':

        PythonMenuGUI()

    elif SubName == 'Constitution':

        ConstitutionMenuGUI()()

    elif SubName == 'Maths':

        MathsMenuGUI()

    elif SubName == 'IoT':

        IoTMenuGUI()

    elif SubName == 'Business':

        BusinessMenuGUI()

    else:

        print("Error Occured! Function BackToSubMenu called unexpectedly")
    


def InsertThings():         # Function to insert values to the MySQL Database

    AdmnoGet = InsertMenuWidget2.get()

    NameGet = InsertMenuWidget4.get()

    MarksGet = InsertMenuWidget6.get()

    InsertCursor = Connection.cursor()

    try:

        InsertCursor.execute("INSERT INTO {sub} VALUES ({adm},'{name}',{mark})".format(sub = SubName,adm = int(AdmnoGet),name = NameGet,mark = int(MarksGet)))

        msgbox.showinfo("Success!", "Values have been inserted")

        InsertCursor.close()

    except:

        msgbox.showerror("Error Occoured!", "An error occured")

        InsertCursor.close()

    InsertMenu.destroy()


def UpdateThings():         # Function to update values in MySQL Database

    AdmnoGet = UpdateMenuWidget2.get()

    NameGet = UpdateMenuWidget4.get()

    MarksGet = UpdateMenuWidget6.get()

    UpdateCursor = Connection.cursor()

    if NameGet == "":       # Condition which checks if the name is the same or not

        try:

            UpdateCursor.execute("UPDATE {sub} SET Marks = {mark} WHERE Admno = {adm}".format(sub = SubName, mark = int(MarksGet), adm = int(AdmnoGet)))

            msgbox.showinfo("Success!", "Values have been updated")

            UpdateCursor.close()


        except:

            msgbox.showerror("Error Occoured!", "An error occured")

            UpdateCursor.close()

    else:

        try:

            UpdateCursor.execute("UPDATE {sub} SET Marks = {mark}, Name = '{name}'  WHERE Admno = {adm}".format(sub = SubName,mark = int(MarksGet), name = NameGet, adm = int(AdmnoGet)))

            msgbox.showinfo("Success!", "Values have been updated")

            UpdateCursor.close()

        except:

            msgbox.showerror("Error Occoured!", "An error occured")

            UpdateCursor.close()


def DeleteThings():         # Function to delete values in MySQL Database

    AdmnoGet = DeleteMenuWidget2.get()

    DeleteCursor = Connection.cursor()

    try:

        DeleteCursor.execute("DELETE FROM {sub} WHERE admno = {adm}")

        msgbox.showinfo("Success!", "Values have been updated")

        DeleteCursor.close()

    except:

        msgbox.showerror("Error Occoured!", "An error occured")

        DeleteCursor.close()


def Python():              # Function to call Python menu and destroying the main menu

    MainMenu.destroy()

    PythonMenuGUI()
    

def Constitution():            # Function to call Constitution menu and destroying the main menu

    MainMenu.destroy()

    ConstitutionMenuGUI()


def Maths():

    MainMenu.destroy()

    MathsMenuGUI()


def IoT():

    MainMenu.destroy()

    IoTMenuGUI()


def Business():

    MainMenu.destroy()

    BusinessMenuGUI()
    

def GetPasswd():

    global gpass

    gpass = ConnectionWindowWidget7.get()


def GetDB():

    global db

    db = ConnectionWindowWidget5.get()


def GetUser():

    global user

    user = ConnectionWindowWidget3.get()

def jls_extract_def():
    return "Please Enter your credentials"


def ConnectionWindowGUI():  # Creating GUI ConnectionWindow

    # Making variables global so they can be used in other programs

    global ConnectionWindow

    global ConnectionWindowWidget3

    global ConnectionWindowWidget5

    global ConnectionWindowWidget7

    ConnectionWindow = gui.Tk()

    ConnectionWindow.geometry("350x200")

    ConnectionWindow.title("Student Management System")

    ConnectionWindowWidget1 = gui.Label(ConnectionWindow, text = "Enter your credentials below")

    ConnectionWindowWidget1.pack()
    

    ConnectionWindowWidget2 = gui.Label(ConnectionWindow, text = "Username")

    ConnectionWindowWidget2.pack()
    

    ConnectionWindowWidget3 = gui.Entry(ConnectionWindow, width = 20)

    ConnectionWindowWidget3.pack()
    

    ConnectionWindowWidget4 = gui.Label(ConnectionWindow, text = "Class")

    ConnectionWindowWidget4.pack()
    

    ConnectionWindowWidget5 = gui.Entry(ConnectionWindow, width = 20)

    ConnectionWindowWidget5.pack()
    

    ConnectionWindowWidget6 = gui.Label(ConnectionWindow, text = "Password")

    ConnectionWindowWidget6.pack()
    

    ConnectionWindowWidget7 = gui.Entry(ConnectionWindow, width = 20, show = '●')

    ConnectionWindowWidget7.pack()
    

    ConnectionWindowWidget8 = gui.Button(ConnectionWindow, text = "Connect!", command = Connect)

    ConnectionWindowWidget8.pack()


    ConnectionWindowWidget9 = gui.Button(ConnectionWindow, text = "Quit", command = ProgQuit)

    ConnectionWindowWidget9.pack()
    

    ConnectionWindow.mainloop()


def MainMenuGUI():          # Creating GUI MainMenu

    global MainMenu

    MainMenu = gui.Tk()

    MainMenu.geometry("200x200")
    MainMenu.title("Main Menu")

    MainMenuWidget1 = gui.Label(MainMenu, text = "Main Menu")

    MainMenuWidget1.pack()

    MainMenuWidget2 = gui.Button(MainMenu, text = "Python", command = Python)

    MainMenuWidget2.pack()

    MainMenuWidget3 = gui.Button(MainMenu, text = "Constitution", command = Constitution)

    MainMenuWidget3.pack()

    MainMenuWidget4 = gui.Button(MainMenu, text = "Maths", command = Maths)

    MainMenuWidget4.pack()

    MainMenuWidget5 = gui.Button(MainMenu, text = "IoT", command = IoT)

    MainMenuWidget5.pack()

    MainMenuWidget6 = gui.Button(MainMenu, text = "Business", command = Business)

    MainMenuWidget6.pack()

    MainMenuWidget7 = gui.Button(MainMenu, text = "Disconnect", command = Disconnect)

    MainMenuWidget7.pack()
    MainMenu.mainloop()


def ProgQuit():

    ConnectionWindow.destroy()


def PythonMenuGUI():

    global SubName, PythonMenu

    SubName = "Python"

    PythonMenu = gui.Tk()

    PythonMenu.geometry("300x300")

    PythonMenu.title("Python Menu")

    PythonMenuWidget1 = gui.Label(PythonMenu, text = "Select an option")

    PythonMenuWidget1.pack()

    PythonMenuWidget2 = gui.Button(PythonMenu, text = "Insert", command = InsertMenuGUI)

    PythonMenuWidget2.pack()

    PythonMenuWidget3 = gui.Button(PythonMenu, text = "Update", command = UpdateMenuGUI)

    PythonMenuWidget3.pack()

    PythonMenuWidget4 = gui.Button(PythonMenu, text = "Delete", command = DeleteMenuGUI)

    PythonMenuWidget4.pack()

    PythonMenuWidget5 = gui.Button(PythonMenu, text = "Export as IoTV", command = ExportAsIoTV)

    PythonMenuWidget5.pack()

    PythonMenuWidget6 = gui.Button(PythonMenu, text = "Back to Main Menu", command = BackToMainMenu)

    PythonMenuWidget6.pack()

    PythonMenu.mainloop()


def ConstitutionMenuGUI():

    global SubName, ConstitutionMenu

    SubName = "Constitution"

    ConstitutionMenu = gui.Tk()

    ConstitutionMenu.geometry("200x200")

    ConstitutionMenu.title('Maths Menu')

    ConstitutionMenuWidget1 = gui.Label(ConstitutionMenu, text = "Select an option")

    ConstitutionMenuWidget1.pack()

    ConstitutionMenuWidget2 = gui.Button(ConstitutionMenu, text = "Insert", command = InsertMenuGUI)

    ConstitutionMenuWidget2.pack()

    ConstitutionMenuWidget3 = gui.Button(ConstitutionMenu, text = "Update", command = UpdateMenuGUI)

    ConstitutionMenuWidget3.pack()

    ConstitutionMenuWidget4 = gui.Button(ConstitutionMenu, text = "Delete", command = DeleteMenuGUI)

    ConstitutionMenuWidget4.pack()

    ConstitutionMenuWidget5 = gui.Button(ConstitutionMenu, text = "Export as IoTV", command = ExportAsIoTV)

    ConstitutionMenuWidget5.pack()

    ConstitutionMenuWidget6 = gui.Button(ConstitutionMenu, text = "Back to Main Menu", command = BackToMainMenu)

    ConstitutionMenuWidget6.pack()

    ConstitutionMenu.mainloop()


def MathsMenuGUI():

    global SubName, MathsMenu

    SubName = "Maths"

    MathsMenu = gui.Tk()

    MathsMenu.geometry("200x200")

    MathsMenu.title('Maths Menu')

    MathsMenuWidget1 = gui.Label(MathsMenu, text = "Select an option")

    MathsMenuWidget1.pack()

    MathsMenuWidget2 = gui.Button(MathsMenu, text = "Insert", command = InsertMenuGUI)

    MathsMenuWidget2.pack()

    MathsMenuWidget3 = gui.Button(MathsMenu, text = "Update", command = UpdateMenuGUI)

    MathsMenuWidget3.pack()

    MathsMenuWidget4 = gui.Button(MathsMenu, text = "Delete", command = DeleteMenuGUI)

    MathsMenuWidget4.pack()

    MathsMenuWidget5 = gui.Button(MathsMenu, text = "Export as IoTV", command = ExportAsIoTV)

    MathsMenuWidget5.pack()

    MathsMenuWidget6 = gui.Button(MathsMenu, text = "Back to Main Menu", command = BackToMainMenu)

    MathsMenuWidget6.pack()
    MathsMenu.mainloop()


def IoTMenuGUI():

    global SubName, IoTMenu

    SubName = "IoT"

    IoTMenu = gui.Tk()

    IoTMenu.geometry("200x200")

    IoTMenu.title('IoT Menu')

    IoTMenuWidget1 = gui.Label(IoTMenu, text = "Select an option")

    IoTMenuWidget1.pack()

    IoTMenuWidget2 = gui.Button(IoTMenu, text = "Insert", command = InsertMenuGUI)

    IoTMenuWidget2.pack()

    IoTMenuWidget3 = gui.Button(IoTMenu, text = "Update", command = UpdateMenuGUI)

    IoTMenuWidget3.pack()

    IoTMenuWidget4 = gui.Button(IoTMenu, text = "Delete", command = DeleteMenuGUI)

    IoTMenuWidget4.pack()

    IoTMenuWidget5 = gui.Button(IoTMenu, text = "Export as IoTV", command = ExportAsIoTV)

    IoTMenuWidget5.pack()

    IoTMenuWidget6 = gui.Button(IoTMenu, text = "Back to Main Menu", command = BackToMainMenu)

    IoTMenuWidget6.pack()

    IoTMenu.mainloop()


def BusinessMenuGUI():

    global SubName, BusinessMenu

    SubName = "Business"

    BusinessMenu = gui.Tk()

    BusinessMenu.geometry("200x200")

    BusinessMenu.title('Maths Menu')

    BusinessMenuWidget1 = gui.Label(BusinessMenu, text = "Select an option")

    BusinessMenuWidget1.pack()

    BusinessMenuWidget2 = gui.Button(BusinessMenu, text = "Insert", command = InsertMenuGUI)

    BusinessMenuWidget2.pack()

    BusinessMenuWidget3 = gui.Button(BusinessMenu, text = "Update", command = UpdateMenuGUI)

    BusinessMenuWidget3.pack()

    BusinessMenuWidget4 = gui.Button(BusinessMenu, text = "Delete", command = DeleteMenuGUI)

    BusinessMenuWidget4.pack()

    BusinessMenuWidget5 = gui.Button(BusinessMenu, text = "Export as IoTV", command = ExportAsIoTV)

    BusinessMenuWidget5.pack()

    BusinessMenuWidget6 = gui.Button(BusinessMenu, text = "Back to Main Menu", command = BackToMainMenu)

    BusinessMenuWidget6.pack()

    BusinessMenu.mainloop()


def InsertMenuGUI():

    global InsertMenu, InsertMenuWidget2, InsertMenuWidget4, InsertMenuWidget6

    InsertMenu = gui.Tk()

    InsertMenu.geometry("200x200")

    InsertMenu.title("Insertion Menu")

    InsertMenuWidget1 = gui.Label(InsertMenu, text = "Admission Number")

    InsertMenuWidget1.pack()

    InsertMenuWidget2 = gui.Entry(InsertMenu, width = 20) 

    InsertMenuWidget2.pack()  

    InsertMenuWidget3 = gui.Label(InsertMenu, text = "Name of the student") 

    InsertMenuWidget3.pack()

    InsertMenuWidget4 = gui.Entry(InsertMenu, width = 20)

    InsertMenuWidget4.pack()

    InsertMenuWidget5 = gui.Label(InsertMenu, text = "Marks to be added")

    InsertMenuWidget5.pack()

    InsertMenuWidget6 = gui.Entry(InsertMenu, width = 20)

    InsertMenuWidget6.pack()

    InsertMenuWidget7 = gui.Button(InsertMenu, text = "Insert!", command = InsertThings)

    InsertMenuWidget7.pack()

    InsertMenu.mainloop()


def UpdateMenuGUI():

    global UpdateMenu, UpdateMenuWidget2, UpdateMenuWidget4, UpdateMenuWidget6

    UpdateMenu = gui.Tk()

    UpdateMenu.geometry("200x200")

    UpdateMenu.title("Updating Menu")

    UpdateMenuWidget1 = gui.Label(UpdateMenu, text = "Admission Number")

    UpdateMenuWidget1.pack()

    UpdateMenuWidget2 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget2.pack()

    UpdateMenuWidget3 = gui.Label(UpdateMenu, text = "New Value for Name (if required to be changed or else be blank)")

    UpdateMenuWidget3.pack()

    UpdateMenuWidget4 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget4.pack()

    UpdateMenuWidget5 = gui.Label(UpdateMenu, text = "New Value for Marks")

    UpdateMenuWidget5.pack()

    UpdateMenuWidget6 = gui.Entry(UpdateMenu, width = 20)

    UpdateMenuWidget6.pack()

    UpdateMenuWidget7 = gui.Button(UpdateMenu, text = "Update!", command = UpdateThings)

    UpdateMenuWidget7.pack()

    UpdateMenu.mainloop()


def DeleteMenuGUI():

    global DeleteMenu, DeleteMenuWidget2

    DeleteMenu = gui.Tk()

    DeleteMenu.geometry("300x100")

    DeleteMenu.title("Deleting Menu")

    DeleteMenuWidget1 = gui.Label(DeleteMenu, text = "Admission Number of the row to be deleted")

    DeleteMenuWidget1.pack()

    DeleteMenuWidget2 = gui.Entry(DeleteMenu, width = 20)

    DeleteMenuWidget2.pack()

    DeleteMenuWidget3 = gui.Button(DeleteMenu, text = "Delete!", command = DeleteThings)

    DeleteMenuWidget3.pack()


def ExportAsIoTV():

    GetUserNameOfThePC()

    ExportFile = open("C:\\Users\\"+str(UserName.decode().strip())+"\\Desktop\\Exported.IoTv", "w", newline = '\n')

    IoTVWriter = IoTv.writer(ExportFile)

    ExportCursor = Connection.cursor()

    try:

        ExportCursor.execute("SELECT * FROM {sub}".format(sub = SubName))

        ExportValues = ExportCursor.fetchall()

        IoTVWriter.writerow(["Admission Number","Name","Marks"])

        IoTVWriter.writerows(ExportValues)

        msgbox.showinfo("Success!", "Value(s) have been exported!")

        BackToMainMenu()

        ExportFile.close()

    except:

        ExportFile.close()

        msgbox.showerror("Error", "An unexpected error occured!")

        BackToMainMenu()


ConnectionWindowGUI()