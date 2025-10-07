class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_text):
        self.undo_stack.append(self.text)
        self.text += ("" if not self.text else " ") + new_text
        self.redo_stack.clear()
        print("✅ Change added.\n")

    def undo(self):
        if not self.undo_stack:
            print("⚠️ Nothing to undo.\n")
            return
        self.redo_stack.append(self.text)
        self.text = self.u
