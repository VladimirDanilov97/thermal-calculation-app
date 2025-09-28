import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, \
    QHBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import math
from matplotlib.ticker import MaxNLocator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тепловой расчет")
        width = 1200
        height = 500
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        # Создание виджетов
        self.train_type_label = QLabel("Локомотив/вагон:")
        self.train_type_checkbox = QComboBox()
        self.train_type_checkbox.addItems(["Локомотив", "Вагон"])

        self.q0_label = QLabel("Нагрузка, передаваемая от колесной пары на рельсы q0, тонна-сила/ось")
        self.q0 = QLineEdit()

        self.brake_material_label = QLabel("Тип тормозной колодки:")
        self.brake_material_input = QComboBox()
        self.brake_material_input.addItems([
            "Чугунные секционные (по четыре на колесо)",
            "Одинарные чугунные (по две на колесо)",
            "Одинарные чугунные (по одной на колесо)",
            "Композиционные"
        ])

        self.speed_label = QLabel("Начальная скорость торможения V0 км/ч:")
        self.speed_input = QLineEdit()

        self.tv_label = QLabel("Время торможения до остановки tв, с")
        self.tv = QLineEdit()

        self.tp_label = QLabel("Время подготовки тормозов tп, с")
        self.tp = QLineEdit()

        self.s_label = QLabel("Длина тормозного пути Sт, м")
        self.s = QLineEdit()

        self.ic_label = QLabel("Наклон спуска i, %")
        self.ic = QLineEdit()

        self.calculate_button = QPushButton("Рассчитать")
        self.calculate_button.clicked.connect(self.calculate)

        self.output_label = QLabel("Максимальная температура на поверхности трения, °C:")
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)

        # Создание графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot()

        # Создание компоновщиков
        main_layout = QHBoxLayout()
        variable_layout = QVBoxLayout()

        # Размещение переменных
        variable_layout.addWidget(self.train_type_label)
        variable_layout.addWidget(self.train_type_checkbox)
        variable_layout.addWidget(self.brake_material_label)
        variable_layout.addWidget(self.brake_material_input)
        variable_layout.addWidget(self.q0_label)
        variable_layout.addWidget(self.q0)
        variable_layout.addWidget(self.tv_label)
        variable_layout.addWidget(self.tv)
        variable_layout.addWidget(self.tp_label)
        variable_layout.addWidget(self.tp)
        variable_layout.addWidget(self.speed_label)
        variable_layout.addWidget(self.speed_input)
        variable_layout.addWidget(self.s_label)
        variable_layout.addWidget(self.s)
        variable_layout.addWidget(self.ic_label)
        variable_layout.addWidget(self.ic)
        variable_layout.addWidget(self.calculate_button)
        variable_layout.addWidget(self.output_label)
        variable_layout.addWidget(self.result_output)

        main_layout.addLayout(variable_layout)
        main_layout.addWidget(self.canvas)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def calculate(self):
        try:
            # Валидация входных данных
            speed_kmh = float(self.speed_input.text())
            speed = speed_kmh / 3.6
            q0_ton = float(self.q0.text())
            q0 = q0_ton * 9.80665 * 1000  # переводим в Ньютоны
            tp = float(self.tp.text())
            tv = int(self.tv.text())
            S = float(self.s.text())
            ic = float(self.ic.text())

            # Проверка на корректность данных
            if S <= speed * tp:
                self.result_output.setText("Ошибка: S должно быть > V0*tп")
                return

            if tv <= 0:
                self.result_output.setText("Ошибка: время торможения должно быть > 0")
                return

            tv_list = list(range(1, tv + 1))

            # Определение параметров в зависимости от выбора
            if self.train_type_checkbox.currentText() == "Локомотив":
                R = 1.050
                if self.brake_material_input.currentText() == "Чугунные секционные (по четыре на колесо)":
                    ar = 0.6
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                elif self.brake_material_input.currentText() == "Одинарные чугунные (по две на колесо)":
                    ar = 0.7
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                elif self.brake_material_input.currentText() == "Одинарные чугунные (по одной на колесо)":
                    ar = 0.8
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                else:  # Композиционные
                    ar = 0.95
                    pi_lambda_gamma_c = 0.62
                    alpha0 = 0.4 / 100 * (1 + 1.33 * math.sqrt(speed))
            else:  # Вагон
                R = 0.95
                if self.brake_material_input.currentText() == "Чугунные секционные (по четыре на колесо)":
                    ar = 0.55
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                elif self.brake_material_input.currentText() == "Одинарные чугунные (по две на колесо)":
                    ar = 0.65
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                elif self.brake_material_input.currentText() == "Одинарные чугунные (по одной на колесо)":
                    ar = 0.7
                    pi_lambda_gamma_c = 6.08
                    alpha0 = 0.004 + 0.005 * math.sqrt(speed)
                else:  # Композиционные
                    ar = 0.95
                    pi_lambda_gamma_c = 0.62
                    alpha0 = 0.4 / 100 * (1 + 1.33 * math.sqrt(speed))

            # Защита от нулевого alpha0
            if alpha0 <= 0:
                alpha0 = 0.001

            list_ = []
            result = perform_heat_calculation(speed, q0, ar, ic, pi_lambda_gamma_c, R, S, tp, tv_list, alpha0, list_)

            self.result_output.setText(str(result))
            self.plot(list_)

        except ValueError as e:
            self.result_output.setText("Ошибка ввода данных")
        except Exception as e:
            self.result_output.setText(f"Ошибка: {str(e)}")

    def plot(self, list_):
        if not list_:
            return

        self.figure.clear()
        ax = self.figure.add_subplot()

        x_data = list(range(1, len(list_) + 1))
        y_data = list_

        ax.plot(x_data, y_data)
        ax.set_xlabel("Время торможения, сек")
        ax.set_ylabel("Температура на поверхности трения, °C")

        # Настройка целочисленных делений
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        self.canvas.draw()


def perform_heat_calculation(speed, q0, ar, ic, pi_lambda_gamma_c, R, S, tp, tv_list, alpha0, list_):
    try:
        # Защита от деления на ноль и отрицательных значений
        denominator = 2 * (S - speed * tp)
        if denominator <= 0:
            return 0

        bt = 108 * speed * speed / denominator - 2 - ic

        # Защита от отрицательного bt
        if bt < 0:
            bt = 0

        qt = ar * bt * q0 * speed / (17080 * math.pi * R * 0.09)

        max_tv = max(tv_list) if tv_list else 1

        for i in tv_list:
            if i <= 0:
                continue

            try:
                exponent = -2 * alpha0 * math.sqrt(i) * (1 - 2 * i / 3 / max_tv) / pi_lambda_gamma_c
                # Ограничиваем exponent чтобы избежать переполнения
                exponent = max(min(exponent, 100), -100)

                t = qt / alpha0 * (1 - math.exp(exponent))
                list_.append(round(t, 2))
            except (ValueError, ZeroDivisionError):
                list_.append(0)

        if list_:
            result = round(max(list_), 2)
        else:
            result = 0

        return result

    except Exception as e:
        print(f"Ошибка в расчетах: {e}")
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())