

def main():
	# 创建两个表单，并分别填入对应的文件中
	htmlForm = create_login_form(HtmlForBuilder())
	with open(htmlFilename, "w", encoding="utf-8") as file:
		file.write(htmlForm)

	tkForm = create_login_form(TkFormBuilder())
	with open(tkFilename, "w", encoding="utf-8") as file:
		file.write(tkForm)