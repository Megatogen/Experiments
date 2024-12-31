import math
import matplotlib.pyplot as plt

#сокращение названий функций
def sin(radians):
	return math.sin(radians)
def cos(radians):
	return math.cos(radians)
def tan(radians):
	return math.tan(radians)
def ctg(radians):
	return 1 / math.tan(radians)
def arcsin(radians):
	return math.asin(radians)
def arccos(radians):
	return math.acos(radians)
def arctan(radians):
	return math.atan(radians)
def arcctg(radians):
	return math.pi / 2 - math.atan(radians)
	


# Setting										# Name		<> Value		<> Comment
g = 9.81     									# g  		<> (m/s^2)		<> Ускорение свободного падения (м/с²)
Cd = float(input("Cd: ")) 						# Cd 		<> (ratio)		<> Коэффициент лобового сопротивления для сферы
A = float(input("A: "))  						# A  		<> (m^2)		<> Площадь поперечного сечения (м²)
p = 1.225  										# p  		<> (kg/m^3)		<> Плотность воздуха (кг/м³) #резерв для вычисления плотности по высоте
m = float(input("m: "))							# m  		<> (kg)			<> Масса снаряда (кг)
v = float(input("v: "))						# v 		<> (m/s)		<> Начальная скорость 
v_angle = math.radians(float(input("Angle: ")))	# v_angle	<> (degrees)	<> Угол запуска снаряда относительно земли 
step = float(input("Step(<1): "))				# step		<> (seconds)	<> Шаг просчёта
x = 0											# x			<> (int)		<> Координата x в момент времени
y = 0											# y			<> (int)		<> координата y в момент времени
xpos = [0]										# xpos		<> (array)		<> Массив положений по x, исп. для отрисовки
ypos = [0]										# ypos		<> (array)		<> массив положений по y, исп. для отрисовки
xforax = [0]									# xforax	<> (array)		<> Массив, содержащий нулевые координаты x
yforax = [0, 0]									# yforax	<> (array)		<> Массив, содержащий нулевые координаты y
inRealTime = False								# inRealTime<> (boolean)	<> Флаг, отвечающий за отрисовку в реальном времени
v0 = v
inpt = input("Draw in real time? 1 or true, other - false: ")
if inpt=="1" or inpt.lower()=="true":
	inRealTime = True
else:
	inRealTime = False

#создание графика
plt.ion()
plt.xlabel("Distance (X axis, meters)")
plt.ylabel('Height (Y axis, meters)')
plt.title("Cd="+str(Cd)+", A="+str(A)+", m="+str(m)+", start v="+str(v0)+". Step="+str(step)+" seconds.")
plt.axis("equal")
plt.show()
plt.pause(0.001)

while y>=0:
	#Fd
	Fd = 0.5 * Cd * A * p * v**2
	#v по базису
	vx = v * cos(v_angle)
	vy = v * sin(v_angle)
	#Fd по базису
	Fdx = -Fd * cos(v_angle)
	Fdy = -Fd * sin(v_angle)
	#Ускорения
	ay = -g + Fdy / m
	ax = Fdx / m
	#Дельты
	dx = vx * step + 0.5 * ax * step**2
	dy = vy * step + 0.5 * ay * step**2
	x += dx
	y += dy
	vx += ax * step
	vy += ay * step
	#Общий вектор по Пифагору
	v = math.sqrt(vx**2+vy**2)
	#Угол скорости
	if vx != 0:
		v_angle = math.atan2(vy, vx)
	else:
		v_angle = math.copysign(math.pi/2, vy)
	#Отрисовка траектории на графике
	xpos.append(x)
	ypos.append(y)
	xforax.append(x)
	plt.plot(xforax, yforax, "r-")
	xforax.pop(1)
	plt.plot(xpos, ypos, "g--")
	plt.xlabel("Distance (X axis, meters)")
	#Дублируем заголовки и подписи на случай закрытия окна и обновляем координаты
	plt.ylabel('Height (Y axis, meters)')
	plt.title("Cd="+str(Cd)+", A="+str(A)+", m="+str(m)+", start v="+str(v0)+". Step="+str(step)+" seconds.\nTotal pos.: "+str(round(x))+";"+str(round(y))+", total v="+str(round(v)))
	plt.axis("equal")
	plt.draw()
	if inRealTime == True:
		plt.pause(step)
input("Trajectory ending on "+str(xpos[-1])+";"+str(ypos[-1]))