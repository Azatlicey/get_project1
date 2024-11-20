import sqlite3
import sys
# тест
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн

        # счетчик. По кругу меняется
        self.step = 0

        self.connection = sqlite3.connect("coffee.sqlite")

        self.pushButton_1.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)



    def run_1(self):
        self.label_7.move(260, 500)

        res = self.connection.cursor().execute(
            """
            SELECT * FROM coffee
               """).fetchall()

        self.step %= len(res)
        i = self.step
        self.lineEdit_1.setText(res[i][1])
        self.lineEdit_2.setText(res[i][2])
        self.lineEdit_3.setText(res[i][3])
        self.lineEdit_4.setText(res[i][4])
        self.lineEdit_5.setText(str(res[i][5]))
        self.lineEdit_6.setText(str(res[i][6]))

        self.step += 1

    def run_2(self):
        #  Выводит запись " Ваш заказ принят"
        self.label_7.move(260,150)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setFixedSize(750, 200)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
