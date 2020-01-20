import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from ui2 import Ui_MainWindow
import sqlite3
from Parser import parse
import math
import numpy as np


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_value.hide()
        self.first_var.hide()
        self.second_value.hide()
        self.second_var.hide()
        self.var_text.hide()
        self.flag = False
        self.flag_2 = False
        self.inf.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.con = sqlite3.connect('Equals.db')
        self.cur = self.con.cursor()
        self.start.clicked.connect(self.run)
        self.buttonGroup.buttonClicked.connect(self.run_btn_pressed)

    # Функциональная часть. Здесь выполняем вычисления. Выполняется по нажатию кнопки "Вычислить"
    def run(self):
        # Проверка, что выбрана функция. Если выбора нет - кнопка "Вычислить" ничего не делает.
        try:
            for_eval = self.cur.execute("""SELECT for_eval FROM Equal WHERE id LIKE '{}'"""
                                        .format(self.need_id)).fetchall()[0][0]
            needed_array = self.cur.execute("""SELECT array FROM Equal WHERE id LIKE '{}'"""
                                            .format(self.need_id)).fetchall()[0][0]
            needed_inf = self.cur.execute("""SELECT inf FROM Equal WHERE id LIKE '{}'"""
                                          .format(self.need_id)).fetchall()[0][0]

            input = 1
            input_2 = 1
            # Находим значения переменных, если они имеются.
            if self.flag:
                input = parse(self.first_value.text())
                if self.flag_2:
                    input_2 = parse(self.second_value.text())
            # Проверяем, введены ли переменные.
            if input == 'ERROR' or input_2 == 'ERROR':
                self.inf.setText('Ошибка.')
                self.graph.clear()
                return
            else:
                # Если проблем с переменными нет - выполняем вычисления.
                self.graph.clear()
                # Если возникает какая-то ошибка в вычислениях, просто выводим ошибку.
                try:
                    self.graph.plot(
                        [i for i in eval(needed_array)],
                        [eval(for_eval.format(input, input_2)) for i in eval(needed_array)],
                        connect='finite'
                    )
                    self.inf.setText(needed_inf)
                except BaseException:
                    self.inf.setText('Ошибка.')
        except BaseException:
            pass

    # По большей части редактируем дизайн. Находим значения возможных переменных.
    def run_btn_pressed(self, button):
        self.equal_text.setText('Выбрано уравнение: {}'.format(button.text()))
        # Находим id необходимой нам функции
        needed_id = self.cur.execute("""SELECT id FROM Equal WHERE with_y LIKE '{}'"""
                                     .format(button.text())).fetchall()
        # Находим пременные необходимой нам функции
        needed_vars = self.cur.execute("""SELECT variables FROM Equal WHERE with_y LIKE '{}'"""
                                       .format(button.text())).fetchall()
        # В возможных вариантах выбора есть функции, которые не требуют дополнительных значений
        # Поэтому рассматриваем функции, не входящие в этот список
        self.need_id = int(needed_id[0][0])
        if self.need_id not in [2, 4, 7, 8, 10, 11, 12, 13]:
            self.flag = True
            self.flag_2 = False
            self.first_value.clear()
            self.second_var.hide()
            self.second_value.hide()
            self.var_text.show()
            self.first_value.show()
            self.first_var.show()
            self.first_var.setText(needed_vars[0][0] + ' = ')
        # Функция с двумя переменными только одна kx + b. k и b. Её id = 2
        elif self.need_id == 2:
            self.flag = True
            self.flag_2 = True
            self.first_value.clear()
            self.second_value.clear()
            self.var_text.show()
            self.first_value.show()
            self.first_var.show()
            self.second_value.show()
            self.second_var.show()
            self.first_var.setText(needed_vars[0][0].split(', ')[0] + ' = ')
            self.second_var.setText(needed_vars[0][0].split(', ')[1] + ' = ')
        else:
            self.flag = False
            self.flag_2 = False
            self.first_value.clear()
            self.second_value.clear()
            self.var_text.hide()
            self.first_value.hide()
            self.first_var.hide()
            self.second_value.hide()
            self.second_var.hide()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
