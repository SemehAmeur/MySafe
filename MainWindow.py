from UI.ui_mainwindow import Ui_MainWindow
import sqlite3
import history
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app, user, decryptPass, consoleOldWindow):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.show()
        self.allDataTableWidget.setColumnHidden(0, True)
        self.allDataTableWidget.setColumnHidden(11, True)
        self.db_to_preview()
        self.addPushButton.clicked.connect(self.add_to_db)
        self.generatePasswordPushButton.clicked.connect(self.generate_password_btn)
        self.copyPushButton.clicked.connect(self.copy_pass_word)
        self.deletePushButton.clicked.connect(self.delete_password)
        self.updatePushButton.clicked.connect(self.update_btn)
        self.actionChange_Password.triggered.connect(self.change_password)
        self.actionLog_Out.triggered.connect(self.logout)
        self.actionClose.triggered.connect(self.closemyapp)
        self.actionHowToUse.triggered.connect(self.how_to_use)
        self.actionAbout_this_Software.triggered.connect(self.about_this_software)
        self.visualizeDataPushButton.clicked.connect(self.check_data_btn)
        self.actionHistory.triggered.connect(self.history_btn)

    def history_btn(self):
        self.history = history.History(self.app, self.user)
    def how_to_use(self):
        QMessageBox.information(self, 'How to use MySafe?',
                             'I tried to create a simple interface suitable for everyone.\n'
                             'So everything is clear and I hope you don\'t find any\n'
                             'difficulty while using this app. I tried my best to apply\n'
                             'a UX (User Experience) to make it easy for everyone to use.\n'
                             'for the buttons below:\n'
                             '-Update: When you click on Update button on the main window\n'
                             '\t  you are just updating the current cell. So make sure to click it\n'
                             '\t  every time you modify a cell. It doesn\'t update the entire row\n'
                             '-Copy:  When you click the copy button, you are just copying the password,\n'
                             '\t(no matter what cell you selected, you just copied the associate\n '
                             '\tpassword)other data you must copy it manually.\n'
                             'I am sure that other buttons works the same the way you are thinking about.',
                             QMessageBox.Ok)
    def about_this_software(self):
        QMessageBox.information(self, 'About this MySafe',
                                'I have been always afraid about my identity'
                                '\non the internet, So I generally create accounts\n'
                                'with different passwords or wrong information\n'
                                'and as always I forget the related information\n'
                                'so I lose access.\n'
                                'And that is why I decided to create MySafe where\n'
                                'I can store all my passwords while I am feeling Safe\n'
                                'Maybe you are confused why you are reading such thing.\n'
                                'Well I have created MySaffe to use it and share it\n'
                                'with others having the same problem\n'
                                'You may also find it strange to store data with different\n'
                                'information each time.\n'
                                'Well, each time I create an account with different information\n'
                                'because back in 2020 I received a message from a friend\n'
                                'about a fake account using my name and my photo.\n'
                                'You have all the reasons to use MySafe\n'
                                'and why not improve it since it is an open source or\n'
                                'you can contact me to improve it',
                                QMessageBox.Ok)
    def check_data_btn(self):
        try:
            data_to_check_id = self.allDataTableWidget.item(self.allDataTableWidget.currentRow(), 0).text()
            self.check_data = CheckData(self.app, self, data_to_check_id, self.decryptPass)

        except:
            QMessageBox.critical(self, 'Unvailable Data',
                                 'Please select a data to preview the information',
                                 QMessageBox.Ok)
    def closemyapp(self):
        self.close()

    def logout(self):
        self.hide()
        self.oldConsole.myshow()
        def update_btn(self):
        ret = QMessageBox.critical(self, 'Updating',
                                   'Are you sure about updating this item?',
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            tableWidgetDict = {1: 'password_website', 2: 'password_link', 3: 'password_linked_website',
                               4: 'password_mail',
                               5: 'password_second_mail', 6: 'password_username', 7: 'password_first_name',
                               8: 'password_last_name', 9: 'password_birthdate', 10: 'password_phone',
                               12: 'password_security_question', 13: 'password_answer', 14: 'password_main_device',
                               15: 'password_purpose_of_use'}

            toUpdate = tableWidgetDict[self.allDataTableWidget.currentColumn()]
            newValue = self.allDataTableWidget.currentItem().text()
            cr = EncryptDecrypt(self.decryptPass)
            newValue = cr.encrypt(newValue)
            valueId = self.allDataTableWidget.item(self.allDataTableWidget.currentRow(), 0).text()
            statement = ('UPDATE passwords SET ' + toUpdate + ' = ?  WHERE password_id = ' + valueId)
            param = (newValue,)
            self.cursor.execute(statement, param)
            self.connection.commit()
    def change_password(self):
        self.chngpass = ChangePassword(self.app, self.user)
        def add_to_db(self):

        # Check for the inputs and get result
        bol, param = self.check_inputs()
        if bol:
            # add the written data to the table
            row_position = self.allDataTableWidget.rowCount()
            self.allDataTableWidget.insertRow(row_position)
            for i in range(16):
                self.allDataTableWidget.setItem(row_position, i + 1, QTableWidgetItem(param[i]))

            # crypt data
            cr = EncryptDecrypt(self.decryptPass)
            # Loop through the list of data to store inside the DB
            for i in range(len(param)):
                param[i] = cr.encrypt(param[i])
            # The username should not be cyphered because I need to use it in fetching data from database
            param.append(self.user)

            params = tuple(param)
            # Inserting Data inside the DataBase
            statement = "INSERT INTO passwords VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(statement, params)
            self.connection.commit()
            param = [self.websiteNameLineEdit, self.websiteLinkLineEdit, self.linkedWebsiteLineEdit, self.emailLineEdit,
                     self.secondEmailLineEdit, self.usernameLineEdit, self.firstNameLineEdit, self.lastNameLineEdit,
                     self.phoneNumerLineEdit, self.passwordLineEdit, self.securityQuestionLineEdit, self.answerLineEdit,
                     self.mainDeviceLineEdit, self.purposeOfUseLineEdit]

            # assign the id to the row
            statement = 'SELECT password_id FROM passwords WHERE user_id = "' + self.user + '"'
            self.cursor.execute(statement)
            output = self.cursor.fetchall()
            self.connection.commit()

            the_id = (str(output[-1][0]))
            self.allDataTableWidget.setItem(row_position, 0, QTableWidgetItem(the_id))

            # empty the edit_lines
            # self.birthDateEdit
            for el in param:
                el.setText("")
            self.notePlainTextEdit.setPlainText("")
    def check_inputs(self):
        param = [self.websiteNameLineEdit.text(), self.websiteLinkLineEdit.text(), self.linkedWebsiteLineEdit.text(),
                 self.emailLineEdit.text(), self.secondEmailLineEdit.text(), self.usernameLineEdit.text(),
                 self.firstNameLineEdit.text(), self.lastNameLineEdit.text(), self.birthDateEdit.text(),
                 self.phoneNumerLineEdit.text(), self.passwordLineEdit.text(), self.securityQuestionLineEdit.text(),
                 self.answerLineEdit.text(), self.mainDeviceLineEdit.text(), self.purposeOfUseLineEdit.text(),
                 self.notePlainTextEdit.toPlainText()]

        if (self.websiteNameLineEdit.text() != "" and (
                self.emailLineEdit.text() != "" or self.usernameLineEdit.text() != "") and
                self.passwordLineEdit.text() != ""):
            return True, param
        else:
            QMessageBox.critical(self, 'Hint',
                                 'Please make sure to insert a website name, \na username or an email, and a password.',
                                 QMessageBox.Ok)
            return False, None