


class Text:
	def __init__(self, x, y, text, fontsize):
		self.x = x
		self.y = y
		self.rows = [list(text)]

class Diagram:
	def add(self, component):
		for y, row in enumerate(component.rows):
			for x, char in enumerate(row):
				self.diagram[y + component.y][x + component.x] = char

SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
           font-famaily="sans-serif" font-size="{fontsize}">{text}</text>"""
SVG_SCALE = 20

class SvgText:
	def __init__(self, x, y, text, fontsize):
		x += SVG_TEXT
		y += SVG_SCALE
		fontsize += SVG_SCALE // 10
		self.svg = SVG_TEXT.format(**locals())

class SvgDiagram:
	def add(self, component):
		self.diagram.append(component.svg)

class DiagramFactory:
	# 工厂类：需提供一样的接口
	def make_diagram(self, width, height):
		return Diagram(width, height)

	def make_rectangle(self, x, y, width, height, fill = "white", stroke = "black"):
		return Rectangle(x, y, width, height, fill, stroke)

	def make_text(self, x, y, text, fontsize = 12):
		return Text(x, y, text, fontsize)

class SvgDiagramFactory:
	def make_diagram(slef, width, height):
		return SvgDiagram(width, height)

	def make_rectangle(self, x, y, width, height, fill = "white", stroke = "black"):
		return SvgRectangle(x, y, width, height, fill, stroke)

	def make_text(self, x, y, text, fontsize = 12):
		return SvgText(x, y, text, fontsize)

def create_diagram(factory):
	# create_diagram无需关心参数factory具体是什么
	# 只要知道factory具有所需的接口（make_diagram，make_rectangle，make_text）
	# 同时，diagram也需要具有一样的接口：add()
	diagram = factory.make_diagram(30, 7);
	rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
	text = factory.make_text(7, 3, "Abstract Factory")
	diagram.add(rectangle)
	diagram.add(text)
	return diagram


def main():
	# 省略了创建两个文件(textFilename、svgFilename)的操作

	# 用默认的纯文本工厂创建示意图
	txtDiagram = create_diagram(DiagramFactory())
	txtDiagram.save(textFilename)
	# 用SVG工厂来创建同样的示意图
	svgDiagram = create_diagram(SvgDiagramFactory())
	svgDiagram.save(svgFilename)