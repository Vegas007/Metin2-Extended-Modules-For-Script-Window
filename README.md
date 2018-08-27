# Metin2 Extended Modules For Script Window

def GetChildDictionary(self, *args):
	"""
	:param args: Is used to send a non-keyworded variable length argument list to the function.
	:how-to-call-ex:
		* I. childrenDict = self.GetChildDictionary('a1')
			# childrenDict['a1'].SetScale(scale)

		* II. childrenDict = self.GetChildDictionary('b1', 'b2')
			# childrenDict['b1'].SetSize(w, h)
			# childrenDict['b2'].SetPosition(x, y)

		* III. 
			for value in self.GetChildDictionary('c1', 'c2', 'c3', 'c4').values():
				value.SetSize(w, h)

		* IV. 
			def OnToggleDown(self, index):
				print 'OnToggleDown {:d}'.format(index)

			for key, value in enumerate(self.GetChildDictionary('d1', 'd2').values()):
				value.SAFE_SetEvent(self.OnToggleDown, key)
	"""

def SAFE_SetDictionaryEvent(self, childrenDict, eventNameFuncs):
	"""
	:param childrenDict: A dictionary with objects.
	:param eventNameFuncs: A list of events name as function which will be executed for each object.
	:how-to-call-ex:
		* I. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('a1', 'a2', 'a3'), ['Show', 'SetCenterPosition'])
		* II. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('b1'), ('Hide'))
		* III. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('c1'), ('SetWindowVerticalAlignCenter', 'SetTop', 'SetFocus', 'Lock'))
	"""
