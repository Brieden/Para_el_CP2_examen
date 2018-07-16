import numpy as np
import matplotlib.pyplot as plt


def Aufgabe_8_2():
	du_dx = lambda x, fun, h: (fun(x + h) - fun(x)) / h
	d2u_dx2 = lambda x, fun, h: (fun(x + 2*h) - 2 * fun(x + h) + fun(x)) / h**2
	d3u_dx3 = lambda x, fun, h: (fun(x + 3*h) - 3 * fun(x + 2*h) + 3 * fun(x + h) - fun(x)) / h**3
	d4u_dx4 = lambda x, fun, h: (fun(x + 4*h) - 4 * fun(x + 3*h) + 6*fun(x + 2*h) - 4*fun(x + h) + fun(x)) / h**4

	x = np.linspace(0, 10, 100)
	funk = lambda x: np.sin(x)
	plt.plot(x,  du_dx(x,funk, 1e-2)), plt.plot(x,d2u_dx2(x,funk, 1e-2))
	plt.plot(x,d3u_dx3(x,funk, 1e-2)), plt.plot(x,d4u_dx4(x,funk, 1e-2))
	plt.plot(x,np.sin(x) , "--")
	plt.title("Numerische Ableitungen bis 4en Grades mit Darstellung von $f(x) = \sin(x)$ als Test")
	plt.show()


	x_min, x_max, points = 0, 10, 100
	x, dx = np.linspace(x_min, x_max, points), (x_max - x_min) / points
	y = np.sin(x)
	D4x = (y[4:] - 4 * y[3:-1] + 6 * y[2:-2] - 4 * y[1:-3] + y[:-4]) / dx **4
	plt.plot(D4x), plt.plot(y, "--")
	plt.title("Differenzial der 4. Ableitung als Vektorgleichung")
	plt.show()


	x_min, x_max, points = 0, 10, 200
	x, dx = np.linspace(x_min, x_max, points), (x_max - x_min) / points
	y = np.sin(x)

	D4_Matrix = (np.eye(points) 
		         - 4 * np.eye(points, k=1) + 6 * np.eye(points, k=2) 
		         - 4 * np.eye(points, k=3) + np.eye(points, k=4)
		    ) / dx**4
	plt.plot(np.dot(D4_Matrix, y)[:-4]), plt.plot(y, "--")
	plt.title("Differenzial der 4. Ableitung als Matrixgleichung")
	plt.show()



def Aufgabe_8_3():
	N = np.logspace(0, 8.5, 50)
	γ_wiki = 0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495
	γ = lambda N: sum([1/(N - n) for n in range(N)]) - np.log(N) - γ_wiki
	plt.plot([int(N_n) for N_n in N], [γ(int(N_n)) for N_n in N], "x")
	plt.loglog(), plt.xlabel(" Number of terms in the sum N"), plt.ylabel("difference to the literary value")
	plt.title("remainder for Number of terms in the sum to calculate Euler constant")
	plt.show()


Aufgabe_8_2()
Aufgabe_8_3()








