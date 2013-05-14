import sublime
import sublime_plugin
import uuid


class GenerateUuidFourCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # paste the UUID at each selection point
        for cursors in self.view.sel():
            uuid4 = "uuid_" + str(uuid.uuid4())
            self.view.replace(edit, cursors, uuid4)

        # copy the last UUID to the clipboard
        sublime.set_clipboard(uuid4)

        # update the status message
        sublime.status_message("Generated UUID version 4")