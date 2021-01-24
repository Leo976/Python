






class A:

	def init_b(self):

		return 10

	def __init__(self, a):

		self.a = a
		self.b = init_b()

	

a = A(4)


print(a.a)
print(a.b)

input()