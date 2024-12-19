from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import subprocess
from IPython.display import display, Javascript
import os
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("11.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 981, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 460, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(219,112,147);\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.next_page)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "DRUG EYE DETECTION"))
        self.pushButton.setText(_translate("Form", "Next"))

    def next_page(self):
        self.Form22 = QtWidgets.QWidget()
        self.ui = Ui_Form22()
        self.ui.setupUi(self.Form22)
        self.Form22.show()
        Form.close()

class Ui_Form22(object):
    def setupUi(self, Form22):
        Form22.setObjectName("Form22")
        Form22.resize(800,600)
        self.label = QtWidgets.QLabel(Form22)
        self.label.setGeometry(QtCore.QRect(0, 0, 800,600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("22.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form22)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 501, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255,255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form22)
        self.label_3.setGeometry(QtCore.QRect(180, 280, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form22)
        self.label_4.setGeometry(QtCore.QRect(180, 190, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255,255,255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form22)
        self.lineEdit.setGeometry(QtCore.QRect(450, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form22)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 290, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form22)
        self.pushButton.setGeometry(QtCore.QRect(470, 400, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(219,112,147);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.next_page)

        self.lineEdit_6 = QtWidgets.QLineEdit(Form22)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 450, 381, 51))
        self.lineEdit_6.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(255,255,255,255);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "paddin-bottom:7px;\n"
                                    "font: 14pt \"MS Shell Dlg 2\";\n"
                                    "")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form22)
        self.lineEdit_21.setGeometry(QtCore.QRect(300, 500, 381, 51))
        self.lineEdit_21.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(255,255,255,255);\n"
                                      "color: rgb(255,255, 255);\n"
                                      "paddin-bottom:7px;\n"
                                      "font: 14pt \"MS Shell Dlg 2\";\n"
                                      "")
        self.lineEdit_21.setObjectName("lineEdit_21")

        self.retranslateUi(Form22)
        QtCore.QMetaObject.connectSlotsByName(Form22)
        Form22.setWindowTitle("Admin login")


    def retranslateUi(self, Form22):
        _translate = QtCore.QCoreApplication.translate
        Form22.setWindowTitle(_translate("Form2", "Form"))
        self.label_2.setText(_translate("Form2", "LOG IN "))
        self.label_3.setText(_translate("Form2", "PASSWORD:"))
        self.label_4.setText(_translate("Form2", "USER_NAME:"))
        self.pushButton.setText(_translate("Form2", "LOG IN"))


    def next_page(self):
        n1 = self.lineEdit.text()
        n2 = self.lineEdit_2.text()
        if n1 == 'project':
            print("correct username")
            self.lineEdit_6.setText("correct username")
            if n2 == '123':
                print("correct password")
                self.lineEdit_21.setText("correct password")
                self.Form3 = QtWidgets.QWidget()
                self.ui = Ui_Form3()
                self.ui.setupUi(self.Form3)
                self.Form3.show()
                
            else:
                print("wrong password")
                self.lineEdit_21.setText("wrong password")
        else:
            print("wrong username")
            self.lineEdit_6.setText("wrong username")
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import subprocess
class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(800, 600)
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("33.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 851, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(Form3)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 410, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(219,112,147);\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_drug_eye_detection)  # Connect the button to the function

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form"))
        self.label_4.setText(_translate("Form3", "DETECT THE DRUGGED PERSONS "))

        self.pushButton_2.setText(_translate("Form3", "DETECT"))

    def open_drug_eye_detection(self):
    # Function to run main program when Detect button is pressed
        def run_main_program():
            #subprocess.run(["jupyter", "nbconvert", "--to", "script", "main.ipynb"])  # Convert notebook to script
            subprocess.run(["python", "main.py"])
    
        run_main_program()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())