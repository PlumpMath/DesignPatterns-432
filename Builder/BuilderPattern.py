
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


    def add_button(self, text, row, column, **kwargs):
        html = """<td><input type="submit" value="{}" /></td>""".format(
                escape(text))
        self.items[(row, column)] = html


    def form(self):
        html = ["<!doctype html>\n<html><head><title>{}</title></head>"
                "<body>".format(self.title), '<form><table border="0">']
        thisRow = None
        for key, value in sorted(self.items.items()):
            row, column = key
            if thisRow is None:
                html.append("  <tr>")
            elif thisRow != row:
                html.append("  </tr>\n  <tr>")
            thisRow = row
            html.append("    " + value)
        html.append("  </tr>\n</table></form></body></html>")
        return "\n".join(html)

class TkFormBuilder(AbstractFormBuilder):
	TEMPLATE = """#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
class {name}Form(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.withdraw()     # hide until ready to show
        self.title("{title}")
        {statements}
        self.bind("<Escape>", lambda *args: self.destroy())
        self.deiconify()    # show when widgets are created and laid out
        if self.winfo_viewable():
            self.transient(master)
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)
if __name__ == "__main__":
    application = tk.Tk()
    window = {name}Form(application)
    application.protocol("WM_DELETE_WINDOW", application.quit)
    application.mainloop()
"""

	def __init__(self):
		self.title = "TkFormBuilder"
		self.statements = []

	def add_title(self, title):
		super.add_title(title)

	def add_label(self, text, row, column, **kwargs):
		name = self._canonicalize(text)
        create = """self.{}Label = ttk.Label(self, text="{}:")""".format(
                name, text)
        layout = """self.{}Label.grid(row={}, column={}, sticky=tk.W, \
padx="0.75m", pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

     def add_entry(self, variable, row, column, **kwargs):
        name = self._canonicalize(variable)
        extra = "" if kwargs.get("kind") != "password" else ', show="*"'
        create = "self.{}Entry = ttk.Entry(self{})".format(name, extra)
        layout = """self.{}Entry.grid(row={}, column={}, sticky=(\
tk.W, tk.E), padx="0.75m", pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

    def add_button(self, text, row, column, **kwargs):
        name = self._canonicalize(text)
        create = ("""self.{}Button = ttk.Button(self, text="{}")"""
                .format(name, text))
        layout = """self.{}Button.grid(row={}, column={}, padx="0.75m", \
pady="0.75m")""".format(name, row, column)
        self.statements.extend((create, layout))

    def _canonicalize(self, text, startLower=True):
        text = re.sub(r"\W+", "", text)
        if text[0].isdigit():
            return "_" + text
        return text if not startLower else text[0].lower() + text[1:]

    def form(self):
    	return TkFormBuilder.TEMPLATE.format(title=self.title,
                name=self._canonicalize(self.title, False),
                statements="\n        ".join(self.statements))

###
# Builder模式与Abstract Factory模式的区别在于，不仅提供了创建复杂对象所需的方法，
# 还保存了复杂对象里各个部分的细节
# 适用于需要把复杂对象各部分的细节与其创建流程相分离的场合

