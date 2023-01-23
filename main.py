import sys, os

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Widgets(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("bmoOS")
        self.widget = QWidget(self)
        
        # Widget para el navegador
        self.webview = QWebEngineView()
        loadingUrl = ("file:" + os.path.dirname(os.path.realpath(__file__)) + "/index.html").replace('\\', '/')

        self.webview.setUrl(QUrl(loadingUrl))
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.webview)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.resize(320, 240)
        self.setWindowFlags(Qt.FramelessWindowHint)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    sys.exit(app.exec())