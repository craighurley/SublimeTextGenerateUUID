import sublime
import sublime_plugin
import uuid


class GenerateUuidFourCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # create and copy the UUID into the paste buffer
        uuid4 = "uuid_" + str(uuid.uuid4())
        sublime.set_clipboard(uuid4)

        # paste the UUID at each selection point
        for cursors in self.view.sel():
            self.view.replace(edit, cursors, uuid4)

        # update the status message
        sublime.status_message("Generated UUID version 4")
