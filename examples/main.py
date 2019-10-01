import ui, exception, dbg

class MainWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
	
	def __LoadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "uiScript/main_window.py")
		except:
			exception.Abort("MainWindow.__LoadWindow.LoadWindow")
			
		try:
			self.childrenDict = self.GetChildDictionary("HideButton", "ShowButton", "UpdateButton")
		except:
			import exception
			exception.Abort('MainWindow.__LoadWindow.BindObject')
		
		for tabKey, tabButton in enumerate(self.childrenDict.values()):
			tabButton.SAFE_SetEvent(self.__OnToggleDown, tabKey)

	def __OnToggleDown(self, index):
		dbg.LogBox('__OnToggleDown {:d}'.format(index))
		
		if index == 0: # HideButton
			self.SAFE_SetDictionaryEvent﻿(self.childrenDict, ('Hide'))
		elif index == 1: # ShowButton
			self.SAFE_SetDictionaryEvent﻿(self.childrenDict, ('Show'))
		elif index == 2: # UpdateButton
			self.SAFE_SetDictionaryEvent﻿(self.childrenDict, ('UpdateRect', 'SetTop', 'SetCenterPosition', 'Lock'))