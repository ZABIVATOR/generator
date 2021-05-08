import warnings
#primer tochek 3 3 2 2 2 5 -2 3 -2 0 0 -3
import sys
warnings.filterwarnings("ignore")
import gmsh
from datetime import date
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QHBoxLayout, QLabel, QLineEdit,QPushButton,QGridLayout,QInputDialog, QDoubleSpinBox
from PyQt5.QtGui import QIcon, QPixmap

try:
	#Mac/Linux
	from PyQt5.QtWinExtras import QtWin
	myappid = 'mycompany.myproduct.subproduct.version'
	QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
	pass

class bd(QWidget):#oshibka

	def __init__(self):
		super().__init__()

		self.initUI()

		
		#if(self.v==0):
			#self.g=bd()
			#self.g.show()
		
		
	def initUI(self):

		hbox = QHBoxLayout(self)
		pixmap = QPixmap("bsod_2.jpg")
		self.setGeometry(-13, -13, 1920, 1080)
		lbl = QLabel(self)
		lbl.setPixmap(pixmap)
		hbox.addWidget(lbl)
		self.setLayout(hbox)


def gmh(a,p):
	n=int(len(p)/2)
	if n>3 and a>0:
		gmsh.initialize()
		lc = 0.1
		gmsh.model.add("ownfigure")
		print(p)
		for i in range(n):
			gmsh.model.geo.addPoint(p[2*i+0], p[2*i+1], 0, lc, i+1)
		for i in range(n-1):
			gmsh.model.geo.addLine(i+1, i+2, i+1)
		gmsh.model.geo.addLine(n, 1, n)
		gmsh.model.geo.addCurveLoop([i+1 for i in range(n)], 1)
#dyrka
		gmsh.model.geo.addPoint(0, 0, 0, lc, n+1)
		gmsh.model.geo.addPoint(a, 0, 0, lc, n+2)
		gmsh.model.geo.addPoint(-a, 0, 0, lc, n+3)
		gmsh.model.geo.addCircleArc(n+2, n+1, n+3, n+1)
		gmsh.model.geo.addCircleArc(n+3, n+1, n+2, n+2)
		gmsh.model.geo.addCurveLoop([n+1, n+2], 2)
#generazia
		gmsh.model.geo.addPlaneSurface([1,-2], 1)
		gmsh.model.geo.synchronize()
		gmsh.model.mesh.generate(2)
		if '-nopopup' not in sys.argv:
			gmsh.fltk.run()
		gmsh.write("ownfigure.msh") 
		gmsh.finalize()
		#3 3 2 2 1 5 -1 3 -2 0 0 -3



class Ui_m1(object):
    def setupUi(self, m1):
        m1.setObjectName("m1")
        m1.resize(430, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(m1.sizePolicy().hasHeightForWidth())
        m1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        m1.setFont(font)
        self.w1 = QtWidgets.QWidget(m1)
        self.w1.setObjectName("w1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.w1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 320, 401, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.w1)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 401, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.w1)
        self.label.setGeometry(QtCore.QRect(20, 40, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.w1)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 321, 21))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.w1)
        self.doubleSpinBox.setGeometry(QtCore.QRect(260, 10, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_3 = QtWidgets.QLabel(self.w1)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 55, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.w1)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 390, 321, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.w1)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 241, 21))
        self.label_4.setObjectName("label_4")
        m1.setCentralWidget(self.w1)

        self.retranslateUi(m1)
        QtCore.QMetaObject.connectSlotsByName(m1)

    def retranslateUi(self, m1):
        _translate = QtCore.QCoreApplication.translate
        m1.setWindowTitle(_translate("m1", "Mesh Generator"))
        self.pushButton_2.setText(_translate("m1", "Плохой"))
        self.pushButton.setText(_translate("m1", "Правильный"))
        self.label.setText(_translate("m1", "Введите точки граничной кривой:"))
        self.label_2.setText(_translate("m1", "Введите радиус скважины:"))
        self.label_3.setText(_translate("m1", "м"))
        self.pushButton_3.setText(_translate("m1", "Найди 5 отличий"))
        self.label_4.setText(_translate("m1", "Генератор сетки"))



class Window(QMainWindow, Ui_m1):#input of points
	def __init__(self):
		super().__init__()
		self.v=0.0
		self.p=[]
		self.setupUi(self)
		self.doubleSpinBox.valueChanged.connect(self.Chan)
		self.pushButton_2.clicked.connect(self.iniz)
		self.pushButton.clicked.connect(self.bd1)
		self.pushButton_3.clicked.connect(self.bd2)
	def bd1(self):
		print('zdes vasha funkzia')#prilepim potom vash kod
	def bd2(self):
		print('zdes vasha funkzia')#prilepim potom vash kod
	def Chan(self):
		self.v=(self.doubleSpinBox.value())
	def iniz(self):
		text = self.plainTextEdit.toPlainText()
		self.p = (list(map(float, text.split())))
		print (text)
		self.close()
		if(len(self.p)==0):
			self.g=bd()
			self.g.show()
			print('vy gde-to oshiblis')
		else:
			gmh(self.v,self.p)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('zac.png'))
	m1 = Window()
	m1.show()
	sys.exit(app.exec_())
	app = QtWidgets.QApplication(sys.argv)

