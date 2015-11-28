
import abc
import os
import sys

def main():
	# 创建两个表单，并分别填入对应的文件中
	htmlForm = create_login_form(HtmlForBuilder())
	with open(htmlFilename, "w", encoding="utf-8") as file:
		file.write(htmlForm)

	tkForm = create_login_form(TkFormBuilder())
	with open(tkFilename, "w", encoding="utf-8") as file:
		file.write(tkForm)

def create_login_form(builder):
    builder.add_title("Login")
    builder.add_label("Username", 0, 0, target="username")
    builder.add_entry("username", 0, 1)
    builder.add_label("Password", 1, 0, target="password")
    builder.add_entry("password", 1, 1, kind="password")
    builder.add_button("Login", 2, 0)
    builder.add_button("Cancel", 2, 1)
    return builder.form()

class AbstractFormBuilder(metaclass=abc.ABCMeta):
	# metaclass为abc.ABCMeta，则该类无法初始化，只能作为抽象基类使用
	# 继承自AbstractFormBuilder的类必须实现所有抽象方法
    @abc.abstractmethod
    def add_title(self, title):
        self.title = title


    @abc.abstractmethod
    def form(self):
        pass


    @abc.abstractmethod
    def add_label(self, text, row, column, **kwargs):
        pass


    @abc.abstractmethod
    def add_entry(self, variable, row, column, **kwargs):
        pass


    @abc.abstractmethod
    def add_button(self, text, row, column, **kwargs):
        pass

class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        self.title = "HtmlFormBuilder"
        self.items = {}


    def add_title(self, title):
        super().add_title(escape(title))


    def add_label(self, text, row, column, **kwargs):
        self.items[(row, column)] = ('<td><label for="{}">{}:</label></td>'
                .format(kwargs["target"], escape(text)))


    def add_entry(self, variable, row, column, **kwargs):
        html = """<td><input name="{}" type="{}" /></td>""".format(
                variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html


    