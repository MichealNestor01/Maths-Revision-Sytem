# This file contains all of the classes and functions that the program needs when it runs
# These are the imports necessary for modules in this file
# PyQt5 and sys work together to create user interfaces
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QCursor
from random import randint
from os import path
import sys
import smtplib

# sqlite3 allows me to access the sqlite database that this program relies on
import sqlite3

# The user class creates user objects that are linked to a record in the users table
# in the main database. These objects are passed between interfaces to identify the user.
class User:
    def __init__(self, userId="", username="", email="", teacherId=""):
        self._id = userId
        self._username = username
        self._email = email
        self._teacherId = teacherId

    def updateAll(self, userId, username, email, teacherId):
        self._id = userId
        self._username = username
        self._email = email
        self._teacherId = teacherId

    def updateId(self, userId):
        self._id = userId

    def updateUsername(self, username):
        self._username = username

    def updateEmail(self, email):
        self._email = email

    def updateTeacherId(self, teacherId):
        self._teacherId = teacherId

    def getUsername(self):
        return self._username

    def getId(self):
        return self._id

    def getEmail(self):
        return self._email

    def getTeacherId(self):
        return self._teacherId


# Below are the classes that create the user interfaces of my program, they were designed
# in qt designer before being ported to python, the setupUi methods are very similar between
# classes as they are just building all of the interface elements, I will therefore only
# comment on the first interface's setupUi retranslateUi methods, after that I will comment
# exclusively at points of interest in these functions

# This class creates the create account window:
class Ui_createAccountWindow(object):
    def setupUi(self, createAccountWindow):
        # set up the window that will contain all of the window elements
        createAccountWindow.setObjectName("createAccountWindow")
        createAccountWindow.resize(731, 308)
        # make sure that the user can not resize the window
        createAccountWindow.setMaximumSize(QtCore.QSize(731, 308))
        # Add an icon to the winodw
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        createAccountWindow.setWindowIcon(icon)
        # create a central element (called a widget in qt) that contains the rest of the qt widgets
        self.centralwidget = QtWidgets.QWidget(createAccountWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        # set up the font used by the window
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        # style sheets are similar to css and are used to colour and add design to qt widgets
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        # add a title label is just a string at the top of the window
        # labels are just string containers that you can place on the screen
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        # set geometry places the widget using coordinates measured from 0, 0 being the top left of the interface,
        # and then it takes a width value and a height value for he widget
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 711, 61))
        # point size is the font size and is variable between widgets
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        # usernameInput is a text input widget
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(180, 80, 531, 51))
        font.setPointSize(22)
        self.usernameInput.setFont(font)
        self.usernameInput.setObjectName("usernameInput")
        # username label is a lable for the text input
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 80, 161, 51))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.usernameLabel.setObjectName("usernameLabel")
        # password label for the password input
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 160, 161, 51))
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.passwordLabel.setObjectName("passwordLabel")
        # password input is a text input widget
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(180, 160, 531, 51))
        self.passwordInput.setFont(font)
        self.passwordInput.setObjectName("passwordInput")
        # submit button is a sibple qt button that can be linked to a function call, this button is used to submit the entered values
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 240, 361, 51))
        self.submitButton.setFont(font)
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        # set cursor makes it so that a pointing hand apears when hovering over the button
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # log on button is used to close this window, which causes the log on window to open
        self.logOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOnButton.setGeometry(QtCore.QRect(550, 240, 161, 51))
        font.setPointSize(15)
        self.logOnButton.setFont(font)
        self.logOnButton.setObjectName("logOnButton")
        self.logOnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(37)
        # background label has no text as is used just to colour the background
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.usernameInput.raise_()
        self.usernameLabel.raise_()
        self.passwordLabel.raise_()
        self.passwordInput.raise_()
        self.submitButton.raise_()
        self.logOnButton.raise_()
        createAccountWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(createAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(createAccountWindow)
        # connect the submit button to the self.createAccountMethod() function
        self.submitButton.clicked.connect(self.createAccountMethod)
        # make it so that the enter key will trigger the submit button
        self.submitButton.setShortcut("Return")
        # connect the log on button to the self.logOnMethod() function
        self.logOnButton.clicked.connect(self.logOnMethod)

    def retranslateUi(self, createAccountWindow):
        # retranslate ui's function is to add text to the interface widgits
        _translate = QtCore.QCoreApplication.translate
        createAccountWindow.setWindowTitle(
            _translate("createAccountWindow", "Mathematics Revision System")
        )
        self.titleLabel.setText(
            _translate(
                "createAccountWindow", "Please chose a username and unique password"
            )
        )
        self.usernameLabel.setText(_translate("createAccountWindow", "Username: "))
        self.passwordLabel.setText(_translate("createAccountWindow", "Password:"))
        self.submitButton.setText(_translate("createAccountWindow", "Create Account"))
        self.logOnButton.setText(_translate("createAccountWindow", "Log On"))

    # create account method is a function to take the user inputs and create an account for the user
    def createAccountMethod(self):
        # username and password are taken from the text entry widgets
        username = self.usernameInput.text().lower()
        password = self.passwordInput.text()
        # database access is a function that is written further down this file and speeds up accessing the daabase
        userData = databaseAccess("SELECT * FROM tblUsers")
        # valid is set to false if the username is not unique
        valid = True
        for records in userData:
            if records[1] == username:
                valid = False
        # if the username is already in use then an error message is displayed
        if valid == False:
            # message box is a function similar to datbase access as I use it to make it easy for me to make message pop,
            # up windows, it's code is further down in this file
            messageBox(
                "Duplicate Error", "Sorry that username is already in use.", "critical"
            )
        else:
            # if the username is not a duplicate then a new user is added to the database
            userId = len(userData)
            databaseAccess(
                ("INSERT INTO tblUsers (userID, userName, password) VALUES(?, ?, ?)"),
                (userId, username, password),
            )
            messageBox(
                "Success",
                "A new account has been created! You will now be taken to the log on screen",
                "information",
            )
            QtWidgets.qApp.quit()

    # due to the main loop, simply closing this window with the command QtWidgets.qApp.quit() will return the user to the log on screen
    def logOnMethod(self):
        QtWidgets.qApp.quit()


# This class creates the log on window:
class Ui_logOnWindow(object):
    def __init__(self):
        # userObject is used to store the current user's data and is passed between interfaces
        self.userObject = User()
        # selected function is used by the main loop to determine the interface that should be shown to the user
        # once this has closed
        self.selectedFunction = "notSelected"

    def setupUi(self, logOnWindow):
        logOnWindow.setObjectName("logOnWindow")
        logOnWindow.resize(731, 308)
        logOnWindow.setMaximumSize(QtCore.QSize(731, 308))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        logOnWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(logOnWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 711, 61))
        font = QtGui.QFont()
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("font-size: 48px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(180, 80, 531, 51))
        font.setPointSize(22)
        self.usernameInput.setFont(font)
        self.usernameInput.setMaxLength(20)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 80, 161, 51))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAutoFillBackground(False)
        self.usernameLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 160, 161, 51))
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(180, 160, 531, 51))
        self.passwordInput.setFont(font)
        self.passwordInput.setMaxLength(20)
        self.passwordInput.setObjectName("passwordInput")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(210, 240, 301, 51))
        self.submitButton.setFont(font)
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createAccount = QtWidgets.QPushButton(self.centralwidget)
        self.createAccount.setGeometry(QtCore.QRect(520, 240, 191, 51))
        font.setPointSize(16)
        self.createAccount.setFont(font)
        self.createAccount.setStyleSheet("")
        self.createAccount.setObjectName("createAccount")
        self.createAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(37)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setText("")
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.forgotPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(10, 240, 191, 51))
        font.setPointSize(16)
        self.forgotPasswordButton.setFont(font)
        self.forgotPasswordButton.setObjectName("forgotPasswordButton")
        self.forgotPasswordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.usernameInput.raise_()
        self.usernameLabel.raise_()
        self.passwordLabel.raise_()
        self.passwordInput.raise_()
        self.submitButton.raise_()
        self.createAccount.raise_()
        self.forgotPasswordButton.raise_()
        logOnWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(logOnWindow)
        QtCore.QMetaObject.connectSlotsByName(logOnWindow)
        # connect all of the windows buttons to function methods
        self.submitButton.clicked.connect(self.submitData)
        self.createAccount.clicked.connect(self.createAccountMethod)
        self.forgotPasswordButton.clicked.connect(self.forgotPasswordMethod)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, logOnWindow):
        _translate = QtCore.QCoreApplication.translate
        logOnWindow.setWindowTitle(
            _translate("logOnWindow", "Mathematics Revision System")
        )
        self.titleLabel.setText(_translate("logOnWindow", "Welcome"))
        self.usernameLabel.setText(_translate("logOnWindow", "Username: "))
        self.passwordLabel.setText(_translate("logOnWindow", "Password: "))
        self.submitButton.setText(_translate("logOnWindow", "Log On"))
        self.createAccount.setText(_translate("logOnWindow", "Create Account"))
        self.forgotPasswordButton.setText(_translate("logOnWindow", "Forgot Password"))

    # return data is used by the main loop to get decide which window should be open next
    def returnData(self):
        if self.selectedFunction == "logOn":
            return self.userObject
        else:
            return self.selectedFunction

    # create account method changes the selected function to 'createAccount' and closes the window
    def createAccountMethod(self):
        self.selectedFunction = "createAccount"
        QtWidgets.qApp.quit()

    # forgot password method changes the selected function to 'forgotPassword' and closes the window
    def forgotPasswordMethod(self):
        self.selectedFunction = "forgotPassword"
        QtWidgets.qApp.quit()

    # submit data is the function that tries to log users in
    def submitData(self):
        # these are variables that will need to be asigned for the user object to be created
        userId = ""
        userEmail = ""
        teacherId = ""
        # the data the user has inputed is collected
        username = self.usernameInput.text().lower()
        password = self.passwordInput.text()
        # data to compare the user's input against is fetched from the database
        storedUserData = databaseAccess("SELECT * FROM tblUsers")
        # the users inputs are checked against the users in the databse
        valid = False
        for records in storedUserData:
            if records[1] == username:
                if records[2] == password:
                    userId = records[0]
                    userEmail = records[3]
                    teacherId = records[4]
                    # if there is a correct match valid is set to true
                    valid = True
        # if there is no match in the database an error message is show to the user
        if valid == False:
            messageBox(
                "Input Error",
                "Sorry either the username or passsword you entered was invalid",
                "critical",
            )
        else:
            # if there is a match selected function is updated and the userobject is created, then the window is closed
            self.selectedFunction = "logOn"
            self.userObject.updateAll(userId, username, userEmail, teacherId)
            QtWidgets.qApp.quit()


# this class creates forgot password window
class Ui_forgotPasswordWindow(object):
    def __init__(self):
        # code is what is used to verify the user's email address
        self._code = ""
        self.userName = ""
        self.email = "NoEmailInputted"

    def setupUi(self, forgotPasswordWindow):
        forgotPasswordWindow.setObjectName("forgotPasswordWindow")
        forgotPasswordWindow.resize(731, 364)
        forgotPasswordWindow.setMaximumSize(QtCore.QSize(731, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        forgotPasswordWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(forgotPasswordWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 600))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(10, 10, 711, 61))
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("font-size: 40px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(230, 80, 481, 51))
        font.setPointSize(22)
        self.emailInput.setFont(font)
        self.emailInput.setObjectName("emailInput")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(20, 80, 161, 51))
        font.setPointSize(20)
        self.emailLabel.setFont(font)
        self.emailLabel.setAutoFillBackground(False)
        self.emailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.emailLabel.setObjectName("emailLabel")
        self.codeLabel = QtWidgets.QLabel(self.centralwidget)
        self.codeLabel.setGeometry(QtCore.QRect(20, 160, 161, 51))
        self.codeLabel.setFont(font)
        self.codeLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.codeLabel.setObjectName("codeLabel")
        self.codeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.codeInput.setGeometry(QtCore.QRect(230, 160, 481, 51))
        font.setPointSize(22)
        self.codeInput.setFont(font)
        self.codeInput.setObjectName("codeInput")
        self.resetPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetPasswordButton.setGeometry(QtCore.QRect(210, 300, 301, 51))
        font.setPointSize(21)
        self.resetPasswordButton.setFont(font)
        self.resetPasswordButton.setAutoDefault(False)
        self.resetPasswordButton.setDefault(False)
        self.resetPasswordButton.setFlat(False)
        self.resetPasswordButton.setObjectName("resetPasswordButton")
        self.resetPasswordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendCodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendCodeButton.setGeometry(QtCore.QRect(520, 300, 191, 51))
        font.setPointSize(16)
        self.sendCodeButton.setFont(font)
        self.sendCodeButton.setObjectName("sendCodeButton")
        self.sendCodeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 501))
        font.setPointSize(37)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.logOnButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOnButton.setGeometry(QtCore.QRect(10, 300, 191, 51))
        font.setPointSize(16)
        self.logOnButton.setFont(font)
        self.logOnButton.setObjectName("logOnButton")
        self.logOnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 230, 201, 51))
        font.setPointSize(20)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(230, 230, 481, 51))
        font.setPointSize(22)
        self.passwordInput.setFont(font)
        self.passwordInput.setObjectName("passwordInput")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.emailInput.raise_()
        self.emailLabel.raise_()
        self.codeLabel.raise_()
        self.codeInput.raise_()
        self.resetPasswordButton.raise_()
        self.sendCodeButton.raise_()
        self.logOnButton.raise_()
        self.passwordLabel.raise_()
        self.passwordInput.raise_()
        forgotPasswordWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(forgotPasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(forgotPasswordWindow)
        self.logOnButton.clicked.connect(self.logOnMethod)
        self.sendCodeButton.clicked.connect(self.sendCode)
        self.resetPasswordButton.clicked.connect(self.resetPasswordMethod)
        self.resetPasswordButton.setShortcut("Return")

    def retranslateUi(self, forgotPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        forgotPasswordWindow.setWindowTitle(
            _translate("forgotPasswordWindow", "Mathematics Revision System")
        )
        self.titleLabel.setText(
            _translate("forgotPasswordWindow", "Forgot Passord Menu")
        )
        self.emailLabel.setText(_translate("forgotPasswordWindow", "Your Email:"))
        self.codeLabel.setText(_translate("forgotPasswordWindow", "Your Code:"))
        self.resetPasswordButton.setText(
            _translate("forgotPasswordWindow", "Reset Password")
        )
        self.sendCodeButton.setText(_translate("forgotPasswordWindow", "Send Code"))
        self.logOnButton.setText(_translate("forgotPasswordWindow", "Log On"))
        self.passwordLabel.setText(_translate("forgotPasswordWindow", "New Password:"))
        messageBox(
            "Forgot password system",
            "Enter your email then click the 'send code' button to have a recovery code sent to your emial address, then put this code into the code box and choose a new password.",
            "information",
        )

    # if log on is pressed just close the current window
    def logOnMethod(self):
        QtWidgets.qApp.quit()

    # send code sends a randomised code the the given email address
    def sendCode(self):
        # get the given email and check it against stored email addresses
        inputedEmail = self.emailInput.text().lower()
        storedUserData = databaseAccess("SELECT * FROM tblUsers")
        valid = False
        for records in storedUserData:
            if records[3] == inputedEmail:
                valid = True
                self.userName = records[1]
        # if there is no matching records show an error message
        if valid == False:
            messageBox(
                "Input Error",
                "Sorry none of the stored accounts have that email",
                "critical",
            )
        else:
            # else show a sucess message box, generate a random code, and send an email to the given account with the reset code
            messageBox(
                "Email Sent",
                "An email with the code has been sent to the email provided. Make sure that you check your spam/junk folder.",
                "information",
            )
            self.email = inputedEmail
            self._code = randint(100000, 999999)
            # send mail is a function I made to make sending emails easier, it is defined after the interface classes
            sendMail("Password Reset Code", f"Your code is: {self._code}", inputedEmail)

    # reset password allows the user, with the correct code, to reset their password
    def resetPasswordMethod(self):
        code = self.codeInput.text()
        # if the code entered does not equal the code sent, then show an error message
        if str(self._code) != code:
            messageBox(
                "Code Error", "Sorry this code is incorrect", "critical",
            )
        else:
            # it is double checked that the user's email is correct and show apropriate message boxes
            if self.emailInput.text() != self.email:
                messageBox(
                    "Input Error",
                    "Please input the email address that is linked to your account",
                    "critical",
                )
            else:
                databaseAccess(
                    f"UPDATE tblUsers SET password = '{self.passwordInput.text()}' WHERE userName = '{self.userName}' "
                )
                messageBox(
                    "Password Changed",
                    "Your password has been successfully changed, you will now be taken to the log on screen",
                    "information",
                )
                QtWidgets.qApp.quit()


# This class creates the first time set up window
class Ui_firstTimeSetUp(object):
    def __init__(self, userdata):
        # the userObject is parsed from the log on window
        self.userObject = userdata
        self.selectedFunction = "notSelected"

    def setupUi(self, firstTimeSetUp):
        firstTimeSetUp.setObjectName("firstTimeSetUp")
        firstTimeSetUp.resize(731, 273)
        firstTimeSetUp.setMinimumSize(QtCore.QSize(731, 273))
        firstTimeSetUp.setMaximumSize(QtCore.QSize(731, 273))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        firstTimeSetUp.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(firstTimeSetUp)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 200))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 731, 71))
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("font-size: 32px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.userEmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.userEmailInput.setGeometry(QtCore.QRect(190, 80, 521, 41))
        font.setPointSize(18)
        self.userEmailInput.setFont(font)
        self.userEmailInput.setObjectName("userEmailInput")
        self.userEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.userEmailLabel.setGeometry(QtCore.QRect(20, 80, 161, 51))
        font.setPointSize(16)
        self.userEmailLabel.setFont(font)
        self.userEmailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.userEmailLabel.setObjectName("userEmailLabel")
        self.teacherEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.teacherEmailLabel.setGeometry(QtCore.QRect(20, 130, 161, 51))
        self.teacherEmailLabel.setFont(font)
        self.teacherEmailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.teacherEmailLabel.setObjectName("teacherEmailLabel")
        self.teacherEmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherEmailInput.setGeometry(QtCore.QRect(190, 130, 521, 41))
        font.setPointSize(18)
        self.teacherEmailInput.setFont(font)
        self.teacherEmailInput.setObjectName("teacherEmailInput")
        self.continueButton = QtWidgets.QPushButton(self.centralwidget)
        self.continueButton.setGeometry(QtCore.QRect(210, 220, 311, 41))
        font.setPointSize(19)
        self.continueButton.setFont(font)
        self.continueButton.setAutoDefault(False)
        self.continueButton.setDefault(False)
        self.continueButton.setFlat(False)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logOut = QtWidgets.QPushButton(self.centralwidget)
        self.logOut.setGeometry(QtCore.QRect(580, 220, 131, 41))
        font.setPointSize(15)
        self.logOut.setFont(font)
        self.logOut.setObjectName("logOut")
        self.logOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(37)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.loggedInLabel = QtWidgets.QLabel(self.centralwidget)
        self.loggedInLabel.setGeometry(QtCore.QRect(20, 160, 691, 71))
        font.setPointSize(15)
        self.loggedInLabel.setFont(font)
        self.loggedInLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.loggedInLabel.setObjectName("loggedInLabel")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.userEmailInput.raise_()
        self.userEmailLabel.raise_()
        self.teacherEmailLabel.raise_()
        self.teacherEmailInput.raise_()
        self.continueButton.raise_()
        self.logOut.raise_()
        self.loggedInLabel.raise_()
        firstTimeSetUp.setCentralWidget(self.centralwidget)
        self.retranslateUi(firstTimeSetUp)
        QtCore.QMetaObject.connectSlotsByName(firstTimeSetUp)
        self.logOut.clicked.connect(self.logOutMethod)
        self.continueButton.clicked.connect(self.updateData)
        self.continueButton.setShortcut("Return")

    def retranslateUi(self, firstTimeSetUp):
        _translate = QtCore.QCoreApplication.translate
        firstTimeSetUp.setWindowTitle(
            _translate("firstTimeSetUp", "Mathematics Revision System")
        )
        self.titleLabel.setText(_translate("firstTimeSetUp", "First time set up"))
        self.userEmailLabel.setText(_translate("firstTimeSetUp", "Your Email:"))
        self.teacherEmailLabel.setText(_translate("firstTimeSetUp", "Teacher Email:"))
        self.continueButton.setText(_translate("firstTimeSetUp", "Continue"))
        self.logOut.setText(_translate("firstTimeSetUp", "Log Out"))
        self.loggedInLabel.setText(
            _translate(
                "firstTimeSetUp", f"Logged in as {self.userObject.getUsername()}"
            )
        )

    def updateData(self):
        # get the inputed email and teacher email, then validate that they contain the '@' symbol
        userEmail = self.userEmailInput.text().lower()
        teacherEmail = self.teacherEmailInput.text().lower()
        validUserEmail = False
        validTeacherEmail = False
        if "@" in userEmail:
            validUserEmail = True
        if "@" in teacherEmail:
            validTeacherEmail = True
        # if its invalid  show an error message
        if validUserEmail == False or validTeacherEmail == False:
            messageBox(
                "Input Error", "You have not entered vaid email adresses!", "critical"
            )
        else:
            # if the teacher email is recognised then link the student record to the corrospoding teacher
            # else set selected function to new teaher so that the new teacher window will be opened next
            self.userObject.updateEmail(userEmail)
            teacherData = databaseAccess("SELECT * FROM tblTeachers")
            newTeacher = True
            for records in teacherData:
                if records[1] == teacherEmail:
                    teacherID = records[0]
                    newTeacher = False
                    self.userObject.updateTeacherId(teacherID)
                    self.selectedFunction = "mainMenu"
            if newTeacher == True:
                teacherID = len(teacherData)
                self.userObject.updateTeacherId(teacherID)
                self.selectedFunction = "newTeacher"
                databaseAccess(
                    ("INSERT INTO tblTeachers (teacherID, teacherEmail) VALUES(?, ?)"),
                    (teacherID, teacherEmail),
                )
            databaseAccess(
                f"UPDATE tblUsers SET email = '{userEmail}', teacherID = {teacherID} WHERE userName = '{self.userObject.getUsername()}'"
            )
            QtWidgets.qApp.quit()

    # if log out is clicked close the window
    def logOutMethod(self):
        QtWidgets.qApp.quit()


# this class creates new teacher records in the database
class Ui_newTeacherSetup(object):
    def __init__(self, userObject):
        # get the teacher record that the user is linked to
        teacherRecords = databaseAccess("SELECT * FROM tblTeachers")
        self.teacherRecord = teacherRecords[userObject.getTeacherId()]
        self.selectedFunction = "notSelected"

    def setupUi(self, newTeacherSetup):
        newTeacherSetup.setObjectName("newTeacherSetup")
        newTeacherSetup.resize(731, 239)
        newTeacherSetup.setMinimumSize(QtCore.QSize(731, 239))
        newTeacherSetup.setMaximumSize(QtCore.QSize(731, 239))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        newTeacherSetup.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(newTeacherSetup)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 200))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: rgba(0,212,255,1);\n"
            "    color: black;\n"
            "    background-color: rgba(220, 240, 255);\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 731, 71))
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("font-size: 32px;")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.topTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.topTextLabel.setGeometry(QtCore.QRect(20, 60, 691, 51))
        font.setPointSize(12)
        self.topTextLabel.setFont(font)
        self.topTextLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topTextLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.teacherNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.teacherNameLabel.setGeometry(QtCore.QRect(20, 130, 181, 41))
        font.setPointSize(17)
        self.teacherNameLabel.setFont(font)
        self.teacherNameLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.teacherNameLabel.setObjectName("teacherNameLabel")
        self.teacherNameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherNameInput.setGeometry(QtCore.QRect(340, 130, 371, 41))
        self.teacherNameInput.setFont(font)
        self.teacherNameInput.setObjectName("teacherNameInput")
        self.continueButton = QtWidgets.QPushButton(self.centralwidget)
        self.continueButton.setGeometry(QtCore.QRect(200, 190, 311, 41))
        font.setPointSize(19)
        self.continueButton.setFont(font)
        self.continueButton.setAutoDefault(False)
        self.continueButton.setDefault(False)
        self.continueButton.setFlat(False)
        self.continueButton.setObjectName("continueButton")
        self.continueButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logOut = QtWidgets.QPushButton(self.centralwidget)
        self.logOut.setGeometry(QtCore.QRect(580, 190, 131, 41))
        font.setPointSize(15)
        self.logOut.setFont(font)
        self.logOut.setObjectName("logOut")
        self.logOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.bottomTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.bottomTextLabel.setGeometry(QtCore.QRect(20, 80, 691, 51))
        font.setPointSize(12)
        self.bottomTextLabel.setFont(font)
        self.bottomTextLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.bottomTextLabel.setObjectName("bottomTextLabel")
        self.teacherPrefixInput = QtWidgets.QComboBox(self.centralwidget)
        self.teacherPrefixInput.setGeometry(QtCore.QRect(200, 130, 131, 41))
        font.setPointSize(17)
        self.teacherPrefixInput.setFont(font)
        self.teacherPrefixInput.setObjectName("teacherPrefixInput")
        self.teacherPrefixInput.addItem("")
        self.teacherPrefixInput.addItem("")
        self.teacherPrefixInput.addItem("")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.topTextLabel.raise_()
        self.teacherNameLabel.raise_()
        self.teacherNameInput.raise_()
        self.continueButton.raise_()
        self.logOut.raise_()
        self.bottomTextLabel.raise_()
        self.teacherPrefixInput.raise_()
        newTeacherSetup.setCentralWidget(self.centralwidget)
        self.retranslateUi(newTeacherSetup)
        QtCore.QMetaObject.connectSlotsByName(newTeacherSetup)
        self.logOut.clicked.connect(self.logOutMethod)
        self.continueButton.clicked.connect(self.updateTeacherName)
        self.continueButton.setShortcut("Return")

    def retranslateUi(self, newTeacherSetup):
        _translate = QtCore.QCoreApplication.translate
        newTeacherSetup.setWindowTitle(
            _translate("newTeacherSetup", "Mathematics Revision System")
        )
        self.titleLabel.setText(_translate("newTeacherSetup", "New teacher window"))
        self.topTextLabel.setText(
            _translate(
                "newTeacherSetup",
                "Sorry we do not recognise your teacher's email address.",
            )
        )
        self.teacherNameLabel.setText(_translate("newTeacherSetup", "Teacher Name:"))
        self.teacherNameInput.setPlaceholderText(
            _translate("newTeacherSetup", "Surname")
        )
        self.continueButton.setText(_translate("newTeacherSetup", "Continue"))
        self.logOut.setText(_translate("newTeacherSetup", "Log Out"))
        self.bottomTextLabel.setText(
            _translate(
                "newTeacherSetup",
                f"What is the name of your teacher with the email '{self.teacherRecord[1]}'?",
            )
        )
        self.teacherPrefixInput.setItemText(0, _translate("newTeacherSetup", "Mr"))
        self.teacherPrefixInput.setItemText(1, _translate("newTeacherSetup", "Mrs"))
        self.teacherPrefixInput.setItemText(2, _translate("newTeacherSetup", "Miss"))

    def updateTeacherName(self):
        # get the name and prefix and check that the name field has been filled
        teacherName = self.teacherNameInput.text()
        teacherPrefix = self.teacherPrefixInput.currentText()
        while True:
            if teacherName == "":
                messageBox(
                    "Input Error",
                    "Please input the surname of your teacher in the entry box",    
                    "critical",
                )
                break
            # if the teacher name has been inputed then join the prefix and name then update the datbase and use
            # selectedFunction to point main loop to run the main menu
            fullName = f"{teacherPrefix} {teacherName}"
            databaseAccess(
                f"UPDATE tblTeachers SET teacherName = '{fullName}' WHERE teacherID = '{self.teacherRecord[0]}' "
            )
            messageBox(
                "Success", f"{fullName} has been successfully added to our records"
            )
            self.selectedFunction = "mainMenu"
            QtWidgets.qApp.quit()
            break

    # if the log out button is pressed close the window
    def logOutMethod(self):
        QtWidgets.qApp.quit()


# main menu user interface class:
class Ui_mainMenuWindow(object):
    def __init__(self, userObject):
        self.userObject = userObject
        self.selectedFunction = "notSelected"
        # function data is an array which stores data that selected functions will need from the main menu
        self.functionData = []
        # teacher data is used in parts of the window to fill in label contents
        self.teacherData = databaseAccess(
            f"SELECT * FROM tblTeachers WHERE teacherID = {userObject.getTeacherId()}"
        )[0]
        # Paths for the images of the player styles:
        self.imagePaths = [
            "./images/style1.png",
            "./images/style2.png",
            "./images/style3.png",
            "./images/style4.png",
            "./images/style5.png",
        ]

    # this setup function is significantly larger than previous interfaces' this is because it uses a QTabWidget to essentially
    # merge 4 windows into 4 tabs within 1 window, the three tabs are called the settings tab, the game tab, the revision tab
    # and the analytics tab. in this setup function widgets are added to tabs rather than being added to a central widget as has
    # bee commonplace in the previouse interfaces' setup functions.
    def setupUi(self, mainMenuWindow):
        mainMenuWindow.setObjectName("mainMenuWindow")
        mainMenuWindow.setMinimumSize(QtCore.QSize(800, 405))
        mainMenuWindow.setMaximumSize(QtCore.QSize(800, 405))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        mainMenuWindow.setWindowIcon(icon)
        # The stylesheet is significantly larger but it fulfills the same purpose, to make the widgets look prettier
        mainMenuWindow.setStyleSheet(
            "QComboBox {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: rgba(0,212,255,1);\n"
            "    color: black;\n"
            "    background-color: rgba(220, 240, 255, 1);\n"
            "}\n"
            "QTabWidget::pane { \n"
            "    border-top: 2px solid grey;\n"
            "    background: #ff8e5e;\n"
            "}\n"
            "QPushButton {\n"
            "    color: black;\n"
            "    background: #57e3ff;\n"
            "}\n"
            "\n"
            "QTabBar::tab {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0       rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5     rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));\n"
            "    border: 2px solid grey;\n"
            "    border-bottom-color: grey;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    padding: 0px;\n"
            "    margin-bottom: 2px;\n"
            "    height: 75px;\n"
            "    padding-bottom: 8px\n"
            "}\n"
            "\n"
            "QTabBar::tab:hover {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(216,248,255,1), stop:0.25 rgba(149,237,255,1), stop:0.5 rgba(83,226,255,1), stop:0.75 rgba(149,237,255,1), stop:1 rgba(216,248,255,1));\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245,250,251,1), stop:0.25 rgba(211,244,251,1), stop:0.5 rgba(188,241,251,1), stop:0.75 rgba(211,244,251,1), stop:1 rgba(245,250,251,1));\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "        border-style: solid;\n"
            "        border-width: 2px;\n"
            "        border-color: black;\n"
            "        background: #ff8e5e;\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "        border-style: solid;\n"
            "        border-width: 2px;\n"
            "        border-color: black;\n"
            "        background: #57e3ff;\n"
            "}\n"
            "QRadioButton::indicator:unchecked {\n"
            "        border-style: solid;\n"
            "        border-width: 2px;\n"
            "        border-color: black;\n"
            "        background: #ff8e5e;\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "        border-style: solid;\n"
            "        border-width: 2px;\n"
            "        border-color: black;\n"
            "        background: #57e3ff;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(mainMenuWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 405))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 405))
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 900, 360))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 360))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 360))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(19)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(65, 90))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.settingsTab.setObjectName("settingsTab")
        self.settingsTitle = QtWidgets.QLabel(self.settingsTab)
        self.settingsTitle.setGeometry(QtCore.QRect(10, 0, 131, 41))
        font.setPointSize(21)
        font.setUnderline(True)
        self.settingsTitle.setFont(font)
        self.settingsTitle.setObjectName("settingsTitle")
        self.loggedInLabel = QtWidgets.QLabel(self.settingsTab)
        self.loggedInLabel.setGeometry(QtCore.QRect(10, 40, 331, 41))
        font.setPointSize(14)
        font.setUnderline(False)
        self.loggedInLabel.setFont(font)
        self.loggedInLabel.setObjectName("loggedInLabel")
        self.changePassword = QtWidgets.QPushButton(self.settingsTab)
        self.changePassword.setGeometry(QtCore.QRect(360, 90, 331, 61))
        self.changePassword.setFont(font)
        self.changePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changePassword.setObjectName("changePassword")
        self.changeUsername = QtWidgets.QPushButton(self.settingsTab)
        self.changeUsername.setGeometry(QtCore.QRect(10, 90, 331, 61))
        self.changeUsername.setFont(font)
        self.changeUsername.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeUsername.setObjectName("changeUsername")
        self.changeTeacherEmail = QtWidgets.QPushButton(self.settingsTab)
        self.changeTeacherEmail.setGeometry(QtCore.QRect(360, 160, 331, 61))
        self.changeTeacherEmail.setFont(font)
        self.changeTeacherEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeTeacherEmail.setObjectName("changeTeacherEmail")
        self.logOutButton = QtWidgets.QPushButton(self.settingsTab)
        self.logOutButton.setGeometry(QtCore.QRect(360, 300, 331, 41))
        self.logOutButton.setFont(font)
        self.logOutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logOutButton.setObjectName("logOutButton")
        self.closeProgramButton = QtWidgets.QPushButton(self.settingsTab)
        self.closeProgramButton.setGeometry(QtCore.QRect(10, 300, 331, 41))
        self.closeProgramButton.setFont(font)
        self.closeProgramButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeProgramButton.setObjectName("closeProgramButton")
        self.changeUserEmail = QtWidgets.QPushButton(self.settingsTab)
        self.changeUserEmail.setGeometry(QtCore.QRect(10, 160, 331, 61))
        self.changeUserEmail.setFont(font)
        self.changeUserEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeUserEmail.setObjectName("changeUserEmail")
        self.changeGameSettings = QtWidgets.QPushButton(self.settingsTab)
        self.changeGameSettings.setGeometry(QtCore.QRect(10, 230, 681, 61))
        self.changeGameSettings.setFont(font)
        self.changeGameSettings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeGameSettings.setObjectName("changeGameSettings")
        self.teacherLabel = QtWidgets.QLabel(self.settingsTab)
        self.teacherLabel.setGeometry(QtCore.QRect(360, 40, 331, 41))
        self.teacherLabel.setFont(font)
        self.teacherLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.teacherLabel.setAutoFillBackground(False)
        self.teacherLabel.setTextFormat(QtCore.Qt.AutoText)
        self.teacherLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.teacherLabel.setObjectName("teacherLabel")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("./images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.tabWidget.addTab(self.settingsTab, icon1, "")
        self.gameTab = QtWidgets.QWidget()
        self.gameTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.gameTab.setObjectName("gameTab")
        self.gameModeTitle = QtWidgets.QLabel(self.gameTab)
        self.gameModeTitle.setGeometry(QtCore.QRect(10, 0, 201, 41))
        font.setPointSize(21)
        font.setUnderline(True)
        self.gameModeTitle.setFont(font)
        self.gameModeTitle.setObjectName("gameModeTitle")
        self.playGameButton = QtWidgets.QPushButton(self.gameTab)
        self.playGameButton.setGeometry(QtCore.QRect(10, 280, 681, 61))
        font.setPointSize(14)
        font.setUnderline(False)
        self.playGameButton.setFont(font)
        self.playGameButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playGameButton.setObjectName("playGameButton")
        self.selectCharacterLabel = QtWidgets.QLabel(self.gameTab)
        self.selectCharacterLabel.setGeometry(QtCore.QRect(10, 190, 331, 41))
        self.selectCharacterLabel.setFont(font)
        self.selectCharacterLabel.setObjectName("selectCharacterLabel")
        self.gameStyleSelect = QtWidgets.QComboBox(self.gameTab)
        self.gameStyleSelect.setGeometry(QtCore.QRect(10, 230, 251, 41))
        self.gameStyleSelect.setFont(font)
        self.gameStyleSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameStyleSelect.setAcceptDrops(False)
        self.gameStyleSelect.setEditable(False)
        self.gameStyleSelect.setObjectName("gameStyleSelect")
        for i in range(5):
            self.gameStyleSelect.addItem("")
        self.characterImage = QtWidgets.QLabel(self.gameTab)
        self.characterImage.setGeometry(QtCore.QRect(400, 40, 168, 216))
        self.characterImage.setPixmap(QtGui.QPixmap(self.imagePaths[0]))
        self.characterImage.setScaledContents(True)
        self.characterImage.setObjectName("characterImage")
        self.selectTTopicLabel = QtWidgets.QLabel(self.gameTab)
        self.selectTTopicLabel.setGeometry(QtCore.QRect(10, 50, 331, 41))
        self.selectTTopicLabel.setFont(font)
        self.selectTTopicLabel.setObjectName("selectTTopicLabel")
        self.gameTopicSelect = QtWidgets.QComboBox(self.gameTab)
        self.gameTopicSelect.setGeometry(QtCore.QRect(10, 90, 251, 41))
        self.gameTopicSelect.setFont(font)
        self.gameTopicSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gameTopicSelect.setAcceptDrops(False)
        self.gameTopicSelect.setEditable(False)
        self.gameTopicSelect.setObjectName("gameTopicSelect")
        for i in range(14):
            self.gameTopicSelect.addItem("")
        self.gameTopicSuggestionButton = QtWidgets.QPushButton(self.gameTab)
        self.gameTopicSuggestionButton.setGeometry(QtCore.QRect(10, 140, 251, 41))
        self.gameTopicSuggestionButton.setFont(font)
        self.gameTopicSuggestionButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.gameTopicSuggestionButton.setObjectName("gameTopicSuggestionButton")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("./images/gameLogoRotated.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget.addTab(self.gameTab, icon2, "")
        self.revisionTab = QtWidgets.QWidget()
        self.revisionTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.revisionTab.setObjectName("revisionTab")
        self.revisionModeTitle = QtWidgets.QLabel(self.revisionTab)
        self.revisionModeTitle.setGeometry(QtCore.QRect(10, 0, 261, 41))
        font.setPointSize(21)
        font.setUnderline(True)
        self.revisionModeTitle.setFont(font)
        self.revisionModeTitle.setObjectName("revisionModeTitle")
        self.playRevisionButton = QtWidgets.QPushButton(self.revisionTab)
        self.playRevisionButton.setGeometry(QtCore.QRect(10, 280, 681, 61))
        font.setPointSize(14)
        font.setUnderline(False)
        self.playRevisionButton.setFont(font)
        self.playRevisionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playRevisionButton.setObjectName("playRevisionButton")
        self.revisionStyleSelect = QtWidgets.QComboBox(self.revisionTab)
        self.revisionStyleSelect.setGeometry(QtCore.QRect(10, 230, 251, 41))
        self.revisionStyleSelect.setMaximumSize(QtCore.QSize(16777215, 41))
        self.revisionStyleSelect.setFont(font)
        self.revisionStyleSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.revisionStyleSelect.setAcceptDrops(False)
        self.revisionStyleSelect.setEditable(False)
        self.revisionStyleSelect.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow
        )
        self.revisionStyleSelect.setObjectName("revisionStyleSelect")
        for i in range(5):
            self.revisionStyleSelect.addItem("")
        self.selectCharacterLabelRevision = QtWidgets.QLabel(self.revisionTab)
        self.selectCharacterLabelRevision.setGeometry(QtCore.QRect(10, 190, 331, 41))
        self.selectCharacterLabelRevision.setFont(font)
        self.selectCharacterLabelRevision.setObjectName("selectCharacterLabelRevision")
        self.characterImageRevision = QtWidgets.QLabel(self.revisionTab)
        self.characterImageRevision.setGeometry(QtCore.QRect(400, 40, 168, 216))
        self.characterImageRevision.setPixmap(QtGui.QPixmap(self.imagePaths[0]))
        self.characterImageRevision.setScaledContents(True)
        self.characterImageRevision.setObjectName("characterImageRevision")
        self.selectTopicLabelRevision = QtWidgets.QLabel(self.revisionTab)
        self.selectTopicLabelRevision.setGeometry(QtCore.QRect(10, 50, 331, 41))
        self.selectTopicLabelRevision.setFont(font)
        self.selectTopicLabelRevision.setObjectName("selectTopicLabelRevision")
        self.revisionTopicSuggestionButton = QtWidgets.QPushButton(self.revisionTab)
        self.revisionTopicSuggestionButton.setGeometry(QtCore.QRect(10, 140, 251, 41))
        self.revisionTopicSuggestionButton.setFont(font)
        self.revisionTopicSuggestionButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.revisionTopicSuggestionButton.setObjectName(
            "revisionTopicSuggestionButton"
        )
        self.revisionTopicSelect = QtWidgets.QComboBox(self.revisionTab)
        self.revisionTopicSelect.setGeometry(QtCore.QRect(10, 90, 251, 41))
        self.revisionTopicSelect.setFont(font)
        self.revisionTopicSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.revisionTopicSelect.setAcceptDrops(False)
        self.revisionTopicSelect.setStyleSheet("")
        self.revisionTopicSelect.setEditable(False)
        self.revisionTopicSelect.setObjectName("revisionTopicSelect")
        for i in range(14):
            self.revisionTopicSelect.addItem("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("./images/reviseLogoRotated.PNG"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget.addTab(self.revisionTab, icon3, "")
        self.analytics = QtWidgets.QWidget()
        self.analytics.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.analytics.setObjectName("analytics")
        self.analyticsTitle = QtWidgets.QLabel(self.analytics)
        self.analyticsTitle.setGeometry(QtCore.QRect(10, 0, 201, 41))
        font.setPointSize(21)
        font.setUnderline(True)
        self.analyticsTitle.setFont(font)
        self.analyticsTitle.setObjectName("analyticsTitle")
        self.selectDataLabel = QtWidgets.QLabel(self.analytics)
        self.selectDataLabel.setGeometry(QtCore.QRect(360, 40, 400, 41))
        font.setPointSize(14)
        font.setUnderline(False)
        self.selectDataLabel.setFont(font)
        self.selectDataLabel.setObjectName("selectDataLabel")
        self.sendEmailButton = QtWidgets.QPushButton(self.analytics)
        self.sendEmailButton.setGeometry(QtCore.QRect(360, 280, 331, 51))
        self.sendEmailButton.setFont(font)
        self.sendEmailButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendEmailButton.setObjectName("sendEmailButton")
        self.checkTotalProgress = QtWidgets.QCheckBox(self.analytics)
        self.checkTotalProgress.setGeometry(QtCore.QRect(360, 90, 331, 31))
        self.checkTotalProgress.setFont(font)
        self.checkTotalProgress.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkTotalProgress.setObjectName("checkTotalProgress")
        self.checkProgressTopic = QtWidgets.QCheckBox(self.analytics)
        self.checkProgressTopic.setGeometry(QtCore.QRect(360, 130, 201, 31))
        self.checkProgressTopic.setFont(font)
        self.checkProgressTopic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkProgressTopic.setObjectName("checkProgressTopic")
        self.checkTimeThisWeek = QtWidgets.QCheckBox(self.analytics)
        self.checkTimeThisWeek.setGeometry(QtCore.QRect(360, 170, 331, 31))
        self.checkTimeThisWeek.setFont(font)
        self.checkTimeThisWeek.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkTimeThisWeek.setObjectName("checkTimeThisWeek")
        self.checkTotalTime = QtWidgets.QCheckBox(self.analytics)
        self.checkTotalTime.setGeometry(QtCore.QRect(360, 210, 331, 31))
        self.checkTotalTime.setFont(font)
        self.checkTotalTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkTotalTime.setObjectName("checkTotalTime")
        self.generateGrapLabel = QtWidgets.QLabel(self.analytics)
        self.generateGrapLabel.setGeometry(QtCore.QRect(10, 40, 291, 41))
        self.generateGrapLabel.setFont(font)
        self.generateGrapLabel.setObjectName("generateGrapLabel")
        self.radioTotalProgress = QtWidgets.QRadioButton(self.analytics)
        self.radioTotalProgress.setGeometry(QtCore.QRect(10, 90, 311, 31))
        self.radioTotalProgress.setFont(font)
        self.radioTotalProgress.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioTotalProgress.setObjectName("radioTotalProgress")
        self.graphTopicSelectionGroup = QtWidgets.QButtonGroup(mainMenuWindow)
        self.graphTopicSelectionGroup.setObjectName("graphTopicSelectionGroup")
        self.graphTopicSelectionGroup.addButton(self.radioTotalProgress)
        self.centralLine = QtWidgets.QFrame(self.analytics)
        self.centralLine.setGeometry(QtCore.QRect(340, 50, 20, 291))
        self.centralLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.centralLine.setLineWidth(1)
        self.centralLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.centralLine.setObjectName("centralLine")
        self.radioTotalProgressTopic = QtWidgets.QRadioButton(self.analytics)
        self.radioTotalProgressTopic.setGeometry(QtCore.QRect(10, 130, 311, 31))
        self.radioTotalProgressTopic.setFont(font)
        self.radioTotalProgressTopic.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.radioTotalProgressTopic.setObjectName("radioTotalProgressTopic")
        self.graphTopicSelectionGroup.addButton(self.radioTotalProgressTopic)
        self.generateGraphButton = QtWidgets.QPushButton(self.analytics)
        self.generateGraphButton.setGeometry(QtCore.QRect(10, 280, 331, 51))
        self.generateGraphButton.setFont(font)
        self.generateGraphButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generateGraphButton.setObjectName("generateGraphButton")
        self.radioTimeThisWeek = QtWidgets.QRadioButton(self.analytics)
        self.radioTimeThisWeek.setGeometry(QtCore.QRect(10, 170, 311, 31))
        self.radioTimeThisWeek.setFont(font)
        self.radioTimeThisWeek.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioTimeThisWeek.setObjectName("radioTimeThisWeek")
        self.graphTopicSelectionGroup.addButton(self.radioTimeThisWeek)
        self.radioTotalTime = QtWidgets.QRadioButton(self.analytics)
        self.radioTotalTime.setGeometry(QtCore.QRect(10, 210, 311, 31))
        self.radioTotalTime.setFont(font)
        self.radioTotalTime.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioTotalTime.setChecked(True)
        self.radioTotalTime.setObjectName("radioTotalTime")
        self.graphTopicSelectionGroup.addButton(self.radioTotalTime)
        self.radioPieChart = QtWidgets.QRadioButton(self.analytics)
        self.radioPieChart.setGeometry(QtCore.QRect(80, 240, 121, 31))
        self.radioPieChart.setFont(font)
        self.radioPieChart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioPieChart.setChecked(True)
        self.radioPieChart.setObjectName("radioPieChart")
        self.graphTypeSelect = QtWidgets.QButtonGroup(mainMenuWindow)
        self.graphTypeSelect.setObjectName("graphTypeSelect")
        self.graphTypeSelect.addButton(self.radioPieChart)
        self.typeLabel = QtWidgets.QLabel(self.analytics)
        self.typeLabel.setGeometry(QtCore.QRect(10, 240, 51, 31))
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.radioBarGraph = QtWidgets.QRadioButton(self.analytics)
        self.radioBarGraph.setGeometry(QtCore.QRect(210, 240, 131, 31))
        self.radioBarGraph.setFont(font)
        self.radioBarGraph.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioBarGraph.setObjectName("radioBarGraph")
        self.graphTypeSelect.addButton(self.radioBarGraph)
        self.graphTopicSelect = QtWidgets.QComboBox(self.analytics)
        self.graphTopicSelect.setGeometry(QtCore.QRect(210, 130, 131, 31))
        font.setPointSize(12)
        self.graphTopicSelect.setFont(font)
        self.graphTopicSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphTopicSelect.setAcceptDrops(False)
        self.graphTopicSelect.setStyleSheet("")
        self.graphTopicSelect.setEditable(False)
        self.graphTopicSelect.setObjectName("graphTopicSelect")
        for i in range(14):
            self.graphTopicSelect.addItem("")
        self.emailTopicSelect = QtWidgets.QComboBox(self.analytics)
        self.emailTopicSelect.setGeometry(QtCore.QRect(560, 130, 131, 31))
        self.emailTopicSelect.setFont(font)
        self.emailTopicSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.emailTopicSelect.setAcceptDrops(False)
        self.emailTopicSelect.setStyleSheet("")
        self.emailTopicSelect.setEditable(False)
        self.emailTopicSelect.setObjectName("emailTopicSelect")
        for i in range(14):
            self.emailTopicSelect.addItem("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("./images/pieChartRotated.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget.addTab(self.analytics, icon4, "")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.background.setMinimumSize(QtCore.QSize(801, 411))
        self.background.setMaximumSize(QtCore.QSize(801, 411))
        self.background.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));\n"
            "font-family: veranda;"
        )
        self.background.setText("")
        self.background.setObjectName("background")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font.setPointSize(26)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.background.raise_()
        self.tabWidget.raise_()
        self.titleLabel.raise_()
        self.tabWidget.setCurrentIndex(0)
        self.radioBarGraph.clicked.connect(self.switchGraphButton)
        self.radioPieChart.clicked.connect(self.switchGraphButton)
        self.gameStyleSelect.currentIndexChanged.connect(self.switchCharater)
        self.revisionStyleSelect.currentIndexChanged.connect(self.switchCharater)
        self.logOutButton.clicked.connect(self.logOutMethod)
        self.closeProgramButton.clicked.connect(self.closeProgramMethod)
        self.changeUsername.clicked.connect(self.changeUsernameMethod)
        self.changePassword.clicked.connect(self.changePasswordMethod)
        self.changeUserEmail.clicked.connect(self.changeEmailMethod)
        self.changeTeacherEmail.clicked.connect(self.changeTeacherMethod)
        self.changeGameSettings.clicked.connect(self.changeGameSettingsMethod)
        self.playGameButton.clicked.connect(self.playGameMethod)
        self.playRevisionButton.clicked.connect(self.playRevisionMethod)
        mainMenuWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(mainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(mainMenuWindow)

    def retranslateUi(self, mainMenuWindow):
        # this transate ui doent just add text like previouse of these functions but in many places adds
        # text that is unique to the user, eg 'welcome username'
        _translate = QtCore.QCoreApplication.translate
        mainMenuWindow.setWindowTitle(
            _translate("mainMenuWindow", "Mathematics Revision System")
        )
        self.settingsTitle.setText(_translate("mainMenuWindow", "Settings"))
        self.loggedInLabel.setText(
            _translate(
                "mainMenuWindow", f"Logged in as: {self.userObject.getUsername()}"
            )
        )
        self.changePassword.setText(_translate("mainMenuWindow", "Change Password"))
        self.changeUsername.setText(_translate("mainMenuWindow", "Change Username"))
        self.changeTeacherEmail.setText(
            _translate("mainMenuWindow", "Update Teacher Details")
        )
        self.logOutButton.setText(_translate("mainMenuWindow", "Log Out"))
        self.closeProgramButton.setText(
            _translate("mainMenuWindow", "Close The Program")
        )
        self.changeUserEmail.setText(
            _translate("mainMenuWindow", "Update Your Email Address")
        )
        self.changeGameSettings.setText(
            _translate("mainMenuWindow", "Change Game Settings")
        )
        self.teacherLabel.setText(
            _translate("mainMenuWindow", f"Teacher: {self.teacherData[2]}")
        )
        self.gameModeTitle.setText(_translate("mainMenuWindow", "Game Mode"))
        self.playGameButton.setText(_translate("mainMenuWindow", "Play"))
        self.selectCharacterLabel.setText(
            _translate("mainMenuWindow", "Select your character:")
        )
        self.gameStyleSelect.setItemText(0, _translate("mainMenuWindow", "Euler"))
        self.gameStyleSelect.setItemText(1, _translate("mainMenuWindow", "Turing"))
        self.gameStyleSelect.setItemText(2, _translate("mainMenuWindow", "Lovelace"))
        self.gameStyleSelect.setItemText(3, _translate("mainMenuWindow", "Germain"))
        self.gameStyleSelect.setItemText(4, _translate("mainMenuWindow", "Boole"))
        self.selectTTopicLabel.setText(_translate("mainMenuWindow", "Select a topic:"))
        self.gameTopicSelect.setItemText(
            0, _translate("mainMenuWindow", "Algebraic Expressions")
        )
        self.gameTopicSelect.setItemText(1, _translate("mainMenuWindow", "Quadratics"))
        self.gameTopicSelect.setItemText(
            2, _translate("mainMenuWindow", "Equations and Inequalities")
        )
        self.gameTopicSelect.setItemText(
            3, _translate("mainMenuWindow", "Graphs and Transformations")
        )
        self.gameTopicSelect.setItemText(
            4, _translate("mainMenuWindow", "Straight Line Graphs")
        )
        self.gameTopicSelect.setItemText(5, _translate("mainMenuWindow", "Circles"))
        self.gameTopicSelect.setItemText(
            6, _translate("mainMenuWindow", "Algebraic Methods")
        )
        self.gameTopicSelect.setItemText(
            7, _translate("mainMenuWindow", "Binomial Expansion")
        )
        self.gameTopicSelect.setItemText(8, _translate("mainMenuWindow", "Trig Ratios"))
        self.gameTopicSelect.setItemText(
            9, _translate("mainMenuWindow", "Trig Identities and Equations")
        )
        self.gameTopicSelect.setItemText(10, _translate("mainMenuWindow", "Vectors"))
        self.gameTopicSelect.setItemText(
            11, _translate("mainMenuWindow", "Differentiation")
        )
        self.gameTopicSelect.setItemText(
            12, _translate("mainMenuWindow", "Integration")
        )
        self.gameTopicSelect.setItemText(
            13, _translate("mainMenuWindow", "Exponentials and Logarithms")
        )
        self.gameTopicSuggestionButton.setText(
            _translate("mainMenuWindow", "Get topic suggestion")
        )
        self.revisionModeTitle.setText(_translate("mainMenuWindow", "Revision Mode"))
        self.playRevisionButton.setText(_translate("mainMenuWindow", "Play"))
        self.revisionStyleSelect.setItemText(0, _translate("mainMenuWindow", "Euler"))
        self.revisionStyleSelect.setItemText(1, _translate("mainMenuWindow", "Turing"))
        self.revisionStyleSelect.setItemText(
            2, _translate("mainMenuWindow", "Lovelace")
        )
        self.revisionStyleSelect.setItemText(3, _translate("mainMenuWindow", "Germain"))
        self.revisionStyleSelect.setItemText(4, _translate("mainMenuWindow", "Boole"))
        self.selectCharacterLabelRevision.setText(
            _translate("mainMenuWindow", "Select your character:")
        )
        self.selectTopicLabelRevision.setText(
            _translate("mainMenuWindow", "Select a topic to revise:")
        )
        self.revisionTopicSuggestionButton.setText(
            _translate("mainMenuWindow", "Get topic suggestion")
        )
        self.revisionTopicSelect.setItemText(
            0, _translate("mainMenuWindow", "Algebraic Expressions")
        )
        self.revisionTopicSelect.setItemText(
            1, _translate("mainMenuWindow", "Quadratics")
        )
        self.revisionTopicSelect.setItemText(
            2, _translate("mainMenuWindow", "Equations and Inequalities")
        )
        self.revisionTopicSelect.setItemText(
            3, _translate("mainMenuWindow", "Graphs and Transformations")
        )
        self.revisionTopicSelect.setItemText(
            4, _translate("mainMenuWindow", "Straight Line Graphs")
        )
        self.revisionTopicSelect.setItemText(5, _translate("mainMenuWindow", "Circles"))
        self.revisionTopicSelect.setItemText(
            6, _translate("mainMenuWindow", "Algebraic Methods")
        )
        self.revisionTopicSelect.setItemText(
            7, _translate("mainMenuWindow", "Binomial Expansion")
        )
        self.revisionTopicSelect.setItemText(
            8, _translate("mainMenuWindow", "Trig Ratios")
        )
        self.revisionTopicSelect.setItemText(
            9, _translate("mainMenuWindow", "Trig Identities and Equations")
        )
        self.revisionTopicSelect.setItemText(
            10, _translate("mainMenuWindow", "Vectors")
        )
        self.revisionTopicSelect.setItemText(
            11, _translate("mainMenuWindow", "Differentiation")
        )
        self.revisionTopicSelect.setItemText(
            12, _translate("mainMenuWindow", "Integration")
        )
        self.revisionTopicSelect.setItemText(
            13, _translate("mainMenuWindow", "Exponentials and Logarithms")
        )
        self.analyticsTitle.setText(_translate("mainMenuWindow", "Analytics"))
        self.selectDataLabel.setText(
            _translate(
                "mainMenuWindow", f"Select data to send to {self.teacherData[2]}:"
            )
        )
        self.sendEmailButton.setText(
            _translate("mainMenuWindow", f"Send to {self.teacherData[2]}")
        )
        self.checkTotalProgress.setText(
            _translate("mainMenuWindow", "Total progress through topics")
        )
        self.checkProgressTopic.setText(
            _translate("mainMenuWindow", "Progress on topic:")
        )
        self.checkTimeThisWeek.setText(
            _translate("mainMenuWindow", "Time spent working this week")
        )
        self.checkTotalTime.setText(
            _translate("mainMenuWindow", "Total time spent working")
        )
        self.generateGrapLabel.setText(
            _translate("mainMenuWindow", "Generate a graph:")
        )
        self.radioTotalProgress.setText(
            _translate("mainMenuWindow", "Total progress through topics")
        )
        self.radioTotalProgressTopic.setText(
            _translate("mainMenuWindow", "Progress on topic:")
        )
        self.generateGraphButton.setText(
            _translate("mainMenuWindow", "Generate Pie Chart")
        )
        self.radioTimeThisWeek.setText(
            _translate("mainMenuWindow", "Time spent working this week ")
        )
        self.radioTotalTime.setText(
            _translate("mainMenuWindow", "Total time spent working")
        )
        self.radioPieChart.setText(_translate("mainMenuWindow", "Pie Chart"))
        self.typeLabel.setText(_translate("mainMenuWindow", "Type:"))
        self.radioBarGraph.setText(_translate("mainMenuWindow", "Bar Graph"))
        self.graphTopicSelect.setItemText(
            0, _translate("mainMenuWindow", "Algebraic Expressions")
        )
        self.graphTopicSelect.setItemText(1, _translate("mainMenuWindow", "Quadratics"))
        self.graphTopicSelect.setItemText(
            2, _translate("mainMenuWindow", "Equations and Inequalities")
        )
        self.graphTopicSelect.setItemText(
            3, _translate("mainMenuWindow", "Graphs and Transformations")
        )
        self.graphTopicSelect.setItemText(
            4, _translate("mainMenuWindow", "Straight Line Graphs")
        )
        self.graphTopicSelect.setItemText(5, _translate("mainMenuWindow", "Circles"))
        self.graphTopicSelect.setItemText(
            6, _translate("mainMenuWindow", "Algebraic Methods")
        )
        self.graphTopicSelect.setItemText(
            7, _translate("mainMenuWindow", "Binomial Expansion")
        )
        self.graphTopicSelect.setItemText(
            8, _translate("mainMenuWindow", "Trig Ratios")
        )
        self.graphTopicSelect.setItemText(
            9, _translate("mainMenuWindow", "Trig Identities and Equations")
        )
        self.graphTopicSelect.setItemText(10, _translate("mainMenuWindow", "Vectors"))
        self.graphTopicSelect.setItemText(
            11, _translate("mainMenuWindow", "Differentiation")
        )
        self.graphTopicSelect.setItemText(
            12, _translate("mainMenuWindow", "Integration")
        )
        self.graphTopicSelect.setItemText(
            13, _translate("mainMenuWindow", "Exponentials and Logarithms")
        )
        self.emailTopicSelect.setItemText(
            0, _translate("mainMenuWindow", "Algebraic Expressions")
        )
        self.emailTopicSelect.setItemText(1, _translate("mainMenuWindow", "Quadratics"))
        self.emailTopicSelect.setItemText(
            2, _translate("mainMenuWindow", "Equations and Inequalities")
        )
        self.emailTopicSelect.setItemText(
            3, _translate("mainMenuWindow", "Graphs and Transformations")
        )
        self.emailTopicSelect.setItemText(
            4, _translate("mainMenuWindow", "Straight Line Graphs")
        )
        self.emailTopicSelect.setItemText(5, _translate("mainMenuWindow", "Circles"))
        self.emailTopicSelect.setItemText(
            6, _translate("mainMenuWindow", "Algebraic Methods")
        )
        self.emailTopicSelect.setItemText(
            7, _translate("mainMenuWindow", "Binomial Expansion")
        )
        self.emailTopicSelect.setItemText(
            8, _translate("mainMenuWindow", "Trig Ratios")
        )
        self.emailTopicSelect.setItemText(
            9, _translate("mainMenuWindow", "Trig Identities and Equations")
        )
        self.emailTopicSelect.setItemText(10, _translate("mainMenuWindow", "Vectors"))
        self.emailTopicSelect.setItemText(
            11, _translate("mainMenuWindow", "Differentiation")
        )
        self.emailTopicSelect.setItemText(
            12, _translate("mainMenuWindow", "Integration")
        )
        self.emailTopicSelect.setItemText(
            13, _translate("mainMenuWindow", "Exponentials and Logarithms")
        )
        self.titleLabel.setText(
            _translate("mainMenuWindow", "Mathematics Revision System")
        )

    # settings tab methods:
    # These are all simple methods that close the window and change the selected function so that the main loop
    # will run the correct interface next
    def logOutMethod(self):
        self.selectedFunction = "logOut"
        QtWidgets.qApp.quit()

    def closeProgramMethod(self):
        QtWidgets.qApp.quit()

    def changeUsernameMethod(self):
        self.selectedFunction = "changeUsername"
        QtWidgets.qApp.quit()

    def changePasswordMethod(self):
        self.selectedFunction = "changePassword"
        QtWidgets.qApp.quit()

    def changeEmailMethod(self):
        self.selectedFunction = "updateEmail"
        QtWidgets.qApp.quit()

    def changeTeacherMethod(self):
        self.selectedFunction = "updateTeacherDetails"
        QtWidgets.qApp.quit()

    def changeGameSettingsMethod(self):
        self.selectedFunction = "gameSettings"
        QtWidgets.qApp.quit()

    # play game and play revison are the same as the settings menu functions however they also update game data with the topic
    # that the user has selected and the style that the user has selected, this is used by the main loop when generating a new
    # game instance
    def playGameMethod(self):
        self.selectedFunction = "gameMode"
        self.functionData.append(self.getStyle("game"))
        self.functionData.append(self.gameTopicSelect.currentText())
        QtWidgets.qApp.quit()

    def playRevisionMethod(self):
        self.selectedFunction = "revisionMode"
        self.functionData.append(self.getStyle("revision"))
        self.functionData.append(self.revisionTopicSelect.currentText())
        QtWidgets.qApp.quit()

    # get style returns the paths of the resources for the sprite that the player has chosen.
    # this is used by the play revision and play game methods who need to parse this data to the
    # main loop
    def getStyle(self, mode):
        if mode == "game":
            styleIndex = self.gameStyleSelect.currentIndex() + 1
        else:
            styleIndex = self.revisionStyleSelect.currentIndex() + 1
        walkforward = path.join(
            path.dirname(__file__),
            f".\gameResources\images\style{styleIndex}\walktowards",
        )
        walkbackwards = path.join(
            path.dirname(__file__),
            f".\gameResources\images\style{styleIndex}\walkaway",
        )
        walkleft = path.join(
            path.dirname(__file__),
            f".\gameResources\images\style{styleIndex}\walkleft",
        )
        walkright = path.join(
            path.dirname(__file__),
            f".\gameResources\images\style{styleIndex}\walkright",
        )
        return [walkforward, walkbackwards, walkleft, walkright]

    # this method services both the game tab and the revision tab and switches the sprite shown on screen
    # depending on the mathematician that the user has chosen
    def switchCharater(self):
        if self.tabWidget.currentIndex() == 1:
            index = self.gameStyleSelect.currentIndex()
            image = self.characterImage
        else:
            index = self.revisionStyleSelect.currentIndex()
            image = self.characterImageRevision
        image.setPixmap(QtGui.QPixmap(self.imagePaths[index]))

    # analytics tab mathods:
    def switchGraphButton(self):
        if self.radioBarGraph.isChecked():
            self.generateGraphButton.setText("Generate Bar Graph")
        else:
            self.generateGraphButton.setText("Generate Pie Chart")


# The following classes make the small settings windows, opened from the settings tab in the main menu

# Change username interface:
class Ui_changeUsernameWindow(object):
    def __init__(self, userObject):
        self.userObject = userObject

    def setupUi(self, changeUsernameWindow):
        changeUsernameWindow.setObjectName("changeUsernameWindow")
        changeUsernameWindow.resize(731, 308)
        changeUsernameWindow.setMaximumSize(QtCore.QSize(731, 308))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        changeUsernameWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(changeUsernameWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(-10, 0, 741, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(240, 160, 451, 51))
        font.setPointSize(22)
        self.usernameInput.setFont(font)
        self.usernameInput.setObjectName("usernameInput")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 160, 211, 51))
        font.setPointSize(18)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.usernameLabel.setObjectName("usernameLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 240, 361, 51))
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 240, 161, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setStyleSheet("")
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTitle.setGeometry(QtCore.QRect(20, 80, 271, 51))
        font.setPointSize(18)
        self.activeTitle.setFont(font)
        self.activeTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTitle.setObjectName("activeTitle")
        self.activeUsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.activeUsernameLabel.setGeometry(QtCore.QRect(240, 80, 451, 51))
        self.activeUsernameLabel.setFont(font)
        self.activeUsernameLabel.setAutoFillBackground(False)
        self.activeUsernameLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeUsernameLabel.setObjectName("activeUsernameLabel")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.usernameInput.raise_()
        self.usernameLabel.raise_()
        self.submitButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTitle.raise_()
        self.activeUsernameLabel.raise_()
        changeUsernameWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.submitButton.clicked.connect(self.changeUsernameMethod)
        self.retranslateUi(changeUsernameWindow)
        QtCore.QMetaObject.connectSlotsByName(changeUsernameWindow)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, changeUsernameWindow):
        _translate = QtCore.QCoreApplication.translate
        changeUsernameWindow.setWindowTitle(
            _translate("changeUsernameWindow", "Mathematics Revision System")
        )
        self.titleLabel.setText(
            _translate("changeUsernameWindow", "Please chose a new username")
        )
        self.usernameLabel.setText(_translate("changeUsernameWindow", "New Username: "))
        self.submitButton.setText(_translate("changeUsernameWindow", "Change username"))
        self.mainMenuButton.setText(_translate("changeUsernameWindow", "Main Menu"))
        self.activeTitle.setText(_translate("changeUsernameWindow", "Active Username:"))
        self.activeUsernameLabel.setText(
            _translate("changeUsernameWindow", f"{self.userObject.getUsername()}")
        )

    # closing the window will take them back to the main menu
    def closeWindow(self):
        QtWidgets.qApp.quit()

    # change username double checks that the given username is not already taken and if it isnt changes the username
    def changeUsernameMethod(self):
        newName = self.usernameInput.text().lower()
        unsernameRecords = databaseAccess("SELECT userName FROM tblUsers")
        valid = True
        for records in unsernameRecords:
            if records[0] == newName:
                messageBox(
                    "Input Error",
                    f"Sorry the username {newName} is already in use!",
                    "warning",
                )
                valid = False
        if valid == True:
            databaseAccess(
                f"UPDATE tblUsers SET userName = '{newName}' WHERE userName = '{self.userObject.getUsername()}' "
            )
            messageBox(
                "Database Amended", f"Your new username is {newName}!", "information",
            )
            # if the user record is changed the userobject also needs to be updated
            self.userObject.updateUsername(newName)
            self.closeWindow()


# Change password interface, this is almost identical to the previouse change username window so I am not going to coment over it,
# however there is a change in the retranslateUi method that is commented
class Ui_changePasswordWindow(object):
    def __init__(self, userObject):
        self.userObject = userObject

    def setupUi(self, changePasswordWindow):
        changePasswordWindow.setObjectName("changePasswordWindow")
        changePasswordWindow.resize(731, 308)
        changePasswordWindow.setMaximumSize(QtCore.QSize(731, 308))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        changePasswordWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(changePasswordWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(-10, 0, 741, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(250, 160, 441, 51))
        font.setPointSize(22)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet(";")
        self.passwordInput.setObjectName("passwordInput")
        self.newPassLabel = QtWidgets.QLabel(self.centralwidget)
        self.newPassLabel.setGeometry(QtCore.QRect(20, 160, 201, 51))
        font.setPointSize(18)
        self.newPassLabel.setFont(font)
        self.newPassLabel.setAutoFillBackground(False)
        self.newPassLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.newPassLabel.setObjectName("newPassLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 240, 361, 51))
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 240, 161, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTitle.setGeometry(QtCore.QRect(20, 80, 221, 51))
        font.setPointSize(18)
        self.activeTitle.setFont(font)
        self.activeTitle.setAutoFillBackground(False)
        self.activeTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTitle.setObjectName("activeTitle")
        self.activePasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.activePasswordLabel.setGeometry(QtCore.QRect(250, 80, 441, 51))
        font.setPointSize(18)
        self.activePasswordLabel.setFont(font)
        self.activePasswordLabel.setAutoFillBackground(False)
        self.activePasswordLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activePasswordLabel.setObjectName("activePasswordLabel")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.passwordInput.raise_()
        self.newPassLabel.raise_()
        self.submitButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTitle.raise_()
        self.activePasswordLabel.raise_()
        changePasswordWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.submitButton.clicked.connect(self.changePasswordMethod)
        self.retranslateUi(changePasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(changePasswordWindow)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, changePasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        changePasswordWindow.setWindowTitle(
            _translate("changePasswordWindow", "Mathematics Revision System")
        )
        self.titleLabel.setText(
            _translate("changePasswordWindow", "Change Your Password")
        )
        self.newPassLabel.setText(_translate("changePasswordWindow", "New Password: "))
        self.submitButton.setText(_translate("changePasswordWindow", "Change Password"))
        self.mainMenuButton.setText(_translate("changePasswordWindow", "Main Menu"))
        self.activeTitle.setText(
            _translate("changePasswordWindow", "Current Password:")
        )
        # this script here hashes the current password of the user, if it is of lenght 4 or less it will be completely replaced with *s however if it is
        # more than 4 long its first second, and second to last and last letters will be visible to the user, this can be helpful if you cant remember your
        # password and maybe you dont want to change it, just remember it
        currentPass = databaseAccess(
            f"SELECT password FROM tblUsers WHERE userName = '{self.userObject.getUsername()}' "
        )[0][0]
        if len(currentPass) <= 4:
            displayPass = len(currentPass) * "*"
        else:
            displayPass = f"{currentPass[0]}{currentPass[1]}{(len(currentPass)-4)*'*'}{currentPass[len(currentPass)-2]}{currentPass[len(currentPass)-1]}"
        self.activePasswordLabel.setText(
            _translate("changePasswordWindow", f"{displayPass}")
        )

    def closeWindow(self):
        QtWidgets.qApp.quit()

    def changePasswordMethod(self):
        newPass = self.passwordInput.text()
        databaseAccess(
            f"UPDATE tblUsers SET password = '{newPass}' WHERE userName = '{self.userObject.getUsername()}' "
        )
        messageBox(
            "Database Amended", "Your password has been updated!", "information",
        )
        self.closeWindow()


# Interface for updating user email address, this is also very similar to the change username class
# however it is even simpler as it my program allows multiple users to share a single email address
class Ui_updateEmailWindow(object):
    def __init__(self, userObject):
        self.userObject = userObject

    def setupUi(self, updateEmailWindow):
        updateEmailWindow.setObjectName("updateEmailWindow")
        updateEmailWindow.resize(731, 308)
        updateEmailWindow.setMaximumSize(QtCore.QSize(731, 308))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        updateEmailWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(updateEmailWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(-10, 0, 741, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(180, 160, 511, 51))
        font.setPointSize(22)
        self.emailInput.setFont(font)
        self.emailInput.setObjectName("emailInput")
        self.newEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.newEmailLabel.setGeometry(QtCore.QRect(20, 160, 151, 51))
        font.setPointSize(18)
        self.newEmailLabel.setFont(font)
        self.newEmailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.newEmailLabel.setObjectName("newEmailLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 240, 361, 51))
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 240, 161, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setStyleSheet("")
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTitle.setGeometry(QtCore.QRect(20, 80, 161, 51))
        font.setPointSize(18)
        self.activeTitle.setFont(font)
        self.activeTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTitle.setObjectName("activeTitle")
        self.activeEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.activeEmailLabel.setGeometry(QtCore.QRect(180, 80, 511, 51))
        self.activeEmailLabel.setFont(font)
        self.activeEmailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeEmailLabel.setObjectName("activeEmailLabel")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.emailInput.raise_()
        self.newEmailLabel.raise_()
        self.submitButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTitle.raise_()
        self.activeEmailLabel.raise_()
        updateEmailWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.submitButton.clicked.connect(self.updateEmailMethod)
        self.retranslateUi(updateEmailWindow)
        QtCore.QMetaObject.connectSlotsByName(updateEmailWindow)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, updateEmailWindow):
        _translate = QtCore.QCoreApplication.translate
        updateEmailWindow.setWindowTitle(
            _translate("updateEmailWindow", "Maths Revision System")
        )
        self.titleLabel.setText(
            _translate("updateEmailWindow", "Update your email address")
        )
        self.newEmailLabel.setText(_translate("updateEmailWindow", "New Email: "))
        self.submitButton.setText(_translate("updateEmailWindow", "Update Email"))
        self.mainMenuButton.setText(_translate("updateEmailWindow", "Main Menu"))
        self.activeTitle.setText(_translate("updateEmailWindow", "Active Email:"))
        self.activeEmailLabel.setText(
            _translate("updateEmailWindow", f"{self.userObject.getEmail()}")
        )

    def closeWindow(self):
        QtWidgets.qApp.quit()

    def updateEmailMethod(self):
        newEmail = self.emailInput.text()
        databaseAccess(
            f"UPDATE tblUsers SET email = '{newEmail}' WHERE userName = '{self.userObject.getUsername()}' "
        )
        messageBox(
            "Database Amended",
            "Your email address has been changed, please double check it is correct before going back to the main menu!",
            "information",
        )
        self.userObject.updateEmail(newEmail)
        self.activeEmailLabel.setText(self.userObject.getEmail())


# The interface is a sub menu that can take a user to the change teacher email window or change teacher window
class Ui_updateTeacherWindow(object):
    def __init__(self, userObject):
        self.teacherRecord = databaseAccess(
            f"SELECT * FROM tblTeachers WHERE teacherID = {userObject.getTeacherId()}"
        )
        self.teacher, self.teacherEmail = (
            self.teacherRecord[0][2],
            self.teacherRecord[0][1],
        )
        self.selectedFunction = "notSelected"

    def setupUi(self, updateTeacherWindow):
        updateTeacherWindow.setObjectName("updateTeacherWindow")
        updateTeacherWindow.resize(731, 237)
        updateTeacherWindow.setMinimumSize(QtCore.QSize(731, 237))
        updateTeacherWindow.setMaximumSize(QtCore.QSize(731, 237))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        updateTeacherWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(updateTeacherWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 173))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(-10, 0, 741, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.activeEmailTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeEmailTitle.setGeometry(QtCore.QRect(20, 130, 301, 51))
        font.setPointSize(18)
        self.activeEmailTitle.setFont(font)
        self.activeEmailTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeEmailTitle.setObjectName("activeEmailTitle")
        self.changeEmailButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeEmailButton.setGeometry(QtCore.QRect(20, 180, 271, 51))
        self.changeEmailButton.setFont(font)
        self.changeEmailButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeEmailButton.setAutoDefault(False)
        self.changeEmailButton.setDefault(False)
        self.changeEmailButton.setFlat(False)
        self.changeEmailButton.setObjectName("changeEmailButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(580, 180, 131, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(30)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTeacherTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTeacherTitle.setGeometry(QtCore.QRect(20, 80, 211, 51))
        font.setPointSize(18)
        self.activeTeacherTitle.setFont(font)
        self.activeTeacherTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTeacherTitle.setObjectName("activeTeacherTitle")
        self.activeTeacher = QtWidgets.QLabel(self.centralwidget)
        self.activeTeacher.setGeometry(QtCore.QRect(230, 80, 461, 51))
        self.activeTeacher.setFont(font)
        self.activeTeacher.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTeacher.setObjectName("activeTeacher")
        self.activeEmail = QtWidgets.QLabel(self.centralwidget)
        self.activeEmail.setGeometry(QtCore.QRect(320, 130, 461, 51))
        self.activeEmail.setFont(font)
        self.activeEmail.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeEmail.setObjectName("activeEmail")
        self.changeTeacherButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeTeacherButton.setGeometry(QtCore.QRect(300, 180, 271, 51))
        self.changeTeacherButton.setFont(font)
        self.changeTeacherButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeTeacherButton.setAutoDefault(False)
        self.changeTeacherButton.setDefault(False)
        self.changeTeacherButton.setFlat(False)
        self.changeTeacherButton.setObjectName("changeTeacherButton")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.activeEmailTitle.raise_()
        self.changeEmailButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTeacherTitle.raise_()
        self.activeTeacher.raise_()
        self.activeEmail.raise_()
        self.changeTeacherButton.raise_()
        updateTeacherWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.changeEmailButton.clicked.connect(self.changeEmail)
        self.changeTeacherButton.clicked.connect(self.changeTeacher)
        self.retranslateUi(updateTeacherWindow)
        QtCore.QMetaObject.connectSlotsByName(updateTeacherWindow)

    def retranslateUi(self, updateTeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        updateTeacherWindow.setWindowTitle(
            _translate("updateTeacherWindow", "Maths Revision System")
        )
        self.titleLabel.setText(
            _translate("updateTeacherWindow", "Update Teacher Details")
        )
        self.activeEmailTitle.setText(
            _translate("updateTeacherWindow", "Current Teacher's Email:")
        )
        self.changeEmailButton.setText(
            _translate("updateTeacherWindow", "Change Email")
        )
        self.mainMenuButton.setText(_translate("updateTeacherWindow", "Main Menu"))
        self.activeTeacherTitle.setText(
            _translate("updateTeacherWindow", "Current Teacher:")
        )
        self.activeTeacher.setText(_translate("updateTeacherWindow", f"{self.teacher}"))
        self.activeEmail.setText(
            _translate("updateTeacherWindow", f"{self.teacherEmail}")
        )
        self.changeTeacherButton.setText(
            _translate("updateTeacherWindow", "Change Teacher")
        )

    # the functions here are very simple either close and go to the main menu or close and tell the main loop to open either the
    # change email function or change teacher function
    def closeWindow(self):
        QtWidgets.qApp.quit()

    def changeEmail(self):
        self.selectedFunction = "email"
        self.closeWindow()

    def changeTeacher(self):
        self.selectedFunction = "newTeacher"
        self.closeWindow()


# change teacher email is a window that allows the user to change the email address that is linked to the user
class Ui_changeTeacherEmailWindow(object):
    def __init__(self, userObject, teacherRecord):
        self.userObject = userObject
        self.teacherId = teacherRecord[0]
        self.teacherEmail = teacherRecord[1]
        self.teacher = teacherRecord[2]

    def setupUi(self, changeTeacherEmailWindow):
        changeTeacherEmailWindow.setObjectName("changeTeacherEmailWindow")
        changeTeacherEmailWindow.resize(731, 269)
        changeTeacherEmailWindow.setMinimumSize(QtCore.QSize(731, 269))
        changeTeacherEmailWindow.setMaximumSize(QtCore.QSize(731, 269))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("./images/А.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        changeTeacherEmailWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(changeTeacherEmailWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 233))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 297))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(-10, 0, 741, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(190, 150, 491, 41))
        font.setPointSize(18)
        self.emailInput.setFont(font)
        self.emailInput.setObjectName("emailInput")
        self.thierEmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.thierEmailLabel.setGeometry(QtCore.QRect(10, 150, 171, 41))
        self.thierEmailLabel.setFont(font)
        self.thierEmailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.thierEmailLabel.setObjectName("thierEmailLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 210, 361, 51))
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 210, 161, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(30)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTitle.setGeometry(QtCore.QRect(10, 90, 161, 51))
        font.setPointSize(18)
        self.activeTitle.setFont(font)
        self.activeTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTitle.setObjectName("activeTitle")
        self.teacherName = QtWidgets.QLabel(self.centralwidget)
        self.teacherName.setGeometry(QtCore.QRect(190, 90, 501, 51))
        self.teacherName.setFont(font)
        self.teacherName.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.teacherName.setObjectName("teacherName")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.emailInput.raise_()
        self.thierEmailLabel.raise_()
        self.submitButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTitle.raise_()
        self.teacherName.raise_()
        changeTeacherEmailWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.submitButton.clicked.connect(self.changeEmail)
        self.retranslateUi(changeTeacherEmailWindow)
        QtCore.QMetaObject.connectSlotsByName(changeTeacherEmailWindow)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, changeTeacherEmailWindow):
        _translate = QtCore.QCoreApplication.translate
        changeTeacherEmailWindow.setWindowTitle(
            _translate("changeTeacherEmailWindow", "Maths Revision System")
        )
        self.titleLabel.setText(
            _translate("changeTeacherEmailWindow", "What is your teacher's email?")
        )
        self.thierEmailLabel.setText(
            _translate("changeTeacherEmailWindow", "Their Email:")
        )
        self.submitButton.setText(
            _translate("changeTeacherEmailWindow", "Update Email")
        )
        self.mainMenuButton.setText(_translate("changeTeacherEmailWindow", "Main Menu"))
        self.activeTitle.setText(
            _translate("changeTeacherEmailWindow", "Your Teacher:")
        )
        self.teacherName.setText(
            _translate("changeTeacherEmailWindow", f"{self.teacher}")
        )

    def closeWindow(self):
        QtWidgets.qApp.quit()

    # this function looks quite complecated but boils down to, does this new email match another teacher and do they want to switch to that teacher
    def changeEmail(self):
        email = self.emailInput.text().lower()
        while True:
            # this selection statement vlaidates that the user has enterd a new email for the teacher and that they have actually entered some form
            # of email address
            if email == "":
                messageBox(
                    "Input Error", "Please input a valid email address", "warning"
                )
                break
            elif email == self.teacherEmail:
                messageBox(
                    "Duplicate Error",
                    f"Sorry {self.teacher}'s email is already stored as {email}",
                    "warning",
                )
                break
            elif ("@" in email) == False:
                messageBox(
                    "Input Error", "Please input a valid email address", "warning"
                )
                break
            # recorded teacher is a variable set to true if the email entered matches another user stored in the database
            teacherRecords = databaseAccess("SELECT * from tblTeachers")
            recordedTeacher = False
            duplicateTeacherRecord = ""
            for record in teacherRecords:
                if record[1] == email:
                    recordedTeacher = True
                    duplicateTeacherRecord = record
            # if the teacher email matches another stored teacher email the program gives the chance for the usre to either re-enter the email address or switch the teacher that is linked to their account
            if recordedTeacher == True:
                # yes no box is similar to messagebox except it gets an input from the user
                result = yesNoBox(
                    "Email Adress Recognised",
                    f"This email adress is already in the system and is linked to a {duplicateTeacherRecord[2]}. Would you like {duplicateTeacherRecord[2]} to be your new teacher for this program? This would mean data about your work will only be sent to {duplicateTeacherRecord[2]} and not {self.teacher}",
                )
                # if the user says yes then the teacehr id is changed and updated in the user's record
                if result == QMessageBox.Ok:
                    self.userObject.updateTeacherId(duplicateTeacherRecord[0])
                    databaseAccess(
                        f"UPDATE tblUsers SET teacherId = '{self.userObject.getTeacherId()}' WHERE userName = '{self.userObject.getUsername()}' "
                    )
                    messageBox(
                        "Records amended sucessfully!",
                        f"{duplicateTeacherRecord[2]} is now your registered teacher.",
                        "information",
                    )
                    self.closeWindow()
            else:
                # if it is not a duplicate then the email adress for the teacher is changed
                databaseAccess(
                    f"UPDATE tblTeachers SET teacherEmail = '{email}' WHERE teacherID = {self.userObject.getTeacherId()}"
                )
                messageBox(
                    "Records amended sucessfully!",
                    f"{self.teacher}'s email address has been sucessfully changed to {email}.",
                    "information",
                )
                self.closeWindow()
            break


# change teacher window allows the user to change who their teacher is
class Ui_changeTeacherWindow(object):
    def __init__(self, userObject, teacherRecord):
        self.userObject = userObject
        self.teacher = teacherRecord[2]
        self.teacherId = teacherRecord[0]
        self.teacherEmail = teacherRecord[1]

    def setupUi(self, changeTeacherWindow):
        changeTeacherWindow.setObjectName("changeTeacherWindow")
        changeTeacherWindow.resize(731, 308)
        changeTeacherWindow.setMaximumSize(QtCore.QSize(731, 308))
        changeTeacherWindow.setStyleSheet(
            "QComboBox {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: rgba(0,212,255,1);\n"
            "    color: black;\n"
            "    background-color: rgba(220, 240, 255, 1);\n"
            "}"
            "QPushButton {\n"
            "    background: rgba(220, 240, 255, 0.5);\n"
            "}\n"
            "QLineEdit {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(changeTeacherWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(731, 308))
        self.centralwidget.setMaximumSize(QtCore.QSize(731, 308))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 731, 81))
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.teacherEmailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherEmailInput.setGeometry(QtCore.QRect(210, 170, 481, 41))
        font.setPointSize(18)
        self.teacherEmailInput.setFont(font)
        self.teacherEmailInput.setObjectName("teacherEmailInput")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(20, 170, 191, 41))
        self.emailLabel.setFont(font)
        self.emailLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.emailLabel.setObjectName("emailLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(180, 240, 361, 51))
        font.setPointSize(22)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(False)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 240, 161, 51))
        font.setPointSize(15)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 731, 351))
        font.setPointSize(30)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(204,246,255,1), stop:0.25 rgba(109,230,255,1), stop:0.5 rgba(0,212,255,1), stop:0.75 rgba(81,226,255,1), stop:1 rgba(204,246,255,1));"
        )
        self.backgroundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.activeTitle = QtWidgets.QLabel(self.centralwidget)
        self.activeTitle.setGeometry(QtCore.QRect(20, 90, 181, 41))
        font.setPointSize(18)
        self.activeTitle.setFont(font)
        self.activeTitle.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.activeTitle.setObjectName("activeTitle")
        self.teacherSurnameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.teacherSurnameInput.setGeometry(QtCore.QRect(350, 90, 341, 41))
        self.teacherSurnameInput.setFont(font)
        self.teacherSurnameInput.setObjectName("teacherSurnameInput")
        self.teacherPrefixInput = QtWidgets.QComboBox(self.centralwidget)
        self.teacherPrefixInput.setGeometry(QtCore.QRect(210, 90, 131, 41))
        self.teacherPrefixInput.setFont(font)
        self.teacherPrefixInput.setAcceptDrops(False)
        self.teacherPrefixInput.setEditable(False)
        self.teacherPrefixInput.setObjectName("teacherPrefixInput")
        self.teacherPrefixInput.addItem("")
        self.teacherPrefixInput.addItem("")
        self.teacherPrefixInput.addItem("")
        self.backgroundLabel.raise_()
        self.titleLabel.raise_()
        self.teacherEmailInput.raise_()
        self.emailLabel.raise_()
        self.submitButton.raise_()
        self.mainMenuButton.raise_()
        self.activeTitle.raise_()
        self.teacherSurnameInput.raise_()
        self.teacherPrefixInput.raise_()
        changeTeacherWindow.setCentralWidget(self.centralwidget)
        self.mainMenuButton.clicked.connect(self.closeWindow)
        self.submitButton.clicked.connect(self.changeTeacherMethod)
        self.retranslateUi(changeTeacherWindow)
        QtCore.QMetaObject.connectSlotsByName(changeTeacherWindow)
        self.submitButton.setShortcut("Return")

    def retranslateUi(self, changeTeacherWindow):
        _translate = QtCore.QCoreApplication.translate
        changeTeacherWindow.setWindowTitle(
            _translate("changeTeacherWindow", "Maths Revision System")
        )
        self.titleLabel.setText(
            _translate("changeTeacherWindow", "Give the details of your new teacher")
        )
        self.emailLabel.setText(_translate("changeTeacherWindow", "Teacher Email:"))
        self.submitButton.setText(_translate("changeTeacherWindow", "Submit Details"))
        self.mainMenuButton.setText(_translate("changeTeacherWindow", "Main Menu"))
        self.activeTitle.setText(_translate("changeTeacherWindow", "Teacher Name:"))
        self.teacherSurnameInput.setPlaceholderText(
            _translate("changeTeacherWindow", "Surname")
        )
        self.teacherPrefixInput.setItemText(0, _translate("changeTeacherWindow", "Mr"))
        self.teacherPrefixInput.setItemText(1, _translate("changeTeacherWindow", "Mrs"))
        self.teacherPrefixInput.setItemText(
            2, _translate("changeTeacherWindow", "Miss")
        )

    def closeWindow(self):
        QtWidgets.qApp.quit()

    # change teacher method is similar to the change email method in the changeTeacherEmail class as it allows for the user to either switch teachers or log a new one in the system
    def changeTeacherMethod(self):
        # all of the inputed data is fetched
        namePrefix = self.teacherPrefixInput.currentText()
        surname = self.teacherSurnameInput.text()
        email = self.teacherEmailInput.text()
        fullName = f"{namePrefix} {surname}"
        teacherRecords = databaseAccess(
            f"SELECT * FROM tblTeachers WHERE teacherID != '{self.teacherId}'"
        )
        while True:
            # first there is validation on the inputs, magking sure that the data is not duplicate or is the data of the users current teacher
            if fullName == "" or email == "":
                messageBox(
                    "Input Error",
                    "Please input your teachers name and their email address",
                    "warning",
                )
                break
            elif "@" not in email:
                messageBox(
                    "Input Error", "Please input a valid email address", "warning"
                )
                break
            elif fullName == self.teacher and email == self.teacherEmail:
                messageBox(
                    "Duplicate Error",
                    f"{self.teacher} is already your registered teacher!",
                    "warning",
                )
                break
            elif email == self.teacherEmail:
                messageBox(
                    "Duplicate Error",
                    f"{self.teacher} is already your registered teacher!",
                    "warning",
                )
                break
            # registered teacher is true if the teacher is already in teh system
            registeredTeacher = False
            newTeacherName = ""
            newTeacherId = ""
            changeTeacher = True
            for teacher in teacherRecords:
                if teacher[1] == email and teacher[2] == fullName:
                    newTeacherName = teacher[2]
                    newTeacherId = teacher[0]
                    registeredTeacher = True
                    break
                elif teacher[1] == email:
                    # the result of this yes no box determins whether the user wants to change teachers
                    result = yesNoBox(
                        "Email Address Recognised!",
                        f"The Email you have entered matches a {teacher[2]}, would you like {teacher[2]} to be your new teacher?",
                    )
                    if result == QMessageBox.Ok:
                        newTeacherName = teacher[2]
                        newTeacherId = teacher[0]
                    else:
                        changeTeacher = False
                    registeredTeacher = True
                    break
                elif teacher[2] == fullName:
                    # this code runs if the teachers name matches the name entered but the email doesnt, this can happen if there were two Mr Jones for example
                    result = yesNoBox(
                        "Name Recognised!",
                        f"The Name you have entered matches a {teacher[2]}, but the email does not match, if {teacher[1]} is actually the email of your teacher press ok however if you are sure you inputed the correct email adress, click cancel and we will add this new teacher to our records.",
                    )
                    if result == QMessageBox.Ok:
                        newTeacherName = teacher[2]
                        newTeacherId = teacher[0]
                        registeredTeacher = True
                        break
            # if the detaiks uputed match a teacher and the user wants to switch to this teahcer then the user object and records are updated
            if registeredTeacher == True and changeTeacher == True:
                self.userObject.updateTeacherId(newTeacherId)
                databaseAccess(
                    f"UPDATE tblUsers SET teacherID = {newTeacherId} WHERE userName = '{self.userObject.getUsername()}'"
                )
                messageBox(
                    "Database Amended!",
                    f"Teacher Successfully changed, your new teacher is {newTeacherName}",
                    "information",
                )
                self.closeWindow()
            elif registeredTeacher == False:
                # if the teachers detials are new then a new teacher record is create and is linked to the user's record
                teacherId = len(teacherRecords) + 1
                self.userObject.updateTeacherId(teacherId)
                databaseAccess(
                    (
                        "INSERT INTO tblTeachers (teacherID, teacherEmail, teacherName) VALUES(?, ?, ?)"
                    ),
                    (teacherId, email, fullName),
                )
                databaseAccess(
                    f"UPDATE tblUsers SET teacherID = {teacherId} WHERE userName = '{self.userObject.getUsername()}'"
                )
                messageBox(
                    "Database Amended!",
                    f"Teacher Successfully added, your new teacher is {fullName}",
                    "information",
                )
                self.closeWindow()
            break


# these functions are independant of classes and are used by all classes to improve the efficiency of the code
# they are all simple but since they are used in multiple places putting them in a function makes my life easier

# This function is used to send emails
def sendMail(subject, body, emailRecipient):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # this gmail account was set up for this program to use it's only use is this program
    server.login("mathrevisionprogram@gmail.com", "------") #password removed for github
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("mathrevisionprogram@gmail.com", emailRecipient, msg)
    server.quit()


# This function is used to access the program's database:
def databaseAccess(query, args=0):
    databaseFile = "database/CourseworkDatabase.db"
    databaseConnection = sqlite3.connect(databaseFile)
    cursor = databaseConnection.cursor()
    if args == 0:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    fetchedData = cursor.fetchall()
    databaseConnection.commit()
    return fetchedData


# This function is used to display message boxes to users, I made a function for it as it has to be used in many places
def messageBox(title, content, iconType="information"):
    msgBox = QMessageBox()
    if iconType == "information":
        msgBox.setIcon(QMessageBox.Information)
    elif iconType == "question":
        msgBox.setIcon(QMessageBox.Question)
    elif iconType == "warning":
        msgBox.setIcon(QMessageBox.Warning)
    else:
        msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText(content)
    msgBox.setWindowTitle(title)
    msgBox.exec()


# this function presents a message box that takes a yes no input from the user
def yesNoBox(title, content):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg.exec_()  # this will return the yes or no selection from the user

