
class MenuEntry:
    def __init__(self, label="DEFAULT_LABEL"):
        self.label = label
        self.show = True

    def onSelected(self):
        pass

    def getLabel(self):
        return self.label

    def setHidden(self):
        self.show = False

    def setVisible(self):
        self.show = True

    def isVisible(self):
        return self.show
