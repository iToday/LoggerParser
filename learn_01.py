import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextBrowser
from PyQt5 import QtCore

from ClassDemo import ClassDemo

if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = QWidget()
    
    q.textBrowser = QTextBrowser(q)
    q.textBrowser.setGeometry(QtCore.QRect(20, 100, 351, 191))
    q.textBrowser.setObjectName("textBrowser")
    cls = ClassDemo("fuck")

    q.textBrowser.setText(cls.name)
    
    q.show()
    sys.exit(app.exec_())

    
