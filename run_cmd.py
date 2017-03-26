import os
import sublime, sublime_plugin

class run_cmd(sublime_plugin.TextCommand):
	def run(self, edit, cmd):
		output = os.popen(cmd).read()
		self.view.insert(edit, self.view.sel()[0].begin(), output)