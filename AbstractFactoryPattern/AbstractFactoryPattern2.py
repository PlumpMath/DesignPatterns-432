
class DiagramFactory:
	# 类方法：当调用这些方法时，首个参数是类
	# 当调用DiagramFactory.make_text()方法时，Class参数就是DiagramFactory

	@classmethod
	def make_diagram(Class, width, height):
		return Class.Diagram(width, height)

	@classmethod
	def make_rectangle(Class, x, y, width, height, fill="white", stroke="black"):
		return Class.Rectangle(x, y, width, height, fill, stroke)

	@classmethod
	def make_text(Class, x, y, text, fontsize=12):
		return Class.Text(x, y, text, fontsize)

class SvgDiagramFactory(DiagramFactory):
	# SvgDiagramFactory只需继承DiagramFactory，而不用再去实现（make_diagram，make_rectangle，make_text）方法
	# 比如：调用SvgDiagramFactory.make_rectangle()方法时，由于SvgDiagramFactory类并没有实现这个方法，就会执行
	# 基类的DiagramFactory.make_rectangle()。执行的时候，Class参数的值是SvgDiagramFactory
	SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
	           font-famaily="sans-serif" font-size="{fontsize}">{text}</text>"""
	SVG_SCALE = 20

	class Text:
		def __init__(self, x, y, text, fontsize):
			x += SvgDiagramFactory.SVG_SCALE
			y += SvgDiagramFactory.SVG_SCALE
			fontsize += SvgDiagramFactory.SVG_SCALE // 10
			self.svg = SvgDiagramFactory.SVG_TEXT.format(**locals())