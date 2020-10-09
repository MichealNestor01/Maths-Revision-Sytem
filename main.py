# This file organises what the user sees when the prgram is actually running, it uses the modules in the programModules file to curate a user experience
from programModules import *
from gameEngine import *

# all of these functions are simple ones that just create interface objects and open the object's windows, they are all mostly identical functions and so
# I will only comment the first function fully
# create account is used to make the create account window
def createAccount():
    # app is an QApplication object which allows for graphical user interfaces
    app = QtWidgets.QApplication(sys.argv)
    # you first need to create a QMainWindow object that is the base window
    createAccountWindow = QtWidgets.QMainWindow()
    # ui is set to the interface object made with the classes in programModules
    ui = Ui_createAccountWindow()
    # then run the setup ui function of the interface object
    ui.setupUi(createAccountWindow)
    # now show the set up user interface
    createAccountWindow.show()
    # only end this subroutine when the user interface has closed
    app.exec_()


# log on is ued to make the log on windows
def logOn():
    app = QtWidgets.QApplication(sys.argv)
    logOnWindow = QtWidgets.QMainWindow()
    ui = Ui_logOnWindow()
    ui.setupUi(logOnWindow)
    logOnWindow.show()
    app.exec_()
    # this function returns data to the main menu
    return ui.returnData()


# set up creates a new account set up window
def setUp(userdata):
    app = QtWidgets.QApplication(sys.argv)
    firstTimeSetUp = QtWidgets.QMainWindow()
    ui = Ui_firstTimeSetUp(userdata)
    ui.setupUi(firstTimeSetUp)
    firstTimeSetUp.show()
    app.exec_()
    # this function needs to return whether or not the user's teacher is recognised and the userObject
    return (ui.selectedFunction, ui.userObject)


# forgot password creates forgot password windows
def forgotPassword():
    app = QtWidgets.QApplication(sys.argv)
    forgotPasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_forgotPasswordWindow()
    ui.setupUi(forgotPasswordWindow)
    forgotPasswordWindow.show()
    app.exec_()


# new teacher creates the new teacher set up window
def newTeacher(userObject):
    app = QtWidgets.QApplication(sys.argv)
    newTeacherSetup = QtWidgets.QMainWindow()
    ui = Ui_newTeacherSetup(userObject)
    ui.setupUi(newTeacherSetup)
    newTeacherSetup.show()
    app.exec_()
    # the window needs to be returned selected function as the user has the option to log
    # out rather than continue to the main menu
    return ui.selectedFunction


# main menu creates main menu windows
def mainMenu(userObject):
    app = QtWidgets.QApplication(sys.argv)
    mainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_mainMenuWindow(userObject)
    ui.setupUi(mainMenuWindow)
    mainMenuWindow.show()
    app.exec_()
    # the main menu returns the selected function and function data as the windows that it
    # causes to open needs specific data about user choices on the main menu like the chosen sprite
    return ui.selectedFunction, ui.functionData


# change usernmae creates the change username window
def changeUsername(userObject):
    app = QtWidgets.QApplication(sys.argv)
    changeUsernameWindow = QtWidgets.QMainWindow()
    ui = Ui_changeUsernameWindow(userObject)
    ui.setupUi(changeUsernameWindow)
    changeUsernameWindow.show()
    app.exec_()
    return ui.userObject


# change password creates the change password window
def changePassword(userObject):
    app = QtWidgets.QApplication(sys.argv)
    changePasswordWindow = QtWidgets.QMainWindow()
    ui = Ui_changePasswordWindow(userObject)
    ui.setupUi(changePasswordWindow)
    changePasswordWindow.show()
    app.exec_()


# update email creates the update email winodw
def updateEmail(userObject):
    app = QtWidgets.QApplication(sys.argv)
    updateEmailWindow = QtWidgets.QMainWindow()
    ui = Ui_updateEmailWindow(userObject)
    ui.setupUi(updateEmailWindow)
    updateEmailWindow.show()
    app.exec_()
    return ui.userObject


# teacher settings creates the teacher settings window
def teacherSettings(userObject):
    app = QtWidgets.QApplication(sys.argv)
    updateTeacherWindow = QtWidgets.QMainWindow()
    ui = Ui_updateTeacherWindow(userObject)
    ui.setupUi(updateTeacherWindow)
    updateTeacherWindow.show()
    app.exec_()
    return ui.selectedFunction, ui.teacherRecord[0]


# change teacher email creates the change teacher email window
def changeTeacherEmail(userObject, teacherRecord):
    app = QtWidgets.QApplication(sys.argv)
    changeTeacherEmailWindow = QtWidgets.QMainWindow()
    ui = Ui_changeTeacherEmailWindow(userObject, teacherRecord)
    ui.setupUi(changeTeacherEmailWindow)
    changeTeacherEmailWindow.show()
    app.exec_()
    return ui.userObject


# change teacher creates the change teacher window
def changeTeacher(userObject, teacherRecord):
    app = QtWidgets.QApplication(sys.argv)
    changeTeacherWindow = QtWidgets.QMainWindow()
    ui = Ui_changeTeacherWindow(userObject, teacherRecord)
    ui.setupUi(changeTeacherWindow)
    changeTeacherWindow.show()
    app.exec_()
    return ui.userObject


# game loads the game, in either revision mode or game mode depending on the parsed variables
def game(gameType, style, topic, userName):
    gameInstance(style, gameType, topic, userName)


# the entire program is ran from this main script, the interfaces are contained in loops which allows for the easiest way to
# move a user between interfaces
if __name__ == "__main__":
    # this loop allows me to implement logic that lets a user quit the program by clicking the red x in the top right
    while True:
        # userdata is either a string refrencing the next interface to display to the user
        # or a userObject that stores data about the logged on user.
        userdata = logOn()
        # if no function is selected the the user clicked the red x, so close the program.
        if userdata == "notSelected":
            break
        while True:
            # this loop allows the user to switch between three interfaces seamlessly,
            # the log on screen, create account screen and forgot password screen
            if userdata == "createAccount":
                createAccount()
            elif userdata == "forgotPassword":
                forgotPassword()
            else:
                break
            userdata = logOn()
        if userdata == "notSelected":
            break
        # this selection statement checks to see whether the first time set up window needs to be ran
        if userdata.getEmail() == None:
            function, userdata = setUp(userdata)
            if function == "notSelected":
                break
        # The following check is made so that a user will be asked for techer information only if that data is mising from the user's record
        teacherRecords = databaseAccess("SELECT * FROM tblTeachers")
        if teacherRecords[userdata.getTeacherId()][2] == None:
            userdata = newTeacher(userdata)
            if userdata == "notSelected":
                break
        # this loop contains the program's main loop and ensures that after a user finishes
        # using part of the program they are brought back to the main menu
        while True:
            function, functionData = mainMenu(userdata)
            if function == "notSelected":
                break
            elif function == "logOut":
                break
            elif function == "changeUsername":
                userdata = changeUsername(userdata)
            elif function == "changePassword":
                changePassword(userdata)
            elif function == "updateEmail":
                userdata = updateEmail(userdata)
            elif function == "updateTeacherDetails":
                # teacher details is a sub section of the main menu where a person can change their teacher and
                # their teachers email
                while True:
                    selectedFunction, teacherRecord = teacherSettings(userdata)
                    if selectedFunction == "notSelected":
                        break
                    elif selectedFunction == "email":
                        userdata = changeTeacherEmail(userdata, teacherRecord)
                    elif selectedFunction == "newTeacher":
                        userdata = changeTeacher(userdata, teacherRecord)
            elif function == "gameSettings":
                print("game settings function selected")
            elif function == "gameMode":
                game("game", functionData[0], functionData[1], userdata.getUsername())
            elif function == "revisionMode":
                game(
                    "revision", functionData[0], functionData[1], userdata.getUsername()
                )
        if function == "notSelected":
            break
