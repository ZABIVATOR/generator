import math as m
import numpy as np
import sys
import vtk
# Класс расчётной сетки
class CalcMesh:

	# Конструктор сетки size x size точек с шагом h по пространству
	def __init__(self, size):
		# 2D-сетка из расчётных точек, у каждой из которых, тем не менее, 3 координаты
		self.nodes = np.mgrid[0:size:np.complex128(size), 0:size:np.complex128(size)]
		self.nodes *= 1/size
		self.eps = sys.float_info.epsilon
		self.r = 1
		self.size = 12
		self.dt = 0.1
		self.h = 1/size
		self.circle = []
		self.alpha = [0, m.pi*1/6, m.pi*1/3, m.pi*1/2, m.pi*2/3, m.pi*5/6, m.pi*1, -m.pi*5/6, -m.pi*2/3, -m.pi*1/2, -m.pi*1/3, -m.pi*1/6]
		for i in range(12):
			 point = [self.r*m.cos(self.alpha[i]), self.r*m.sin(self.alpha[i])]
			 #print(m.sqrt(point[0]**2+point[1]**2), '\n')
			 self.circle.append(point)
		self.curve = [[2, 0], [3, 1], [2, 2], [1,3], [0, 2], [-1, 3], [-1, 2], [-2, 0], [0, -4], [1, -3], [2,-2], [3, -1]]
		print(self.circle)
		for i in range (self.size):
			self.nodes[0][0,i]= self.curve[i][0]
			self.nodes[1][0,i]= self.curve[i][1]
			self.nodes[0][size-1,i]= self.circle[i][0]
			self.nodes[1][size-1,i]= self.circle[i][1]
		print(self.nodes)

	# Метод отвечает за запись текущего состояния сетки в снапшот в формате VTK
	def snapshot(self, snap_number):
		# Сетка в терминах VTK
		structuredGrid = vtk.vtkStructuredGrid()
		# Точки сетки в терминах VTK
		points = vtk.vtkPoints()

		# Обходим все точки нашей расчётной сетки
		# Делаем это максимально неэффективным, зато наглядным образом
		number = len(self.nodes[0])
		for i in range(0, number):
			for j in range(0, number):
				# Вставляем новую точку в сетку VTK-снапшота
				points.InsertNextPoint(self.nodes[0][i,j], self.nodes[1][i,j], 0)

		# Задаём размеры VTK-сетки (в точках, по трём осям)
		structuredGrid.SetDimensions(number, number, 1)
		# Грузим точки в сетку
		structuredGrid.SetPoints(points)

		# Создаём снапшот в файле с заданным именем
		writer = vtk.vtkXMLStructuredGridWriter()
		writer.SetInputDataObject(structuredGrid)
		writer.SetFileName("aaaaaaaaa" + str(snap_number) + ".vts")
		writer.Write()
		
		
	def laplas(self,dt, h):
		val_present=[0, 0]
		val_previous=[1, 1]
		
		while (abs(val_present[0] - val_previous[0]) > self.eps) and (abs(val_present[1] - val_previous[1]) > self.eps):
			for i in range(1, self.size):
				for j in range(1, self.size):
					val_previous = (self.nodes[0][i,j], self.nodes[1][i,j])
					for o in range(2):
						f_i_j=self.nodes[o][i,j]
						f_1=self.nodes[o][i+1,j]
						f_2=self.nodes[o][i-1,j]
						f_3=self.nodes[o][i,j-1]
						self.nodes[o][i,j] = f_i_j - dt/h**2 * ( f_1 - 4*f_i_j + f_2 + f_3 )
					val_present = (self.nodes[0][i,j], self.nodes[1][i,j])
					print(val_present)
					print(val_previous)
		return f

# Размер расчётной сетки, точек на сторону
size = 12

# Шаг по времени
tau = 0.01

# Создаём сетку заданного размера
m = CalcMesh(size)
#m.laplas(tau,1/size)
# Пишем её начальное состояние в VTK
m.snapshot(0)
