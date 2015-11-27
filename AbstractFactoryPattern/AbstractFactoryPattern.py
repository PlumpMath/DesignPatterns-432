





def create_diagram(factory):
	# create_diagram无需关心参数factory具体是什么
	# 只要知道factoryj具有所需的接口（make_diagram，make_rectangle，make_text）
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