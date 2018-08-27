#1.1 Search for:
	def GetChild2(self, name):
		return self.ElementDictionary.get(name, None)
#1.1 Add after:
	def GetChildDictionary(self, *args):
		"""
		:param args: Is used to send a non-keyworded variable length argument list to the function.
		:how-to-call-ex:
			* I. childrenDict = self.GetChildDictionary('a1')
				# childrenDict['b1'].SetScale(scale)

			* II. childrenDict = self.GetChildDictionary('b1', 'b2')
				# childrenDict['b2'].SetSize(w, h)
				# childrenDict['b3'].SetPosition(x, y)

			* III. 
				for value in self.GetChildDictionary('c1', 'c2', 'c3', 'c4').values():
					value.SetSize(w, h)

			* IV. 
				def OnToggleDown(self, index):
					print 'OnToggleDown {:d}'.format(index)

				for key, value in enumerate(self.GetChildDictionary('d1', 'd2').values()):
					value.SAFE_SetEvent(self.OnToggleDown, key)
					
					SetEvent(ui.__mem_func__(self.StartGame))

		"""
		if isinstance(args, tuple):
			return {children : self.ElementDictionary.get(children, None) for children in args}

		return dict()

	def SAFE_SetDictionaryEvent(self, childrenDict, eventNameFuncs):
		"""
		:param childrenDict: A dictionary with objects.
		:param eventNameFuncs: A list of events name as function which will be executed for each object.
		:how-to-call-ex:
			* I. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('a1', 'a2', 'a3'), ['Show', 'SetCenterPosition'])
			* II. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('b1'), ('Hide'))
			* III. 	self.SAFE_SetDictionaryEvent(self.GetChildDictionary('c1'), ('SetWindowVerticalAlignCenter', 'SetTop', 'SetFocus', 'Lock'))
		"""
		def Abort(*args):
			import dbg, exception
			dbg.TraceError("\n".join(args))
			exception.Abort('SAFE_SetDictionaryEvent')
	
		if isinstance(eventNameFuncs, str):
			eventNameFuncs = tuple(eventNameFuncs.split())

		allowedWindowEventsTuple = \
		(
			'SetWindowHorizontalAlignLeft',     'SetWindowHorizontalAlignCenter',
			'SetWindowHorizontalAlignRight',    'SetWindowVerticalAlignTop',
			'SetWindowVerticalAlignCenter',     'SetWindowVerticalAlignBottom',
			'SetPickAlways',                    'SetTop',
			'SetCenterPosition',                'SetFocus',
			'UpdateRect',                       'KillFocus',
			'Show',                             'Hide',
			'Lock',                             'Unlock'
		)

		if not isinstance(childrenDict, dict):
			Abort('Wrong type of argument childrenDict({:s}), must be as dictionary.'.format(type(childrenDict).__name__))

		if not isinstance(eventNameFuncs, (tuple, list)):
			Abort('Wrong type of argument eventNameFuncs({:s}), must be as list or tuple.'.format(type(eventNameFuncs).__name__))
			
		unallowedWindowEvents = (', '.join(event for event in eventNameFuncs if event not in allowedWindowEventsTuple))
		if unallowedWindowEvents:
			Abort('Unallowed eventNameFuncs ({:s}).'.format(unallowedWindowEvents))

		for key, value in childrenDict.iteritems():
			for event in eventNameFuncs:
				try:
					# Smth: eval('childrenDict.get("{:s}").{:s}()'.format(key, event))
					######################################################################
					# Return the value of the named attribute of object. name must be a string.
					# If the string is the name of one of the object’s attributes, the result is the value of that attribute. 
					# For example, getattr(x, 'foobar') is equivalent to x.foobar. 
					# If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
					getattr(value, event)()

				except AttributeError:
					Abort("Can't get attribute.")