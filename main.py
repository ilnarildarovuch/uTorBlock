from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
# import os
import sys
# import subprocess

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        proxy = QNetworkProxy(QNetworkProxy.Socks5Proxy, '127.0.0.1', 9050)
        QNetworkProxy.setApplicationProxy(proxy)

        self.browser.setUrl(QUrl("https://youtube.com"))

        self.setCentralWidget(self.browser)
        self.setWindowTitle("Youtube (uTorBlock)")
        self.resize(1160, 840)
        self.show()

    def fulsc(self, request):
        self.showFullScreen()
        self.browser.page().fullScreenRequested.disconnect()
        self.browser.page().fullScreenRequested.connect(self.exit_fullscreen)
        return request.accept()

    def exit_fullscreen(self, request):
        self.showNormal()
        self.browser.page().fullScreenRequested.disconnect()
        self.browser.page().fullScreenRequested.connect(self.fulsc)
        return request.accept()

if __name__ == "__main__":
    # os.chdir("TorBrowser/Tor") # bad idea, TODO: change that
    # subprocess.Popen("tor.exe")
    app = QApplication(sys.argv)
    app.setApplicationName("uTorBlock")
    window = MainWindow()
    window.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
    window.browser.page().fullScreenRequested.connect(window.fulsc)
    
    app.exec_()