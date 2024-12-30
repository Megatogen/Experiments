import math
import matplotlib.pyplot as plt

#функции для градусов(мне так удобнее)
def sin(degrees):
	return math.sin(math.radians(degrees))
def cos(degrees):
	return math.cos(math.radians(degrees))
def tan(degrees):
	return math.tan(math.radians(degrees))
def ctg(degrees):
	return 1 / math.tan(math.radians(degrees))
def arcsin(degrees):
	return math.asin(math.radians(degrees))
def arccos(degrees):
	return math.acos(math.radians(degrees))
def arctan(degrees):
	return math.atan(math.radians(degrees))
def arcctg(degrees):
	return math.pi / 2 - math.atan(math.radians(degrees))
	


# Setting							# Name		<> Value		<> Comment
g = 9.81     						# g  		<> (m/s^2)		<> Ускорение свободного падения (м/с²)
Cd = float(input("Cd: ")) 			# Cd 		<> (ratio)		<> Коэффициент лобового сопротивления для сферы
A = float(input("A: "))  			# A  		<> (m^2)		<> Площадь поперечного сечения (м²)
p = 1.225  							# p  		<> (kg/m^3)		<> Плотность воздуха (кг/м³) #резерв для вычисления плотности по высоте
m = float(input("m: "))				# m  		<> (kg)			<> Масса снаряда (кг)
v = float(input("v: "))				# v 		<> (m/s)		<> Начальная скорость 
v_angle = float(input("Angle: "))	# v_angle	<> (degrees)	<> Угол запуска снаряда относительно земли 
step = float(input("Step: "))		# step		<> (seconds)	<> Шаг просчёта
x = 0								# x			<> (int)		<> Координата x в момент времени
y = 0								# y			<> (int)		<> координата y в момент времени

#создание графика
plt.ion()
plt.xlabel("Distance (X axis, meters)")
plt.ylabel('Height (Y axis, meters)')
plt.title("The trajectory of the projectile, taking into account the aerodynamic drag")
plt.axis("equal")
plt.scatter(0, 0)
plt.show()
plt.pause(1)

while y>=0:
	#Fd
	Fd = 0.5 * Cd * A * p * v**2
	#v по базису
	vy = v * cos(v_angle)
	vx = v * sin(v_angle)
	#Fd по базису
	Fdy = -Fd * cos(v_angle)
	Fdx = -Fd * sin(v_angle)
	#Ускорения
	ay = -g + Fdy / m
	ax = -Fdx / m
	#Дельты
	dx = vx * step + 0.5 * ax * step**2
	dy = vy * step + 0.5 * ay * step**2
	y += dy
	x += dx
	vy += ay * step
	vx += ax * step
	#Общий вектор по Пифагору
	v = math.sqrt(vx**2+vy**2)
	#Угол скорости
	try:
		v_angle = arctan(dy/dx)
	except Exception:
		if vy > 0:
			v_angle = 90
		elif vy == 0:
			v_angle = 0
		else:
			v_angle = -90
	plt.scatter(x, y)
	plt.draw()
input("Type anything to exit: ")