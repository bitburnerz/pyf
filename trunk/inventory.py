'''Inventory container class.'''

"""This file is part of PyF.

PyF is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyF is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyF.  If not, see <http://www.gnu.org/licenses/>.
"""

class Inventory:
	def __init__(self, parent):
		self.parent = parent
		#: Item this inventory belongs to
		self.list = []
		#: list of items in inventory
		
	def __iter__(self):
		if self.parent.accessibleChildren():
			return iter(self.list)
		else:
			return iter(())
			
	def __getitem__(self, i):
		return self.list[i]
			
	def append(self, item):
		if not item.proxy:
			self.list.append(item)
		
	def remove(self, item):
		self.list.remove(item)