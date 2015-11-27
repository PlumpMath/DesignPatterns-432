
class DiagramFactory:

	@classmethod
	def make_diagram(Class, width, height):
		return Class.Diagram(width, height)

	@classmethod
	def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
		return Class.Rectangle(x, y, width, height, fill, stroke)

	@classmethod
	def make_text(Class, x, y, text, fontsize=12):
		return Class.Text(x, y, text, fontsize)