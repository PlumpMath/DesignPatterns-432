


def main():
	# 省略了创建两个文件(textFilename、svgFilename)的操作

	# 用默认的纯文本工厂创建示意图
	txtDiagram = create_diagram(DiagramFactory())
	txtDiagram.save(textFilename)
	# 用SVG工厂来创建同样的示意图
	svgDiagram = create_diagram(SvgDiagramFactory())
	svgDiagram.save(svgFilename)