This program code is a graphical application for automating manual traction and braking calculations for rail transport.

Purpose of the program
The program calculates the maximum temperature on the friction surface of the braking system during braking and plots temperature changes during braking, as well as outputs the numerical characteristics of the graph in a separate text file.

**How to use the program**

**1. Input of the initial data:**
Locomotive/wagon - choosing the type of rolling stock
Load q0 - load from the wheelset on the rails (ton-force/axle)
Brake pad type - choose from 4 options:
Cast-iron sectional doors (four per wheel)
Single cast iron (two per wheel)
Single cast iron (one per wheel)
Composite
Initial braking speed V0 (km/h)
Braking time to stop tb (s)
Brake preparation time tp (s)
Braking distance length St (m)
Descent slope i (%)

**2. Calculation:**
Click the "Calculate" button

**3. Getting results:**
The maximum temperature on the friction surface (°C) is displayed in the output field
The graph shows the temperature change during braking

**Technical details**
The program takes into account various factors:
The type of rolling stock (locomotive/wagon)
and the material of the brake pads.
Axle load
Initial velocity
Braking time parameters
The length of the braking distance
The slope of the path
The code is based on the formulas derived by V.G. Inozemtsev in the book Automatic brakes 1981
The calculation is performed using a thermophysical model that takes into account the intensity of braking and heat dissipation from friction surfaces.

======================================================================================================================================================================

Данный программный код представляет собой графическое приложение для автоматизации ручных методов тяговыъ и тормозных расчетов для рельсового транспорта.

Назначение программы
Программа рассчитывает максимальную температуру на поверхности трения тормозной системы во время торможения и строит график изменения температуры в процессе торможения, а также выводит численные характеристики графика в отдельный текстовый файл.

**Как пользоваться программой**

**1. Ввод исходных данных:**
Локомотив/вагон - выбор типа подвижного состава
Нагрузка q0 - нагрузка от колесной пары на рельсы (тонна-сила/ось)
Тип тормозной колодки - выбор из 4 вариантов:
Чугунные секционные (по четыре на колесо)
Одинарные чугунные (по две на колесо)
Одинарные чугунные (по одной на колесо)
Композиционные
Начальная скорость торможения V0 (км/ч)
Время торможения до остановки tв (с)
Время подготовки тормозов tп (с)
Длина тормозного пути Sт (м)
Наклон спуска i (%)

**2. Расчет:**
Нажать кнопку "Рассчитать"

**3. Получение результатов:**
В поле вывода отображается максимальная температура на поверхности трения (°C)
На графике отображается изменение температуры в процессе торможения

**Технические детали**
Программа учитывает различные факторы:
Тип подвижного состава (локомотив/вагон)
Материал тормозных колодок
Нагрузку на ось
Начальную скорость
Временные параметры торможения
Длину тормозного пути
Уклон пути
Код написана на основе выведенных формул В.Г. Иноземцевым в книге Автоматические тормоза 1981
Расчет выполняется по теплофизической модели, учитывающей интенсивность торможения и теплоотвод от поверхностей трения.
