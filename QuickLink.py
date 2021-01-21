from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

# Each button has 2 lists. One has the URLs that will be pulled up in a browser. The URLs are split into parts if they have a variable and stored in the non "X_show" list
# The X_Show lists are only used to display URLs on the UI
btn_1 = [] 
btn_1_Show = []
btn_2 = [] 
btn_2_Show = []
btn_3 = []
btn_3_Show = []
btn_4 = [] 
btn_4_Show = []
btn_5 = [] 
btn_5_Show = []
btn_6 = []
btn_6_Show = []
btn_7 = [] 
btn_7_Show = []
btn_8 = [] 
btn_8_Show = []
btn_9 = []
btn_9_Show = []
btn_10 = [] 
btn_10_Show = []
btn_11 = [] 
btn_11_Show = []
btn_12 = []
btn_12_Show = []
labels = []

with open("C:\\Quick link\\output.txt", 'r+') as f:
        line_number = 0
        for line in f:
                urls = line.split(',')             
                for x in urls:            
                        if(line_number == 0):
                                temp = x.split("+")
                                for y in temp:
                                        btn_1.insert(len(btn_1), y)                  #Splitting urls into seperate parts
                                btn_1_Show.insert(len(btn_1_Show), x)
                        elif(line_number == 1):
                                temp = x.split("+")
                                for y in temp:
                                        btn_2.insert(len(btn_2), y)                  #Splitting urls into seperate parts
                                btn_2_Show.insert(len(btn_2_Show), x)
                        elif(line_number == 2):
                                temp = x.split("+")
                                for y in temp:
                                        btn_3.insert(len(btn_3), y)                  #Splitting urls into seperate parts
                                btn_3_Show.insert(len(btn_3_Show), x)
                        elif(line_number == 3):
                                temp = x.split("+")
                                for y in temp:
                                        btn_4.insert(len(btn_4), y)                  #Splitting urls into seperate parts
                                btn_4_Show.insert(len(btn_4_Show), x)
                        elif(line_number == 4):
                                temp = x.split("+")
                                for y in temp:
                                        btn_5.insert(len(btn_5), y)                  #Splitting urls into seperate parts
                                btn_5_Show.insert(len(btn_5_Show), x)
                        elif(line_number == 5):
                                temp = x.split("+")
                                for y in temp:
                                        btn_6.insert(len(btn_6), y)                  #Splitting urls into seperate parts
                                btn_6_Show.insert(len(btn_6_Show), x)
                        elif(line_number == 6):
                                temp = x.split("+")
                                for y in temp:
                                        btn_7.insert(len(btn_7), y)                  #Splitting urls into seperate parts
                                btn_7_Show.insert(len(btn_7_Show), x)
                        elif(line_number == 7):
                                temp = x.split("+")
                                for y in temp:
                                        btn_8.insert(len(btn_8), y)                   #Splitting urls into seperate parts
                                btn_8_Show.insert(len(btn_8_Show), x)
                        elif(line_number == 8):
                                temp = x.split("+")
                                for y in temp:
                                        btn_9.insert(len(btn_9), y)                  #Splitting urls into seperate parts
                                btn_9_Show.insert(len(btn_9_Show), x)
                        elif(line_number == 9):
                                temp = x.split("+")
                                for y in temp:
                                        btn_10.insert(len(btn_10), y)                #Splitting urls into seperate parts
                                btn_10_Show.insert(len(btn_10_Show), x)
                        elif(line_number == 10):
                                temp = x.split("+")
                                for y in temp:
                                        btn_11.insert(len(btn_11), y)                #Splitting urls into seperate parts
                                btn_11_Show.insert(len(btn_11_Show), x)
                        elif(line_number == 11):
                                temp = x.split("+")
                                for y in temp:
                                        btn_12.insert(len(btn_12), y)                #Splitting urls into seperate parts
                                btn_12_Show.insert(len(btn_12_Show), x)
                        else:
                                labels.insert(len(labels), x)                                                                                                                                                                                                                                                                                                   
                line_number = line_number + 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 550)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Store = "*"
        self.Register = "*"
        self.TransactionNumber = "*"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)       # Button declarations start here 
        self.pushButton.setGeometry(QtCore.QRect(100, 150, 100, 60))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.numCheck)        
        self.pushButton.clicked.connect(self.clicked1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 100, 60))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.numCheck)
        self.pushButton_2.clicked.connect(self.clicked2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 150, 100, 60))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.numCheck)
        self.pushButton_3.clicked.connect(self.clicked3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 150, 100, 60))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.numCheck)
        self.pushButton_4.clicked.connect(self.clicked4)        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 255, 100, 60))
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.numCheck)
        self.pushButton_5.clicked.connect(self.clicked5)        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 255, 100, 60))
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.numCheck)
        self.pushButton_6.clicked.connect(self.clicked6)        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 255, 100, 60))
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.numCheck)
        self.pushButton_7.clicked.connect(self.clicked7)        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 255, 100, 60))
        self.pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.numCheck)
        self.pushButton_8.clicked.connect(self.clicked8)        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 360, 100, 60))
        self.pushButton_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.numCheck)
        self.pushButton_9.clicked.connect(self.clicked9)        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 360, 100, 60))
        self.pushButton_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.numCheck)
        self.pushButton_10.clicked.connect(self.clicked10)        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 360, 100, 60))
        self.pushButton_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.numCheck)
        self.pushButton_11.clicked.connect(self.clicked11)        
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(550, 360, 100, 60))
        self.pushButton_12.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.numCheck)
        self.pushButton_12.clicked.connect(self.clicked12)        
        self.label = QtWidgets.QLabel(self.centralwidget)                  #Label declarations start here
        self.label.setGeometry(QtCore.QRect(140, 120, 47, 13))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 120, 47, 13))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 120, 75, 13))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 120, 50, 13))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 225, 47, 13))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 225, 75, 13))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 225, 60, 13))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 225, 110, 13))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 330, 47, 13))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 330, 75, 13))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(410, 330, 80, 13))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(570, 330, 47, 13))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)         #Line-edit 1 declaration here
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 113, 30))   
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setInputMask("9999")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(120, 40, 70, 10))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)       #Line-edit 2 declaration here
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 60, 113, 30))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setInputMask("99")
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(310, 38, 80, 15))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)       #Line-edit 3 declaration here
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 60, 113, 30))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_3.setInputMask("9999")
        self.lineEdit_3.setMaxLength(4)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(490, 38, 100, 15))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.listView = QtWidgets.QListView(self.centralwidget)             #List-view declaration here
        self.listView.setGeometry(QtCore.QRect(690, 20, 310, 192))
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(690, 260, 100, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_13.clicked.connect(self.addURL)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(900, 260, 100, 40))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_14.clicked.connect(self.removeURL)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)                   #Combo-box declaration here
        self.comboBox.setGeometry(QtCore.QRect(690, 320, 310, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.currentIndexChanged.connect(self.update_Listview)           #Line-edit 4 declaration here
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 220, 310, 30))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(795, 260, 100, 40))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_15.clicked.connect(self.label_Change)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Setting all of the text for the labels, buttons, and combo-box start here
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Link"))
        self.pushButton.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_2.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_3.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_4.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_5.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_6.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_7.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_8.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_9.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_10.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_11.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_12.setText(_translate("MainWindow", "Click Here"))
        self.pushButton_13.setText(_translate("MainWindow", "Add"))
        self.pushButton_14.setText(_translate("MainWindow", "Remove"))
        self.pushButton_15.setText(_translate("MainWindow", "Rename"))
        self.label.setText(str(labels[0]))
        self.label_2.setText(str(labels[1]))
        self.label_3.setText(str(labels[2]))
        self.label_4.setText(str(labels[3]))
        self.label_5.setText(str(labels[4]))     
        self.label_6.setText(str(labels[5]))        
        self.label_7.setText(str(labels[6]))       
        self.label_8.setText(str(labels[7]))     
        self.label_9.setText(str(labels[8]))      
        self.label_10.setText(str(labels[9]))      
        self.label_11.setText(str(labels[10]))       
        self.label_12.setText(str(labels[11]))        
        self.label_13.setText(_translate("MainWindow", "Store Number"))
        self.label_14.setText(_translate("MainWindow", "Register Number"))
        self.label_15.setText(_translate("MainWindow", "Transaction Number"))
        for x in range(0, 12):
                self.comboBox.addItem(labels[x])

    #This method checks if the numbers for store, register, etc. are formatted correctly
    def numCheck(self):
        temp = str(self.lineEdit.text())
        temp2 = str(self.lineEdit_2.text())
        temp3 = str(self.lineEdit_3.text())
        if (len(temp) == 3):
            self.lineEdit.setText("0" + temp)
            self.Store = str(self.lineEdit.text())
        else:
             self.Store = str(self.lineEdit.text())   
        if(len(temp2) == 1):
            self.lineEdit_2.setText("0" + temp2)
            self.Register = str(self.lineEdit_2.text())
        else:
             self.Register = str(self.lineEdit_2.text())
        if(len(temp3) == 3):
            self.lineEdit_3.setText("0" + temp3)
            self.TransactionNumber = str(self.lineEdit_3.text())
        else:
             self.TransactionNumber = str(self.lineEdit_3.text())
        if(len(temp) == 0):
            self.Store = "*"
        if(len(temp2) == 0):
            self.Register = "*"
        if(len(temp3) == 0):
            self.TransactionNumber = "*"
        

    #This method updates the labels if their texts are changed.
    def label_Change(self):
        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                        buf = in_file.readlines()
        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                count = 1
                for line in buf:
                        if(count < 13):
                                out_file.write(line)
                        count = count + 1
                new_Name = str(self.lineEdit_4.text())
                if(self.comboBox.currentIndex() == 0):
                        labels.pop(0)
                        labels.insert(0, new_Name)
                        self.comboBox.removeItem(0)
                        self.comboBox.insertItem(0, new_Name)
                        self.label.setText(new_Name)
                        self.comboBox.setCurrentIndex(0)
                elif(self.comboBox.currentIndex() == 1):
                        labels.pop(1)
                        labels.insert(1, new_Name)
                        self.comboBox.removeItem(1)
                        self.comboBox.insertItem(1, new_Name)
                        self.label_2.setText(new_Name)
                        self.comboBox.setCurrentIndex(1)
                elif(self.comboBox.currentIndex() == 2):
                        labels.pop(2)
                        labels.insert(2, new_Name)
                        self.comboBox.removeItem(2)
                        self.comboBox.insertItem(2, new_Name)
                        self.label_3.setText(new_Name)
                        self.comboBox.setCurrentIndex(2)
                elif(self.comboBox.currentIndex() == 3):
                        labels.pop(3)
                        labels.insert(3, new_Name)
                        self.comboBox.removeItem(3)
                        self.comboBox.insertItem(3, new_Name)
                        self.label_4.setText(new_Name)
                        self.comboBox.setCurrentIndex(3)
                elif(self.comboBox.currentIndex() == 4):
                        labels.pop(4)
                        labels.insert(4, new_Name)
                        self.comboBox.removeItem(4)
                        self.comboBox.insertItem(4, new_Name)
                        self.label_5.setText(new_Name)
                        self.comboBox.setCurrentIndex(4)
                elif(self.comboBox.currentIndex() == 5):
                        labels.pop(5)
                        labels.insert(5, new_Name)
                        self.comboBox.removeItem(5)
                        self.comboBox.insertItem(5, new_Name)
                        self.label_6.setText(new_Name)
                        self.comboBox.setCurrentIndex(5)
                elif(self.comboBox.currentIndex() == 6):
                        labels.pop(6)
                        labels.insert(6, new_Name)
                        self.comboBox.removeItem(6)
                        self.comboBox.insertItem(6, new_Name)
                        self.label_7.setText(new_Name)
                        self.comboBox.setCurrentIndex(6)
                elif(self.comboBox.currentIndex() == 7):
                        labels.pop(7)
                        labels.insert(7, new_Name)
                        self.comboBox.removeItem(7)
                        self.comboBox.insertItem(7, new_Name)
                        self.label_8.setText(new_Name)
                        self.comboBox.setCurrentIndex(7)
                elif(self.comboBox.currentIndex() == 8):
                        labels.pop(8)
                        labels.insert(8, new_Name)
                        self.comboBox.removeItem(8)
                        self.comboBox.insertItem(8, new_Name)
                        self.label_9.setText(new_Name)
                        self.comboBox.setCurrentIndex(8)
                elif(self.comboBox.currentIndex() == 9):
                        labels.pop(9)
                        labels.insert(9, new_Name)
                        self.comboBox.removeItem(9)
                        self.comboBox.insertItem(9, new_Name)
                        self.label_10.setText(new_Name)
                        self.comboBox.setCurrentIndex(9)
                elif(self.comboBox.currentIndex() == 10):
                        labels.pop(10)
                        labels.insert(10, new_Name)
                        self.comboBox.removeItem(10)
                        self.comboBox.insertItem(10, new_Name)
                        self.label_11.setText(new_Name)
                        self.comboBox.setCurrentIndex(10)
                elif(self.comboBox.currentIndex() == 11):
                        labels.pop(11)
                        labels.insert(11, new_Name)
                        self.comboBox.removeItem(11)
                        self.comboBox.insertItem(11, new_Name)
                        self.label_12.setText(new_Name)
                        self.comboBox.setCurrentIndex(11)
                self.lineEdit_4.setText("")
                count = 0
                while(count < 11):
                        out_file.write(str(labels[count]) + ",")
                        count = count + 1
                out_file.write(str(labels[count]) + "\n")

    #This method Updates the listview component when the drop down component changes index 
    def update_Listview(self):
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)    
        if(self.comboBox.currentIndex() == 0):
               for i in btn_1_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item) 
        elif(self.comboBox.currentIndex() == 1):
               for i in btn_2_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item) 
        elif(self.comboBox.currentIndex() == 2):
               for i in btn_3_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 3):
               for i in btn_4_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 4):
               for i in btn_5_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 5):
               for i in btn_6_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 6):
               for i in btn_7_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 7):
               for i in btn_8_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 8):
               for i in btn_9_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 9):
               for i in btn_10_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        elif(self.comboBox.currentIndex() == 10):
               for i in btn_11_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        else:
               for i in btn_12_Show:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)

    # Adds a URL to the specified button. Handles writing them to the txt file and adding 
    # them to current lists so they can be used right away.
    def addURL(self):
            if(str(self.lineEdit_4.text()) != ""):
                if(self.comboBox.currentIndex() == 0):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_1_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_1_Show) == 1 and btn_1_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 1):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 1):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_1.insert(len(btn_1)-1, y)               # Splitting urls into seperate parts
                                                                btn_1_Show.insert(len(btn_1_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 1):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_1.insert(len(btn_1), y)               # Splitting urls into seperate parts
                                                btn_1_Show.insert(len(btn_1_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 1):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_2_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_2_Show) == 1 and btn_2_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 2):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 2):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_2.insert(len(btn_2)-1, y)               # Splitting urls into seperate parts
                                                                btn_2_Show.insert(len(btn_2_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 2):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_2.insert(len(btn_2), y)               # Splitting urls into seperate parts
                                                btn_2_Show.insert(len(btn_2_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 2):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_3_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_3_Show) == 1 and btn_3_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 3):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 3):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_3.insert(len(btn_3)-1, y)               # Splitting urls into seperate parts
                                                                btn_3_Show.insert(len(btn_3_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 3):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_3.insert(len(btn_3), y)               # Splitting urls into seperate parts
                                                btn_3_Show.insert(len(btn_3_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 3):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_4_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_4_Show) == 1 and btn_4_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 4):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 4):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_4.insert(len(btn_4)-1, y)               # Splitting urls into seperate parts
                                                                btn_4_Show.insert(len(btn_4_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 4):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_4.insert(len(btn_4), y)               # Splitting urls into seperate parts
                                                btn_4_Show.insert(len(btn_4_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 4):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_5_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_5_Show) == 1 and btn_5_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 5):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 5):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_5.insert(len(btn_5)-1, y)               # Splitting urls into seperate parts
                                                                btn_5_Show.insert(len(btn_5_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 5):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_5.insert(len(btn_5), y)               # Splitting urls into seperate parts
                                                btn_5_Show.insert(len(btn_5_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 5):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_6_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_6_Show) == 1 and btn_6_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 6):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 6):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_6.insert(len(btn_6)-1, y)               # Splitting urls into seperate parts
                                                                btn_6_Show.insert(len(btn_6_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 6):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_6.insert(len(btn_6), y)               # Splitting urls into seperate parts
                                                btn_6_Show.insert(len(btn_6_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 6):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_7_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_7_Show) == 1 and btn_7_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 7):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 7):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_7.insert(len(btn_7)-1, y)               # Splitting urls into seperate parts
                                                                btn_7_Show.insert(len(btn_7_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 7):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_7.insert(len(btn_7), y)               # Splitting urls into seperate parts
                                                btn_7_Show.insert(len(btn_7_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 7):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_8_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_8_Show) == 1 and btn_8_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 8):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 8):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_8.insert(len(btn_8)-1, y)               # Splitting urls into seperate parts
                                                                btn_8_Show.insert(len(btn_8_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 8):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_8.insert(len(btn_8), y)               # Splitting urls into seperate parts
                                                btn_8_Show.insert(len(btn_8_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 8):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_9_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_9_Show) == 1 and btn_9_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 9):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 9):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_9.insert(len(btn_9)-1, y)               # Splitting urls into seperate parts
                                                                btn_9_Show.insert(len(btn_9_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 9):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_9.insert(len(btn_9), y)               # Splitting urls into seperate parts
                                                btn_9_Show.insert(len(btn_9_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 9):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_10_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_10_Show) == 1 and btn_10_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 2):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 2):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_10.insert(len(btn_10)-1, y)               # Splitting urls into seperate parts
                                                                btn_10_Show.insert(len(btn_10_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 10):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_10.insert(len(btn_10), y)               # Splitting urls into seperate parts
                                                btn_10_Show.insert(len(btn_10_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 10):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_11_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_11_Show) == 1 and btn_11_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 11):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 11):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_11.insert(len(btn_11)-1, y)               # Splitting urls into seperate parts
                                                                btn_11_Show.insert(len(btn_11_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 11):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_11.insert(len(btn_11), y)               # Splitting urls into seperate parts
                                                btn_11_Show.insert(len(btn_11_Show), temp)
                                out_file.close()
                                in_file.close()
                elif(self.comboBox.currentIndex() == 11):
                        temp = str(self.lineEdit_4.text())        
                        if(temp not in btn_12_Show):       
                                with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                        buf = in_file.readlines()
                                temp = str(self.lineEdit_4.text())
                                with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                        if(len(btn_12_Show) == 1 and btn_12_Show[0] == "\n"):    # If the list is empty
                                                count = 1
                                                for line in buf:
                                                        if(count < 12):
                                                                out_file.write(line)
                                                                count = count + 1                
                                                        elif(count == 12):
                                                                out_file.write(temp + line)
                                                                temp2 = temp.split("+")
                                                                for y in temp2:
                                                                        btn_12.insert(len(btn_12)-1, y)               # Splitting urls into seperate parts
                                                                btn_12_Show.insert(len(btn_12_Show)-1, temp)
                                                                count = count + 1
                                                        else:
                                                                out_file.write(line)
                                        else:
                                                count = 1
                                                for line in buf:
                                                        if(count == 12):
                                                                line = str.rstrip(line) + "," + str.rstrip(temp) + "\n"  
                                                                out_file.write(line)
                                                        else:
                                                                out_file.write(line)
                                                        count = count + 1
                                                temp2 = temp.split("+")
                                                for y in temp2:
                                                        btn_12.insert(len(btn_12), y)               # Splitting urls into seperate parts
                                                btn_12_Show.insert(len(btn_12_Show), temp)
                                out_file.close()
                                in_file.close()
                self.update_Listview()
                self.lineEdit_4.setText("")

    # Removes a URL from the application. Handles removing the URL from the txt file and from the lists 
    def removeURL(self):
            if(str(self.lineEdit_4.text()) != ""):
                temp = str(self.lineEdit_4.text())
                if(self.comboBox.currentIndex() == 0):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 1):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_1_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_1_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_1_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_1_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_1.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_1.pop(index)               # Splitting urls into seperate parts
                                                                                btn_1_Show.remove(x)
                                                                                if(len(btn_1_Show) == 0):
                                                                                        btn_1_Show.insert(0,"\n")
                                                                                        btn_1.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_1.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_1.pop(index)               # Splitting urls into seperate parts
                                                                                btn_1_Show.remove(x)
                                                                                if(len(btn_1_Show) == 0):
                                                                                        btn_1_Show.insert(0,"\n")
                                                                                        btn_1.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_1_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_1.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_1.pop(index)               # Splitting urls into seperate parts
                                                                                btn_1_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_1.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_1.pop(index)               # Splitting urls into seperate parts
                                                                                btn_1_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 1):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 2):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_2_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_2_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_2_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_2_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_2.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_2.pop(index)               # Splitting urls into seperate parts
                                                                                btn_2_Show.remove(x)
                                                                                if(len(btn_2_Show) == 0):
                                                                                        btn_2_Show.insert(0,"\n")
                                                                                        btn_2.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_2.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_2.pop(index)               # Splitting urls into seperate parts
                                                                                btn_2_Show.remove(x)
                                                                                if(len(btn_2_Show) == 0):
                                                                                        btn_2_Show.insert(0,"\n")
                                                                                        btn_2.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_2_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_2.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_2.pop(index)               # Splitting urls into seperate parts
                                                                                btn_2_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_2.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_2.pop(index)               # Splitting urls into seperate parts
                                                                                btn_2_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 2):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 3):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_3_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_3_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_3_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_3_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_3.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_3.pop(index)               # Splitting urls into seperate parts
                                                                                btn_3_Show.remove(x)
                                                                                if(len(btn_3_Show) == 0):
                                                                                        btn_3_Show.insert(0,"\n")
                                                                                        btn_3.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_3.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_3.pop(index)               # Splitting urls into seperate parts
                                                                                btn_3_Show.remove(x)
                                                                                if(len(btn_3_Show) == 0):
                                                                                        btn_3_Show.insert(0,"\n")
                                                                                        btn_3.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_3_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_3.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_3.pop(index)               # Splitting urls into seperate parts
                                                                                btn_3_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_3.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_3.pop(index)               # Splitting urls into seperate parts
                                                                                btn_3_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 3):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 4):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_4_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_4_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_4_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_4_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_4.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_4.pop(index)               # Splitting urls into seperate parts
                                                                                btn_4_Show.remove(x)
                                                                                if(len(btn_4_Show) == 0):
                                                                                        btn_4_Show.insert(0,"\n")
                                                                                        btn_4.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_4.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_4.pop(index)               # Splitting urls into seperate parts
                                                                                btn_4_Show.remove(x)
                                                                                if(len(btn_4_Show) == 0):
                                                                                        btn_4_Show.insert(0,"\n")
                                                                                        btn_4.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_4_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_4.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_4.pop(index)               # Splitting urls into seperate parts
                                                                                btn_4_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_4.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_4.pop(index)               # Splitting urls into seperate parts
                                                                                btn_4_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 4):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 5):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_5_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_5_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_5_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_5_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_5.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_5.pop(index)               # Splitting urls into seperate parts
                                                                                btn_5_Show.remove(x)
                                                                                if(len(btn_5_Show) == 0):
                                                                                        btn_5_Show.insert(0,"\n")
                                                                                        btn_5.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_5.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_5.pop(index)               # Splitting urls into seperate parts
                                                                                btn_5_Show.remove(x)
                                                                                if(len(btn_5_Show) == 0):
                                                                                        btn_5_Show.insert(0,"\n")
                                                                                        btn_5.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_5_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_5.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_5.pop(index)               # Splitting urls into seperate parts
                                                                                btn_5_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_5.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_5.pop(index)               # Splitting urls into seperate parts
                                                                                btn_5_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 5):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 6):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_6_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_6_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_6_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_6_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_6.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_6.pop(index)               # Splitting urls into seperate parts
                                                                                btn_6_Show.remove(x)
                                                                                if(len(btn_6_Show) == 0):
                                                                                        btn_6_Show.insert(0,"\n")
                                                                                        btn_6.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_6.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_6.pop(index)               # Splitting urls into seperate parts
                                                                                btn_6_Show.remove(x)
                                                                                if(len(btn_6_Show) == 0):
                                                                                        btn_6_Show.insert(0,"\n")
                                                                                        btn_6.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_6_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_6.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_6.pop(index)               # Splitting urls into seperate parts
                                                                                btn_6_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_6.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_6.pop(index)               # Splitting urls into seperate parts
                                                                                btn_6_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 6):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 7):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_7_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_7_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_7_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_7_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_7.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_7.pop(index)               # Splitting urls into seperate parts
                                                                                btn_7_Show.remove(x)
                                                                                if(len(btn_7_Show) == 0):
                                                                                        btn_7_Show.insert(0,"\n")
                                                                                        btn_7.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_7.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_7.pop(index)               # Splitting urls into seperate parts
                                                                                btn_7_Show.remove(x)
                                                                                if(len(btn_7_Show) == 0):
                                                                                        btn_7_Show.insert(0,"\n")
                                                                                        btn_7.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_7_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_7.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_7.pop(index)               # Splitting urls into seperate parts
                                                                                btn_7_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_7.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_7.pop(index)               # Splitting urls into seperate parts
                                                                                btn_7_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 7):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 8):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_8_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_8_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_8_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_8_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_8.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_8.pop(index)               # Splitting urls into seperate parts
                                                                                btn_8_Show.remove(x)
                                                                                if(len(btn_8_Show) == 0):
                                                                                        btn_8_Show.insert(0,"\n")
                                                                                        btn_8.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_8.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_8.pop(index)               # Splitting urls into seperate parts
                                                                                btn_8_Show.remove(x)
                                                                                if(len(btn_8_Show) == 0):
                                                                                        btn_8_Show.insert(0,"\n")
                                                                                        btn_8.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_8_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_8.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_8.pop(index)               # Splitting urls into seperate parts
                                                                                btn_8_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_8.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_8.pop(index)               # Splitting urls into seperate parts
                                                                                btn_8_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 8):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 9):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_9_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_9_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_9_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_9_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_9.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_9.pop(index)               # Splitting urls into seperate parts
                                                                                btn_9_Show.remove(x)
                                                                                if(len(btn_9_Show) == 0):
                                                                                        btn_9_Show.insert(0,"\n")
                                                                                        btn_9.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_9.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_9.pop(index)               # Splitting urls into seperate parts
                                                                                btn_9_Show.remove(x)
                                                                                if(len(btn_9_Show) == 0):
                                                                                        btn_9_Show.insert(0,"\n")
                                                                                        btn_9.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_9_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_9.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_9.pop(index)               # Splitting urls into seperate parts
                                                                                btn_9_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_9.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_9.pop(index)               # Splitting urls into seperate parts
                                                                                btn_9_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 9):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 10):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_10_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_10_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_10_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_10_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_10.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_10.pop(index)               # Splitting urls into seperate parts
                                                                                btn_10_Show.remove(x)
                                                                                if(len(btn_10_Show) == 0):
                                                                                        btn_10_Show.insert(0,"\n")
                                                                                        btn_10.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_10.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_10.pop(index)               # Splitting urls into seperate parts
                                                                                btn_10_Show.remove(x)
                                                                                if(len(btn_10_Show) == 0):
                                                                                        btn_10_Show.insert(0,"\n")
                                                                                        btn_10.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_10_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_10.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_10.pop(index)               # Splitting urls into seperate parts
                                                                                btn_10_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_10.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_10.pop(index)               # Splitting urls into seperate parts
                                                                                btn_10_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                elif(self.comboBox.currentIndex() == 10):
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 11):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_11_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_11_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_11_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_11_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_11.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_11.pop(index)               # Splitting urls into seperate parts
                                                                                btn_11_Show.remove(x)
                                                                                if(len(btn_11_Show) == 0):
                                                                                        btn_11_Show.insert(0,"\n")
                                                                                        btn_11.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_11.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_11.pop(index)               # Splitting urls into seperate parts
                                                                                btn_11_Show.remove(x)
                                                                                if(len(btn_11_Show) == 0):
                                                                                        btn_11_Show.insert(0,"\n")
                                                                                        btn_11.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_11_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_11.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_11.pop(index)               # Splitting urls into seperate parts
                                                                                btn_11_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_11.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_11.pop(index)               # Splitting urls into seperate parts
                                                                                btn_11_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                else:
                        with open("C:\\Quick link\\output.txt", 'r') as in_file:
                                buf = in_file.readlines()
                        with open("C:\\Quick link\\output.txt", 'w') as out_file:
                                notFound = True
                                line_number = 1                                
                                for line in buf:
                                        if(line_number == 12):
                                                urls = line.split(",")
                                                count = 1
                                                for x in urls:
                                                        if(x.find(temp) == -1):
                                                                if(len(btn_12_Show) - 1 == count and notFound == True):
                                                                        out_file.write(x)
                                                                elif(len(btn_12_Show) == count and notFound == True):
                                                                        out_file.write("," + x)
                                                                elif(len(btn_12_Show) == count):
                                                                        if(x.find("\n") != -1):
                                                                                out_file.write(x)
                                                                        else:
                                                                                out_file.write(x + "\n") 
                                                                else:        
                                                                        out_file.write(x + ",")
                                                        else:
                                                                if(x.find("\n") != -1):
                                                                        out_file.write("\n")
                                                                        if(x.find("\n") != -1 and x in btn_12_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_12.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_12.pop(index)               # Splitting urls into seperate parts
                                                                                btn_12_Show.remove(x)
                                                                                if(len(btn_12_Show) == 0):
                                                                                        btn_12_Show.insert(0,"\n")
                                                                                        btn_12.insert(0,"\n")                                                                                
                                                                        else:
                                                                                x = str.rstrip(x)        
                                                                                temp2 = x.split("+")
                                                                                index = btn_12.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_12.pop(index)               # Splitting urls into seperate parts
                                                                                btn_12_Show.remove(x)
                                                                                if(len(btn_12_Show) == 0):
                                                                                        btn_12_Show.insert(0,"\n")
                                                                                        btn_12.insert(0,"\n")
                                                                else:        
                                                                        notFound = False
                                                                        if(x in btn_12_Show):
                                                                                temp2 = x.split("+")
                                                                                index = btn_12.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_12.pop(index)               # Splitting urls into seperate parts
                                                                                btn_12_Show.remove(x)
                                                                        else:
                                                                                x = x + "\n"
                                                                                temp2 = x.split("+")
                                                                                index = btn_12.index(temp2[0])
                                                                                for y in temp2:
                                                                                        btn_12.pop(index)               # Splitting urls into seperate parts
                                                                                btn_12_Show.remove(x)  
                                                                count = count - 1
                                                        count = count + 1
                                        else:
                                                out_file.write(line)
                                        line_number = line_number + 1
                self.update_Listview()
                self.lineEdit_4.setText("")
                out_file.close()
                in_file.close()

                            
    # These methods are click events for the buttons. 
    def clicked1(self):
        item_number = 0
        puzzle = btn_1[item_number]
        temp = []
        for item in btn_1:
                if(btn_1[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_1[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_1[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_1[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_1[item_number]
                        item_number = item_number + 1                        
                elif(btn_1[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked2(self):                
        item_number = 0
        puzzle = btn_2[item_number]
        temp = []
        for item in btn_2:
                if(btn_2[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_2[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_2[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_2[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_2[item_number]
                        item_number = item_number + 1                        
                elif(btn_2[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)
    
    def clicked3(self):
        item_number = 0
        puzzle = btn_3[item_number]
        temp = []
        for item in btn_3:
                if(btn_3[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_3[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_3[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_3[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_3[item_number]
                        item_number = item_number + 1                        
                elif(btn_3[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked4(self):
        item_number = 0
        puzzle = btn_4[item_number]
        temp = []
        for item in btn_4:
                if(btn_4[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_4[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_4[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_4[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_4[item_number]
                        item_number = item_number + 1                        
                elif(btn_4[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked5(self):
        item_number = 0
        puzzle = btn_5[item_number]
        temp = []
        for item in btn_5:
                if(btn_5[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_5[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_5[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_5[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_5[item_number]
                        item_number = item_number + 1                        
                elif(btn_5[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked6(self):
        item_number = 0
        puzzle = btn_6[item_number]
        temp = []
        for item in btn_6:
                if(btn_6[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_6[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_6[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_6[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_6[item_number]
                        item_number = item_number + 1                        
                elif(btn_6[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked7(self):
        item_number = 0
        puzzle = btn_7[item_number]
        temp = []
        for item in btn_7:
                if(btn_7[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_7[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_7[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_7[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_7[item_number]
                        item_number = item_number + 1                        
                elif(btn_7[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked8(self):
        item_number = 0
        puzzle = btn_8[item_number]
        temp = []
        for item in btn_8:
                if(btn_8[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_8[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_8[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_8[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_8[item_number]
                        item_number = item_number + 1                        
                elif(btn_8[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked9(self):
        item_number = 0
        puzzle = btn_9[item_number]
        temp = []
        for item in btn_9:
                if(btn_9[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_9[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_9[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_9[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_9[item_number]
                        item_number = item_number + 1                        
                elif(btn_9[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked10(self):
        item_number = 0
        puzzle = btn_10[item_number]
        temp = []
        for item in btn_10:
                if(btn_10[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_10[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_10[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_10[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_10[item_number]
                        item_number = item_number + 1                        
                elif(btn_10[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked11(self):
        item_number = 0
        puzzle = btn_11[item_number]
        temp = []
        for item in btn_11:
                if(btn_11[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_11[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_11[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_11[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_11[item_number]
                        item_number = item_number + 1                        
                elif(btn_11[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)

    def clicked12(self):
        item_number = 0
        puzzle = btn_12[item_number]
        temp = []
        for item in btn_12:
                if(btn_12[item_number] == " Store "):
                        puzzle = puzzle + self.Store
                        item_number = item_number + 1
                elif(btn_12[item_number] == " Register "):
                        puzzle = puzzle + self.Register
                        item_number = item_number + 1
                elif(btn_12[item_number] == " TransactionNumber "):
                        puzzle = puzzle + self.TransactionNumber
                        item_number = item_number + 1
                elif(btn_12[item_number].find("http") != -1 and item_number != 0):
                        temp.insert(len(temp), puzzle)
                        puzzle = btn_12[item_number]
                        item_number = item_number + 1                        
                elif(btn_12[item_number] != puzzle):
                        puzzle = puzzle + item
                        item_number = item_number + 1
                else:
                        item_number = item_number + 1
        temp.insert(len(temp), puzzle)                
        for url in temp:
                webbrowser.get('chrome').open_new(url)                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    f.close()
    sys.exit(app.exec_())
