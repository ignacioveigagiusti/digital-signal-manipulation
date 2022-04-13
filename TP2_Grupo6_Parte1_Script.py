# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:39:07 2020

@author: Ignacio
"""

from TP2_Grupo6_Parte1 import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_() 