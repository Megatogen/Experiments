import math

#функции для градусов(мне так удобнее)
def sin(degrees):
	return math.sin(math.radians(degrees))
def cos(degrees):
	return math.cos(math.radians(degrees))
def tan(degrees):
	return math.tan(math.radians(degrees))
def ctg(degrees):
	return math.tan(math.radians(degrees))/1
def arcsin(degrees):
	return math.asin(math.radians(degrees))
def arccos(degrees):
	return math.acos(math.radians(degrees))
def arctan(degrees):
	return math.atan(math.radians(degrees))
def arcctg(degrees):
	return (math.pi/2) - math.atan(math.radians(degrees))
	
"""
Псевдокод:
	t = 0
	разложить на вектора
	while y >0:
		посчитать силу сопротивления
		разложить на вектора
		посчитать ускорения по векторам
		изменить скорости
		изменить координаты
"""

#Основной код вычислений

class ballistic():
	def iterative_param(angle, speed, mass, A, Cd, rho):
		import numpy as np
		from scipy.integrate import odeint
		import matplotlib.pyplot as plt

		# Параметры
		g = 9.81  # Ускорение свободного падения (м/с²)
		C_d = 0.47  # Коэффициент лобового сопротивления для сферы
		A = A  # Площадь поперечного сечения (м²)
		rho = rho  # Плотность воздуха (кг/м³)
		m = mass  # Масса снаряда (кг)
		V_0 = speed  # Начальная скорость (м/с)
		alpha = np.radians(45)  # Угол выстрела в радианах

		# Функция для системы ОДУ
		def model(state, t):
			x, y, vx, vy = state
			v = np.sqrt(vx**2 + vy**2)  # Скорость
			dvxdt = -C_d * A * rho * vx * v / (2 * m)
			dvydt = -g - C_d * A * rho * vy * v / (2 * m)
			return [vx, vy, dvxdt, dvydt]

		# Начальные условия: [x0, y0, vx0, vy0]
		initial_state = [0, 0, V_0 * np.cos(alpha), V_0 * np.sin(alpha)]

		# Временной интервал
		t = np.linspace(0, 20, 100)

		# Решение ОДУ
		solution = odeint(model, initial_state, t)

		# Извлечение результатов
		x = solution[:, 0]
		y = solution[:, 1]

		# Построение графика траектории
		plt.plot(x, y)
		plt.xlabel('Расстояние (м)')
		plt.ylabel('Высота (м)')
		plt.title('Траектория полета снаряда с учетом аэродинамического сопротивления')
		plt.grid()
		plt.show()





b = ballistic
b.iterative_param(60, 300, 100, 0.2, 0.5, 1.293)