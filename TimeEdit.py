from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt


class TimeEdit(QLineEdit):

    def __init__(self, parent=None):
        super(TimeEdit, self).__init__(parent)

        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setReadOnly(True)