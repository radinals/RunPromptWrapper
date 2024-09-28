from .MenuEntry import MenuEntry

import subprocess


class RunPromptWrapper:
    def __init__(self,  run_prompt_cmd):
        self.run_prompt_cmd = run_prompt_cmd
        self.menu_entries = []

    # generate menu entry label string
    def _generateExecStr(self):
        exec_string = ""
        for entry in self.menu_entries:
            if (entry.isVisible()):
                exec_string += (f"{entry.getLabel()}\n")

        return exec_string

    # add a menu entry
    def addMenuEntry(self, menu_entry: MenuEntry, append=False):
        if (append):
            self.menu_entries.append(menu_entry)
        else:
            self.menu_entries.insert(0, menu_entry)

    # execute the run prompt command
    def _execMenuCmd(self):
        return subprocess.run(self.run_prompt_cmd,
                              input=self._generateExecStr(),
                              text=True,
                              shell=True,
                              capture_output=True)

    # iteratively search for the label in the entries
    def _getMenuEntry(self, label: str):
        for entry in self.menu_entries:
            if (entry.getLabel() == label):
                return entry
        return None

    # on exit event
    def _captureEvent(self, exit_string):
        if (exit_string):
            menu_entry = self._getMenuEntry(
                str(exit_string.stdout).strip("\n"))
            if (menu_entry != None):
                self.onMenuEntrySelected(menu_entry)

    # on menu entry selection
    def onMenuEntrySelected(self, menu_entry: MenuEntry):
        menu_entry.onSelected()

    # start the run prompt, and capture output
    def start(self):
        self._captureEvent(self._execMenuCmd())
