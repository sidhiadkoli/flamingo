import sys
from PyQt4 import QtCore, QtGui
import editor_window
import ui_schoolEssay
import ui_formalLetter
import ui_debate
import fn

class SchoolDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self) 		
		self.ui = ui_schoolEssay.Ui_Dialog()
		self.ui.setupUi(self)

		self.initUiElements()

	def initUiElements(self):
		pass

	def getCombinedText(self):
		text = ""
		texttemp = str(self.ui.titleTextEdit.toPlainText()).strip()
		text = "Title :: "
		if(texttemp ==""):
			texttemp = "Type the Title  here"
		text += texttemp
		
		texttemp = str(self.ui.introTextEdit.toPlainText()).strip()
		if(texttemp ==""):
			texttemp = "Type Introduction here"
		text += "\n\n"+texttemp
		
		texttemp = str(self.ui.point1TextEdit.toPlainText()).strip()
		if(texttemp ==""):
			texttemp = "Type point considered for 1st Paragraph here"
		text += "\n\n"+texttemp
		text += "Expand here"
		
		texttemp = str(self.ui.point2TextEdit.toPlainText()).strip()
		if(texttemp ==""):
			texttemp = "Type point considered for 2nd Paragraph here"
		text += "\n\n"+texttemp
		text += "Expand here"
		
		texttemp = str(self.ui.point3TextEdit.toPlainText()).strip()
		if(texttemp ==""):
			texttemp = "Type point considered for 3rd Paragraph here"
		text += "\n\n"+texttemp
		text += "Expand here"
		
		text += "\n\nType conclusion here."

		return text

class LetterDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self) 		
		self.ui = ui_formalLetter.Ui_Dialog()
		self.ui.setupUi(self)

		self.initUiElements()

	def initUiElements(self):
		pass

	def getCombinedText(self):
		
		#sender's address
		text = ""
		texttemp = str(self.ui.sendAddr1LineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter Sender's Address here"
		text += texttemp
		texttemp = str(self.ui.sendAddr2LineEdit.text()).strip()
		text += "\n" + texttemp
		texttemp = str(self.ui.sendAddr3LineEdit.text()).strip()
		text += "\n"+ texttemp
		text += "\n\n"
		
		#recv name
		texttemp = str(self.ui.recvNameLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter Receiver's name here"
		text += texttemp
		text += "\n"
		
		#recv address
		texttemp = str(self.ui.recvAddr1LineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter Receiver's Address here"
		text += texttemp
		texttemp = str(self.ui.recvAddr2LineEdit.text()).strip()
		text += "\n" + texttemp
		texttemp = str(self.ui.recvAddr3LineEdit.text()).strip()
		text += "\n"+ texttemp
		text += "\n\n"
		
		#date
		texttemp = str(self.ui.dateLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter Date here"
		text += texttemp
		text += "\n\n"
		
		#subject
		text += "Subject : "
		texttemp = str(self.ui.subjectLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter subject here"
		text += texttemp
		text += "\n\n"
		
		#salutation
		texttemp = str(self.ui.salutationLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter salutation here"
		text += texttemp
		text += "\n\n"
		
		#content
		text += "\n\n"
		
		#regards
		texttemp = str(self.ui.regardsLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter regards here"
		text += texttemp
		text += "\n\n"
		
		#sender's name
		texttemp = str(self.ui.sendNameLineEdit.text()).strip()
		if(texttemp == ""):
			texttemp = "Enter sender's name here"
		text += texttemp
		text += "\n\n"
		
		return text
		

class DebateDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self) 		
		self.ui = ui_debate.Ui_Dialog()
		self.ui.setupUi(self)

		self.initUiElements()

	def initUiElements(self):
		pass

	def getCombinedText(self):
	
		text = ""
		temptext = str(self.ui.introTextEdit.toPlainText()).strip()
		if(temptext == ""):
			temptext = "Type Introduction here"
		text += temptext	
		text += "\n\n"
		temptext = str(self.ui.arg1TextEdit.toPlainText()).strip()
		if(temptext != ""):
			text += temptext
			text += "\n\n"
		temptext = str(self.ui.arg2TextEdit.toPlainText()).strip()
		if(temptext != ""):
			text += temptext
			text += "\n\n"
		temptext = str(self.ui.arg3TextEdit.toPlainText()).strip()
		if(temptext != ""):
			text += temptext
			text += "\n\n"
		text += "Type conclusion here."

		return text

class EditorMainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 

		self.ui = editor_window.Ui_MainWindow()
		self.ui.setupUi(self)
		self.readabilities = {"None": None,"Children (<=12)":[0,7],"Adolescence":[7,12],"Undergraduate":[12, 16],"Graduate":[15,18],"PhD":[18,24]}
		
		self.fileName = ""
		self.evaluator = fn.Comments()		
		self.rc = fn.Readability()
		self.clickSet = False
		self.targetReadability = self.readabilities["None"]
		self.textEdit = self.ui.editorTextEdit

		self.initUiElements()
		self.setupFileActions()
		self.setupEditActions()
		self.setupEditorProperties()
		self.setupToolActions()

	def initUiElements(self):
		self.textEdit.setFocus()
		self.setFileName("")
		self.clearAll()
		self.colour = [QtGui.QColor(204, 229, 255), QtGui.QColor(255, 204, 204), QtGui.QColor(255, 255, 255)]

		self.textEdit.cursorPositionChanged.connect(self.updateCursorPosition)

	def setupFileActions(self):
		menu = self.ui.menuFile
		
		self.actionNew = QtGui.QAction("New", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.New,
			triggered=self.fileNew)
		menu.addAction(self.actionNew)

		self.actionOpen = QtGui.QAction("Open...", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Open,
			triggered=self.fileOpen)
		menu.addAction(self.actionOpen)
	
		menu.addSeparator()

		self.actionSave = QtGui.QAction("Save", self,
			shortcut=QtGui.QKeySequence.Save,
			enabled=self.textEdit.document().isModified(),
			triggered=self.fileSave)
		menu.addAction(self.actionSave)

		self.actionSaveAs = QtGui.QAction("Save As...", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_S,
			triggered=self.fileSaveAs)
		menu.addAction(self.actionSaveAs)
	
	def setupEditActions(self):
		menu = self.ui.menuEdit

		self.actionUndo = QtGui.QAction("Undo", self,
			shortcut=QtGui.QKeySequence.Undo,
			enabled=self.textEdit.document().isUndoAvailable(),
			triggered=self.textEdit.undo)
		menu.addAction(self.actionUndo)

		self.actionRedo = QtGui.QAction("Redo", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Redo,
			enabled=self.textEdit.document().isRedoAvailable(),
			triggered=self.textEdit.redo)
		menu.addAction(self.actionRedo)	

		menu.addSeparator()

		self.actionCut = QtGui.QAction("Cut", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Cut,
			enabled=False,
			triggered=self.textEdit.cut)
		menu.addAction(self.actionCut)

		self.actionCopy = QtGui.QAction("Copy", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Copy,
			enabled=False,
			triggered=self.textEdit.copy)
		menu.addAction(self.actionCopy)

		self.actionPaste = QtGui.QAction("Paste", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Paste,
			enabled=(len(QtGui.QApplication.clipboard().text()) != 0),
			triggered=self.textEdit.paste)
		menu.addAction(self.actionPaste)

	def setupEditorProperties(self):
		self.textEdit.document().modificationChanged.connect(self.actionSave.setEnabled)
		self.textEdit.document().modificationChanged.connect(self.setWindowModified)
		self.textEdit.document().undoAvailable.connect(self.actionUndo.setEnabled)
		self.textEdit.document().redoAvailable.connect(self.actionRedo.setEnabled)
		self.setWindowModified(self.textEdit.document().isModified())

		self.textEdit.copyAvailable.connect(self.actionCut.setEnabled)
		self.textEdit.copyAvailable.connect(self.actionCopy.setEnabled)

		#QtGui.QApplication.clipboard().dataChanged.connect(
                #	self.clipboardDataChanged)

	def setupToolActions(self):
		menu = self.ui.menuTools
		
		themes = QtGui.QMenu("Choose Theme", self)
		menu.addMenu(themes)
		
		self.actionSchoolEssay = QtGui.QAction("School Essay",
			self,
			triggered=self.createSchoolEssay)
		themes.addAction(self.actionSchoolEssay)
		
		self.actionFormalLetter = QtGui.QAction("Formal Letter",
			self,
			triggered=self.createFormalLetter)
		themes.addAction(self.actionFormalLetter)

		self.actionDebate = QtGui.QAction("Debate",
			self,
			triggered=self.createDebate)
		themes.addAction(self.actionDebate)

		readability = QtGui.QMenu("Set Readability", self)
		menu.addMenu(readability)
		
		ag = QtGui.QActionGroup(self, exclusive=True)

		self.actionRead0 = QtGui.QAction("None",
			self,
			checkable=True,
			checked=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead0))
		
		self.actionRead1 = QtGui.QAction("Children (<=12)",
			self,			
			checkable=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead1))

		self.actionRead2 = QtGui.QAction("Adolescence",
			self,			
			checkable=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead2))

		self.actionRead3 = QtGui.QAction("Undergraduate",
			self,			
			checkable=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead3))

		self.actionRead4 = QtGui.QAction("Graduate",
			self,			
			checkable=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead4))

		self.actionRead5 = QtGui.QAction("PhD",
			self,			
			checkable=True,
			triggered=self.setRead1)
		readability.addAction(ag.addAction(self.actionRead5))
		
		ag.triggered.connect(self.setReadability)	
		menu.addSeparator()

		self.actionEvaluate = QtGui.QAction("Evaluate document",
			self,
			shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_E,
			triggered=self.evaluate)
		menu.addAction(self.actionEvaluate)

		self.actionReadability = QtGui.QAction("Calculate readability scores",
			self,
			shortcut=QtCore.Qt.CTRL + QtCore.Qt.Key_G,
			triggered=self.getReadability)
		menu.addAction(self.actionReadability)

		menu.addSeparator()

		self.actionAutoRead = QtGui.QAction("Auto evaluate readability",
			self,
			checkable=True,
			triggered=self.autoRead)
		menu.addAction(self.actionAutoRead) 

	def setReadability(self, currentAction):
		self.targetReadability = self.readabilities[str(currentAction.text())]

	def updateCursorPosition(self):
		line = self.textEdit.textCursor().blockNumber() + 1
		col = self.textEdit.textCursor().columnNumber()
		status = ("Line: " + str(line) + ", " + "Column: "
				+ str(col))
		self.statusBar().showMessage(status)

	def checkSave(self):
		if not self.textEdit.document().isModified():
			return True
		
		shouldSave = QtGui.QMessageBox.warning(self, "Application",
				"Do you want to save the changes you " +
				"made to the document \"" +
				self.windowTitle() +
				"\"?", 
				QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)

		if shouldSave == QtGui.QMessageBox.Save:
			return self.fileSave()

		elif shouldSave == QtGui.QMessageBox.Cancel:
			return False

		return True

	def fileNew(self):
		if self.checkSave():
			self.clearAll()
			self.setFileName("")

	def fileOpen(self):
		if not self.checkSave():
			return False
		
		fname = QtGui.QFileDialog.getOpenFileName(self, 
		"Open File...", 
		"~",
		"Text-Files (*.txt);;All Files (*)")
		
		if fname:
			f = open(fname, 'r')
			textData = f.read()
			f.close()
			self.clearAll()
			self.textEdit.setPlainText(textData)
			self.setFileName(fname)
			return True

		return False
	
	def fileSave(self):
		if not self.fileName:
			return self.fileSaveAs()
		
		f = open(self.fileName, 'w')

		if not f:
			return False

		f.write(self.textEdit.toPlainText())
		f.close()
		
		self.textEdit.document().setModified(False)
		return True

	def fileSaveAs(self):
		fname = QtGui.QFileDialog.getSaveFileName(self, 
			"Save as...", "~", 
			"Text-Files (*.txt);;All Files (*)")

		if not fname:
			return False

		if not str(fname).endswith('.txt'):
			fname += ".txt"

		self.setFileName(fname)
		return self.fileSave()

	
	def closeEvent(self, event):
		if self.checkSave():
			event.accept()
		else:
			event.ignore()

	def setFileName(self, name):
		self.fileName = name
		if self.fileName == "":
			self.setWindowTitle("untitled")
		else:
			self.setWindowTitle(QtCore.QFileInfo(self.fileName).fileName())

	def createSchoolEssay(self):
		self.schoolEssay = SchoolDialog()
		self.schoolEssay.exec_()

		self.textEdit.setPlainText(self.schoolEssay.getCombinedText())
		self.textEdit.document().setModified(True)
		
	def createDebate(self):
		self.debate = DebateDialog()
		self.debate.exec_()

		self.textEdit.setPlainText(self.debate.getCombinedText())
		self.textEdit.document().setModified(True)
		
	def createFormalLetter(self):
		self.formalLetter = LetterDialog()
		self.formalLetter.exec_()
		
		self.textEdit.setPlainText(self.formalLetter.getCombinedText())
		self.textEdit.document().setModified(True)

	def setRead1(self):
		pass

	def evaluate(self):
		self.ui.commentsListWidget.clear()
		if str(self.textEdit.toPlainText()) == "":
			return 0
		
		self.comments = self.evaluator.getComments(str(self.textEdit.toPlainText()))

		for c in self.comments:
			self.ui.commentsListWidget.addItem(c[2])

		for i in range(self.ui.commentsListWidget.count()):
			self.ui.commentsListWidget.item(i).setBackground(self.colour[self.comments[i][1]])

		if not self.clickSet:
			self.ui.commentsListWidget.itemSelectionChanged.connect(self.itemSelectedSlot)
			self.clickSet = True

	def itemSelectedSlot(self):
		item = self.ui.commentsListWidget.currentItem()
		row = self.ui.commentsListWidget.currentRow()
		com = self.comments[row][0]
		cu = self.textEdit.textCursor()
		pos = str(self.textEdit.toPlainText()).find(com)
		
		if pos != -1:
			cu.setPosition(pos)
			cu.setPosition(pos+len(com), QtGui.QTextCursor.KeepAnchor)
			self.textEdit.setTextCursor(cu)
		else:
			cu.setPosition(0)
			self.textEdit.setTextCursor(cu)	

	def getReadability(self):
		self.ui.readabilityTextEdit.clear()

		rd = self.rc.getReadability(str(self.textEdit.toPlainText()))

		if not rd:
			return False

		for s in rd:
			self.ui.readabilityTextEdit.append(s[0] + ": " + str(s[1]))

		self.ui.readabilityTextEdit.append("\n")

		data = self.rc.getResultData()
		for r in data:
			self.ui.readabilityTextEdit.append(r[0] + ": " + str(r[1]))


		avg = float(rd[len(rd) - 1][1])
		if self.targetReadability and (avg > self.targetReadability[1] or avg < self.targetReadability[0]):
			self.ui.readabilityTextEdit.setTextBackgroundColor(self.colour[1])
		else :
			self.ui.readabilityTextEdit.setTextBackgroundColor(self.colour[2])


		return True

	def autoRead(self):
		if self.actionAutoRead.isChecked() == True:
			self.actionReadability.setDisabled(True) 
			self.textEdit.textChanged.connect(self.getReadability)
		else:
			self.actionReadability.setDisabled(False)
			self.textEdit.textChanged.disconnect()

	def clearAll(self):
		self.textEdit.clear()
		self.ui.readabilityTextEdit.clear()
		self.ui.commentsListWidget.clear()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = EditorMainWindow()
	window.show()
	sys.exit(app.exec_())
