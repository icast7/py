
class Parent(object):
	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print "-"*50

class Other(object):
	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child1(object):

	def __init__(self):
		self.other =  Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD1 override()"

	def altered(self):
		print "CHILD1, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD1, AFTER OTHER altered()"

son = Child1()

son.implicit()
son.override()
son.altered()