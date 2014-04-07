import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
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
		text = str(self.ui.titleTextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.introTextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point1TextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point2TextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point3TextEdit.toPlainText()).strip()
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
		self.readabilities = {"None": None,"Children":[0,7],"Adolescence":[7,12],"Undergraduate":[12, 16],"Graduate":[15,18],"PhD":[18,24]}
		
		self.fileName = ""
		self.evaluator = fn.Comments()		
		self.rc = fn.Readability()
		self.clickSet = False
		self.targetReadability = self.readabilities["None"]

		self.initUiElements()
		self.setupFileActions()
		self.setupEditActions()
		self.setupEditorProperties()
		self.setupToolActions()

	def initUiElements(self):
		self.ui.editorTextEdit.setFocus()
		self.setFileName("")
		self.clearAll()
		self.colour = [QtGui.QColor(204, 229, 255), QtGui.QColor(255, 204, 204)]

		self.ui.editorTextEdit.cursorPositionChanged.connect(self.updateCursorPosition)

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
			enabled=self.ui.editorTextEdit.document().isModified(),
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
			enabled=self.ui.editorTextEdit.document().isUndoAvailable(),
			triggered=self.ui.editorTextEdit.undo)
		menu.addAction(self.actionUndo)

		self.actionRedo = QtGui.QAction("Redo", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Redo,
			enabled=self.ui.editorTextEdit.document().isRedoAvailable(),
			triggered=self.ui.editorTextEdit.redo)
		menu.addAction(self.actionRedo)	

		menu.addSeparator()

		self.actionCut = QtGui.QAction("Cut", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Cut,
			enabled=False,
			triggered=self.ui.editorTextEdit.cut)
		menu.addAction(self.actionCut)

		self.actionCopy = QtGui.QAction("Copy", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Copy,
			enabled=False,
			triggered=self.ui.editorTextEdit.copy)
		menu.addAction(self.actionCopy)

		self.actionPaste = QtGui.QAction("Paste", self,
			priority=QtGui.QAction.LowPriority,
			shortcut=QtGui.QKeySequence.Paste,
			enabled=(len(QtGui.QApplication.clipboard().text()) != 0),
			triggered=self.ui.editorTextEdit.paste)
		menu.addAction(self.actionPaste)

	def setupEditorProperties(self):
		self.ui.editorTextEdit.document().modificationChanged.connect(self.actionSave.setEnabled)
		self.ui.editorTextEdit.document().modificationChanged.connect(self.setWindowModified)
		self.ui.editorTextEdit.document().undoAvailable.connect(self.actionUndo.setEnabled)
		self.ui.editorTextEdit.document().redoAvailable.connect(self.actionRedo.setEnabled)
		self.setWindowModified(self.ui.editorTextEdit.document().isModified())

		self.ui.editorTextEdit.copyAvailable.connect(self.actionCut.setEnabled)
		self.ui.editorTextEdit.copyAvailable.connect(self.actionCopy.setEnabled)

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
		#self.connect(ag, SIGNAL("triggered(QtGui.QAction *action)"), self.setReadability)	
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

	#@pyqtSlot(QtGui.QAction)
	def setReadability(self, currentAction):
		self.targetReadability = self.readabilities[str(currentAction.text())]

	def updateCursorPosition(self):
		line = self.ui.editorTextEdit.textCursor().blockNumber()
		col = self.ui.editorTextEdit.textCursor().columnNumber()
		status = ("Line: " + str(line) + ", " + "Column: "
				+ str(col))
		self.statusBar().showMessage(status)

	def checkSave(self):
		if not self.ui.editorTextEdit.document().isModified():
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
			text = f.read()
			f.close()
			self.clearAll()
			self.ui.editorTextEdit.setPlainText(text)
			self.setFileName(fname)
			return True

		return False
	
	def fileSave(self):
		if not self.fileName:
			return self.fileSaveAs()
		
		f = open(self.fileName, 'w')

		if not f:
			return False

		f.write(self.ui.editorTextEdit.toPlainText())
		f.close()
		
		self.ui.editorTextEdit.document().setModified(False)
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

		self.ui.editorTextEdit.setPlainText(self.schoolEssay.getCombinedText())
		self.ui.editorTextEdit.document().setModified(True)
		
	def createDebate(self):
		self.debate = DebateDialog()
		self.debate.exec_()

		self.ui.editorTextEdit.setPlainText(self.debate.getCombinedText())
		self.ui.editorTextEdit.document().setModified(True)
		
	def createFormalLetter(self):
		self.formalLetter = LetterDialog()
		self.formalLetter.exec_()
		
		self.ui.editorTextEdit.setPlainText(self.formalLetter.getCombinedText())
		self.ui.editorTextEdit.document().setModified(True)

	def setRead1(self):
		pass

	def evaluate(self):
		self.ui.commentsListWidget.clear()
		if str(self.ui.editorTextEdit.toPlainText()) == "":
			return 0
		
		self.comments = self.evaluator.getComments(str(self.ui.editorTextEdit.toPlainText()))

		for c in self.comments:
			self.ui.commentsListWidget.addItem(c[2])

		for i in range(self.ui.commentsListWidget.count()):
			self.ui.commentsListWidget.item(i).setBackground(self.colour[self.comments[i][1]])

		if not self.clickSet:
			self.ui.commentsListWidget.itemSelectionChanged.connect(self.itemSelectedSlot)
			#self.connect(self.ui.commentsListWidget, SIGNAL("itemSelectionChanged()"), self, SLOT("itemSelectedSlot()"))
			self.clickSet = True

	#@pyqtSlot()
	def itemSelectedSlot(self):
		item = self.ui.commentsListWidget.currentItem()
		row = self.ui.commentsListWidget.currentRow()
		com = self.comments[row][0]
		cu = self.ui.editorTextEdit.textCursor()
		pos = str(self.ui.editorTextEdit.toPlainText()).find(com)
		
		if pos != -1:
			cu.setPosition(pos)
			cu.setPosition(pos+len(com), QtGui.QTextCursor.KeepAnchor)
			self.ui.editorTextEdit.setTextCursor(cu)
		else:
			cu.setPosition(0)
			self.ui.editorTextEdit.setTextCursor(cu)	

	def getReadability(self):
		self.ui.readabilityTextEdit.clear()

		rd = self.rc.getReadability(str(self.ui.editorTextEdit.toPlainText()))

		for s in rd:
			self.ui.readabilityTextEdit.append(s[0] + ": " + str(s[1]))

	def clearAll(self):
		self.ui.editorTextEdit.clear()
		self.ui.readabilityTextEdit.clear()
		self.ui.commentsListWidget.clear()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = EditorMainWindow()
	window.show()
	sys.exit(app.exec_())
