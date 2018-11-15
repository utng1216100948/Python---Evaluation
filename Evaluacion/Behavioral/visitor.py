# visitor.py

class House(object):
	def accept(self, visitor):
		"""Interface to accept a visitor"""
		visitor.visit(self)

	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist)

	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician) 

	def __str__(self):
		"""Simply return the class name when the House object is printed"""
		return self.__class__.__name__


class Visitor(object):
	"""Abstract visitor"""
	def __str__(self):
		"""Simply return the class name when the Visitor object is printed"""
		return self.__class__.__name__


class HvacSpecialist(Visitor): 
	"""Concrete visitor: HVAC specialist"""
	def visit(self, house):
		house.work_on_hvac(self) 


class Electrician(Visitor): 
	"""Concrete visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self) 

#Create an HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()
#Create a house
home = House()
#Let the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)
#Let the house accept the electrician and work on the house by invoking the visit() method
home.accept(e)

