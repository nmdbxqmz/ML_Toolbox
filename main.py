# -*- coding: utf-8 -*-
# @Time    : 2024/3/19 10:46
# @Author  : licheng
# @File    : main.py
import sys
from test import Ui_widget
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Ui_widget()
    Window.show()
    sys.exit(app.exec())