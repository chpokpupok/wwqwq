import sys
from PIL import Image, ImageDraw, ImageFilter
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('foto.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')
        self.image = QLabel(self)
        self.image.move(100, 60)
        self.image.resize(400, 400)
        im_rgb = Image.open('1.jpg')
        im_rgb.putalpha(255)
        im_rgb.save('1.png')
        self.pixmap = QPixmap('1.png')
        self.image.setPixmap(self.pixmap)
        self.sld.valueChanged.connect(self.run)
    def run(self):
        self.n = int(2.55 * self.sld.value())
        im_rgb = Image.open('1.jpg')
        im_rgb.putalpha(self.n)
        im_rgb.save('1.png')
        self.pixmap = QPixmap('1.png')
        self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())