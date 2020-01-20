import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from Parser import parse


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.run)

    def quadratic_function(self):
        ix_b = str(-int(self.input_b.text()))
        ix2a = '2 * ' + self.input_a.text()
        count = abs(len(ix_b) - len(ix2a)) / 2
        self.ix_b.setText(' ' + round(count)
                          * ' ' + ix_b + ' ' * round(count) if len(ix_b) < len(ix2a) else ix_b)
        self.ix__.setText('_' * len(ix_b) if len(ix_b) > len(ix2a) else '_' * (len(ix2a) - 1))
        self.ix2a.setText(' ' + round(count) * ' ' + ix2a + ' ' * round(count) if len(ix_b) > len(ix2a) else ix2a)
        self.first_eq.setText('x =     =' + max(len(ix2a), len(ix_b)) * ' ' + '    ' + '= ' + str(
            round(eval(ix_b + '/' + '(' + ix2a + ')'), 2)))
        x_b = eval(ix_b + '/' + '(' + ix2a + ')')
        self.label.setText(str(x_b))
        minus = int(x_b - x_b * 3)
        plus = int(x_b + x_b * 3)
        self.graphicsView.clear()
        if x_b <= 0:
            need = plus, minus
        else:
            need = minus, plus
        if abs(need[0]) - abs(need[1]) in [1, -1, 0]:
            need = need[0] - 5, need[1] + 5
        self.graphicsView.plot(
            [i for i in range(need[0], need[1] + 1)],
            [int(self.input_a.text()) * (i ** 2) + int(self.input_b.text())
             * i + int(self.input_c.text()) for i in range(need[0], need[1] + 1)])

    def run(self):
        if self.input_a.text() and self.input_b.text() and self.input_c.text():
            if self.input_a.text() != '0':
                self.quadratic_function()
            elif self.input_a.text() == '0':
                self.linear_function()
        else:
            self.label.setText('Вы ввели некорректное значение.')
            self.ix_b.setText('')
            self.ix__.setText('')
            self.ix2a.setText('')
            self.first_eq.setText('x =     = ...')
            self.graphicsView.clear()

print(parse('123+15x+32^7-(-(12x))'))
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())


