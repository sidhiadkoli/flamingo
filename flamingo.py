import sys
from PyQt4 import QtCore, QtGui
import editor_window
import ui_schoolEssay

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


class EditorMainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self) 

		self.ui = editor_window.Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.initUiElements()
		self.setupFileActions()
		self.setupEditActions()
		self.setupEditorProperties()
		self.setupToolActions()

	def initUiElements(self):
		pass

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
		
		self.actionSchoolEssay = QtGui.QAction("School Essay",
			self,
			triggered=self.createSchoolEssay)
		menu.addAction(self.actionSchoolEssay)
	
	def checkSave(self):
		if self.ui.editorTextEdit.document().isModified():
			return True
		
		shouldSave = QtGui.QMessageBox.warning(self, "Application",
				"Do you want to save the changes you " +
				"made to the document \"" + self.fileName +
				"\"?", 
				QtGui.QMesssageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)

	def fileNew(self):
		pass
		#if self.checkSave():

	def fileOpen(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self, 
		"Open File...", 
		"~",
		"Text-Files (*.txt);;All Files (*)")
		
		f = open(fileName)
		text = f.read()

		self.ui.editorTextEdit.setPlainText(text)
	
	def fileSave(self):
		pass

	def fileSaveAs(self):
		pass

	def createSchoolEssay(self):
		self.schoolEssay = SchoolDialog()
		self.schoolEssay.exec_()

		self.ui.editorTextEdit.setPlainText(self.schoolEssay.getCombinedText())

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = EditorMainWindow()
	window.show()
	sys.exit(app.exec_())
