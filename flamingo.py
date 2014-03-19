import sys
from PyQt4 import QtCore, QtGui
import create_file
import editor_window
import school_essay

class MyMainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 
		
		self.ui = create_file.Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.initUiElements()

	def initUiElements(self):
		self.ui.themeComboBox.addItems(["None", 
						"School Essay",
						"Debate",
						"Formal Letter",
						"Policy Memo"])
		
		self.ui.readabilityComboBox.addItems(["None",
						"Children (< 13)",
						"Adolescence (13-18)",
						"Undergraduate",
						"Post Graduate",
						"PhD"])

		self.ui.browsePushButton.clicked.connect(self.selectFile)
		self.ui.openPushButton.clicked.connect(self.openFile)
		self.ui.createPushButton.clicked.connect(self.createFile)
		self.ui.cancelPushButton.clicked.connect(self.reject)

	def selectFile(self):
		self.ui.pathTextEdit.setPlainText(QtGui.QFileDialog.getOpenFileName())
	
	def openFile(self):
		path = self.ui.pathTextEdit.toPlainText()
		
		if path[-4:] != '.txt':
			self.ui.pathTextEdit.setPlainText("Please use .txt!")

	def createFile(self):
		params = []

		params.append(self.ui.nameTextEdit.toPlainText())
		params.append(self.ui.themeComboBox.currentText())
		params.append(self.ui.readabilityComboBox.currentText())
		
		theme = self.ui.themeComboBox.currentText()
		
		self.close()

		if theme == 'School Essay':
			self.window = SchoolMainWindow(params)
		else :
			self.window = EditorMainWindow(params)

		self.window.show()

	def reject(self):
		sys.exit()


class SchoolMainWindow(QtGui.QMainWindow):
	def __init__(self, params):
		QtGui.QMainWindow.__init__(self) 
		self.params = params		
		self.ui = school_essay.Ui_MainWindow()
		self.ui.setupUi(self)

		self.initUiElements()

	def initUiElements(self):
		self.ui.proceedPushButton.clicked.connect(self.nextWindow)

	def combinedText(self):
		text = str(self.ui.introTextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point1TextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point2TextEdit.toPlainText()).strip()
		text += "\n\n"
		text += str(self.ui.point3TextEdit.toPlainText()).strip()
		text += "\n\nType conclusion here."

		return text

	def nextWindow(self):
		self.params.append(self.combinedText())
		
		self.close()
		self.window = EditorMainWindow(self.params)
		self.window.show()


class EditorMainWindow(QtGui.QMainWindow):
	def __init__(self, params):
		QtGui.QMainWindow.__init__(self) 
		self.params = params
		self.ui = editor_window.Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.initUiElements()
		self.setupFileActions()
		self.setupEditActions()
		self.setupEditorProperties()
		self.setupToolActions()

	def initUiElements(self):
		if len(self.params) > 3 :
			self.ui.editorTextEdit.setPlainText(self.params[3])

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
			triggered=self.fileNew)
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
		pass	

	def fileNew(self):
		pass
	
	def fileSave(self):
		pass

	def fileSaveAs(self):
		pass

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyMainWindow()
	window.show()
	sys.exit(app.exec_())
