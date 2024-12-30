import math
import matplotlib as plt

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
	


# Setting					# Name		<> Value		<> Comment
g = 9.81     				# g  		<> (m/s^2)		<> Ускорение свободного падения (м/с²)
Cd = input("Cd: ") 			# Cd 		<> (ratio)		<> Коэффициент лобового сопротивления для сферы
A = input("A: ")  			# A  		<> (m^2)		<> Площадь поперечного сечения (м²)
p = 1.225  					# p  		<> (kg/m^3)		<> Плотность воздуха (кг/м³) #резерв для вычисления плотности по высоте
m = input("m: ")			# m  		<> (kg)			<> Масса снаряда (кг)
v = input("v: ")			# v 		<> (m/s)		<> Начальная скорость 
v_angle = input("Angle: ")	# v_angle	<> (degrees)	<> Угол запуска снаряда относительно земли 
step = input("Step: ")		# step		<> (seconds)	<> Шаг просчёта
x = 0						# x			<> (int)		<> Координата x в момент времени
y = 0						# y			<> (int)		<> координата y в момент времени

#создание графика
plt.ion()
plt.xlabel("Distance (X axis, meters)")
plt.ylabel('Height (Y axis, meters)')
plt.title("The trajectory of the projectile, taking into account the aerodynamic drag")
plt.show()
#Основные вычисления
#Пока высота не равна нулю:
#	#посчитать Fd 
#	#разложить v по базису
#	#разложить Fd по базису
#	#сложить горизонтальные, вертикальные базисы
#	#по сумме базисов найти угол скорости
#	#изменить y
#	#изменить x
	#отобразить на графике|



#while y>=0:
	#Fd = 0.5 * Cd * A * p * v**2
	#Fd_angle = v_angle + 180
	# -----
	#vy = v * sin(v_angle)
	#vx = v * cos(v_angle)
	#-----
	#Fdy = Fd * sin(Fd_angle)
	#Fdx = Fd * cos(Fd_angle)
	#ay = Fdy / m
	#ax = Fdx / m
	#-----
	#dy = (vy - ay - g)*step
	#dx = (vx - ax)*step
	#-----
	#v_angle = arctan(dy/dx)
	#-----
	#y += dy
	#x += x
	#-----
	#plt.scatter(x, y)
	#plt.draw()
input("Type anything to exit: ")